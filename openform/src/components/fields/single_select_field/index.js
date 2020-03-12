import createDefine from '../select_field/index'

const meta = createDefine();
meta.name = '单项选择';
const defaultValue = meta.default;
meta.default = ()=> {
    const fieldValue = defaultValue();
    fieldValue.type = 'radio';
    return fieldValue;
}
export default meta