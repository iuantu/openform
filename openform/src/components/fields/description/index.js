import DescriptionFieldEditor from './DescriptionFieldEditor'
import DescriptionFieldPreview from './DescriptionFieldPreview'
import * as attrs from '../../cp/form/field/attributes'

export default {
  name: '描述',
  discriminator: 'description-field',
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
  }
}