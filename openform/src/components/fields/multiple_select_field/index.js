import createDefine from '../select_field/index';
import * as attrs from '../../cp/form/field/attributes';

const meta = createDefine();
meta.name = '多项选择';
meta.multiple = true;

const defaultValue = meta.default;
meta.default = ()=> {
    const fieldValue = defaultValue();
    fieldValue.type = 'checkbox';
    fieldValue.multiple = true;
    return fieldValue;
}

meta.attributes.validation = [
    attrs.FieldAttributeConstraintRequired,
    [attrs.FieldAttributeConstraintMin, ['最少选', '个选项']],
    [attrs.FieldAttributeConstraintMax, ['最多选', '个选项']],
    attrs.FieldAttributeConstraintErrorMessage,
];

export default meta