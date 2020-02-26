import TextFieldEditor from './TextFieldEditor'
import TextFieldPreview from './TextFieldPreview'
// import FieldAttributeTitle from '../../cp/form/field/attributes/FieldAttributeTitle'
import * as attrs from '../../cp/form/field/attributes'

export default {
  name: '文本字段',
  discriminator: 'text-field',
  editor: TextFieldEditor,
  preview: TextFieldPreview,
  attributes: {
    basic: [
      attrs.FieldAttributeTitle,
      attrs.FieldAttributeDefault,
      attrs.FieldAttributePlaceholder,
      attrs.FieldAttributeDescription,
    ],
    validation: [
      attrs.FieldAttributeConstraintRequired,
      attrs.FieldAttributeConstraintMin,
      attrs.FieldAttributeConstraintMax,
      attrs.FieldAttributeConstraintErrorMessage,
    ],
    layout: [
      // FieldAttributeSelectLayout
    ],
    other: [
      // FieldAttributeHidden
    ]
  }
}