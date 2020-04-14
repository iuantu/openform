import logging
from app import models
from flask_appbuilder import Model
from sqlalchemy import inspect
from app.utils import to_camel_case
from datetime import datetime
from sqlalchemy.orm import class_mapper

def find_model_for_relation(define, field_name):
    for pro in class_mapper(define).iterate_properties:
        if pro.key == field_name:
            return pro.entity.class_

def find_primary_key(define, field_name):
    for pro in class_mapper(define).iterate_properties:
        if pro.key == field_name:
            for column in pro.entity.class_.__table__.columns:
                if column.primary_key:
                    return column

class ModelFactory:

    def clear_relation_field(self, dto):
        """ 创建新的对象时，关系对象还未创建模型，返回无关系对象的字典
        """
        dto = dto.copy()
        return dict([
            (k, v) for k, v in dto.items() if not isinstance(v, (list, ))
        ])

    def not_in_dto(self, primary_key_value, dto_hash_map):
        """ 集合中的对象在请求的数据中不存在
            用在判断集合项被删除的场景
        """
        return not primary_key_value in dto_hash_map

    def remove_model(self, primary_key, model, dto, collection_field_name):
        # logging.debug('remove %s collection' % (collection_field_name))
        collection = getattr(model, collection_field_name)

        dto_hash_map = {}
        for i in dto[collection_field_name]:
            if primary_key.name in i:
                dto_hash_map[i[primary_key.name]] = i

        # logging.debug("collection size %d" % (len(collection)))
        removes = []
        for i in collection:
            primary_key_value = getattr(i, primary_key.name)
            # logging.debug(i.asdict())
            if not primary_key_value:
                logging.debug("not primary key value")
                continue
            
            # logging.debug("primary key: %s, value: %s" % (primary_key.name, primary_key_value,))
            if self.not_in_dto(primary_key_value, dto_hash_map):
                # logging.debug("remove")
                removes.append(i)
                # collection.remove(i)
        
        for remove in removes:
            collection.remove(remove)

    def process_one_to_many(self, model, primary_key, dto_field_name, \
        dto_collection, is_update: bool=False):

        # logging.debug("process one to many, field %s" % dto_field_name)

        relations = getattr(model, dto_field_name)
        model_hash_map = dict([
            (getattr(ins, primary_key.name), ins) for ins in relations
        ])

        for relation_dto in dto_collection:
            has_primary = primary_key.name in relation_dto \
                and relation_dto[primary_key.name] in model_hash_map

            # 有存在的主键id，更新对象
            if has_primary:
                primary_value = relation_dto[primary_key.name]
                update_model = model_hash_map[primary_value]
                self.create_or_update(update_model, relation_dto, is_update)
            else:
                # 无主键id，创建新对象
                obj = self.create_object(
                    model, 
                    self.clear_relation_field(relation_dto), 
                    dto_field_name
                )

                # logging.debug("no primary key: %s %s" % (dto_field_name, obj.asdict()))
                relations.append(obj)

                if isinstance(relation_dto, dict):
                    self.create_or_update(obj, relation_dto, False, skip_remove=True)

    def create_or_update(self, model: Model, dto, is_update: bool=False, skip_remove=False):
        # logging.debug('create or update')
        # logging.debug(type(model))
        # logging.debug(model.asdict())
        for dto_field_name, v in dto.items():
            if isinstance(v, (list,)):
                dto_collection = v
                primary_key = find_primary_key(model.__class__, dto_field_name)

                if is_update and not skip_remove:# and isinstance(dto, dict):
                    # logging.debug('remove model')
                    self.remove_model(primary_key, model, dto, dto_field_name)

                self.process_one_to_many(model, primary_key, dto_field_name, \
                    dto_collection, is_update)

            elif getattr(model, dto_field_name) != v:
                setattr(model, dto_field_name, v)

        return model

    def create_object(self, parent_object, dto, releation_key) -> Model:
        cls_name = parent_object.__class__.__name__

        if "discriminator" in dto:
            dto = dto.copy()
            class_name = to_camel_case(dto['discriminator'])
            class_ = getattr(models, class_name)
            del dto['discriminator']
            obj = class_(**dto)
            return obj

        model = find_model_for_relation(parent_object.__class__, releation_key)
        return model(**dto)
    

class FormAssembler:
    model_factory = ModelFactory()

    def to_model(self, model: Model, dto, is_update: bool=False):
        if not is_update:
            model.user_id = dto['user_id']
        return self.model_factory.create_or_update(model, dto, is_update)