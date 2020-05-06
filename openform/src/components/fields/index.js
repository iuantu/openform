import TextFieldMeta from './text_field';
import DescriptionFieldMeta from './description';
import SingleSelectFieldMeta from './single_select_field';
import MultipleSelectFieldMeta from './multiple_select_field';
import AttachmentFieldMeta from "./attachment_field";

const metas = [
  TextFieldMeta,
  SingleSelectFieldMeta,
  MultipleSelectFieldMeta,
  DescriptionFieldMeta,
  AttachmentFieldMeta,
];

const d = {}
const editors = {}
const components = {}
const details = {}
const list = {}

metas.forEach((meta) => {
  editors[meta.discriminator] = meta.editor;
  d[meta.discriminator] = meta;
  components[meta.discriminator] = meta.component;
  details[meta.discriminator] = meta.detail;
  list[meta.discriminator] = meta.list;
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
    return category.name === meta.category;
  });

  if (!category || category.length === 0) {
    throw new Error(`Not found category ${meta.category}`)
  }
  category[0].components.push(meta);
})

function getMeta(discriminator) {
  return d[discriminator.replace("_", "-")];
}

export { editors, components, categories, details, list, getMeta };
export default {
  ...d
}