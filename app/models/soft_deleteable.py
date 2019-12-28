"""
class SoftDeleteableMixinQuery(BaseQuery):
    _with_deleted = False

    def __new__(cls, *args, **kwargs):
        obj = super(SoftDeleteableMixinQuery, cls).__new__(cls)
        with_deleted = kwargs.pop('_with_deleted', False)
        if len(args) > 0:
            super(SoftDeleteableMixinQuery, obj).__init__(*args, **kwargs)
            return obj.filter_by(deleted_at=None) if not with_deleted else obj
        return obj

    def __init__(self, *args, **kwargs):
        pass

    def with_deleted(self):
        from app import db
        return self.__class__(self.db.class_mapper(self._mapper_zero().class_),
                              session=self.db.session(), _with_deleted=True)

    def _get(self, *args, **kwargs):
        # this calls the original query.get function from the base class
        return super(SoftDeleteableMixinQuery, self).get(*args, **kwargs)

    def get(self, *args, **kwargs):
        # the query.get method does not like it if there is a filter clause
        # pre-loaded, so we need to implement it using a workaround
        obj = self.with_deleted()._get(*args, **kwargs)
        return obj if obj is None or self._with_deleted or not obj.deleted else None
"""