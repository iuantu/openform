import TextFieldMeta from './text_field'
import DescriptionFieldMeta from './description'

const metas = [
  TextFieldMeta,
  DescriptionFieldMeta
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