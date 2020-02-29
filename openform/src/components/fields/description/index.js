import DescriptionFieldEditor from './DescriptionFieldEditor'
import DescriptionFieldPreview from './DescriptionFieldPreview'
import * as attrs from '../../cp/form/field/attributes'

const define = {
  name: '描述',
  discriminator: 'description-field',
  category: 'basic',
  editor: DescriptionFieldEditor,
  preview: DescriptionFieldPreview,
  attributes: {
    basic: [
      attrs.FieldAttributeTitle,
    ],
    validation: [
    ],
    layout: [
      // FieldAttributeSelectLayout
    ],
    other: [
      // FieldAttributeHidden
    ]
  },
  default() {
    return {
      discriminator: define.discriminator,
      title: '未命名',
    }
  }
};

export default define