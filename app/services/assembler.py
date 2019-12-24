import logging
from app import models

# def a(self, model, dto, root=True):
#     members = inspect.getmembers(model)

#     if not dto.id or dto.id == 0:
#         pass

#     # 如果是更新对象，则更新里面的数据
#     if not root and update:
#         for member in members:
#             setattr(model, member, dto[member])
#     for member in members:
#         if isinstance(member, list):
#             pass
        
#         model_collection_map = {}
#         dto_collection_map = {}
#         for member_model in getattr(model, member):
#             model_collection_map[member_model.id] = member_model

#         # when has dto and not model, insert
#         # else update
#         for member_dto in dto[member]:
#             is_new = ("id" in member_dto and member_dto["id"] < 1) or not ("id" in member_dto)
            
#             if is_new:
#                 ni = instance(**kw)
#             dto_collection_map[member_dto["id"]] = member_dto

#             if 

#         for member_dto in dto[member]:
#             if "id" in member_dto:
#                 if not member_dto["id"] in model_collection_map:
#                     pass
#         # 如果对象在模型中并不存在则是新增
#         # 如果DTO中有，模型中没有是新增
#         # 如果DTO中没有，模型中有则是删除。
        
        

class FormAssembler:

    def to_model(self, dto):
        if "id" in dto and dto["id"] > 0:
            pass
        else:
            return self.create_model(dto)

    def to_value(self, form, values):
        v = {}

        for field in form.fields:
            is_list = field.discriminator == "select_field" \
                and field.type =="checkbox"

            if is_list:
                v[field.id] = [int(o) for o in values.getlist("%d[]" % field.id)]
            else:
                v[field.id] = field.format(values.get("%d" % field.id))
                    
        value = models.Value(form_id=form.id, values=v)
        return value

    def create_model(self, dto):
        fields = self.create_field_models(dto["fields"])
        form = models.Form(title=dto["title"], fields=fields)
        return form

    def create_field_models(self, dto_list):
        fields = []
        for field_dto in dto_list:
            field_class = models.get_field_by_discriminator(field_dto["discriminator"])
            field_dto_cloned = field_dto.copy()

            if "options" in field_dto_cloned:
                option_dto_list = field_dto_cloned["options"]
                del field_dto_cloned["options"]
                options = self.create_option_models(option_dto_list)
                field_dto_cloned["options"] = options
            field = field_class(**field_dto_cloned)

            # if "options" in field_dto_cloned:
            #     for option in options:
            #         field.options.append(option)

            fields.append(field)
        print(fields)
        return fields

    def create_option_models(self, dto_list):
        options = [models.Option(**option) for option in dto_list]
        for i in range(len(options)):
            options[i].ordering = options[i].value = i
        
        return options