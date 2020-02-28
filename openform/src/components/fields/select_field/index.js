import TextFieldEditor from './TextFieldEditor'
import TextFieldPreview from './TextFieldPreview'
import * as attrs from '../../cp/form/field/attributes'

export default {
  name: '选择字段',
  discriminator: 'select-field',
  editor: TextFieldEditor,
  preview: TextFieldPreview,
  attributes: {
    basic: [
      attrs.FieldAttributeTitle,
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