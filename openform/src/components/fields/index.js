import TextFieldMeta from './text_field'
import DescriptionFieldMeta from './description'
import SingleSelectFieldMeta from './single_select_field'
import MultipleSelectFieldMeta from './multiple_select_field'

const metas = [
  TextFieldMeta,
  SingleSelectFieldMeta,
  MultipleSelectFieldMeta,
  DescriptionFieldMeta,
];

const d = {}
const editors = {}

metas.forEach((meta) => {
  editors[meta.discriminator] = meta.editor
  d[meta.discriminator] = meta
})

const categories = [
  {
    name: 'basic',
    label: '基本',
    components: []
  },
  {
    name: 'advance',
    label: '高级',
    components: []
  }
];

metas.forEach((meta) => {
  const category = categories.filter((category) => {
    if (category.name == meta.category)
      return true;
    else
      return false;
  });
  if (category.length == 0) {
    throw new Error(`Not found category ${meta.category}`)
  }
  category[0].components.push(meta);
})

export { editors, categories };
export default {
  ...d
}