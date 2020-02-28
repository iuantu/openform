import TextFieldMeta from './text_field'
import DescriptionFieldMeta from './description'
import SingleSelectFieldMeta from './select_field'

const metas = [
  TextFieldMeta,
  DescriptionFieldMeta,
  SingleSelectFieldMeta
];

const d = {}
const editors = {}

metas.forEach((meta) => {
  editors[meta.discriminator] = meta.editor
  d[meta.discriminator] = meta
})

export { editors };
export default {
  ...d
}