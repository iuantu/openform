import SelectFieldEditor from './SelectFieldEditor'
import * as attrs from '../../cp/form/field/attributes'

export default {
  name: '选择字段',
  discriminator: 'select-field',
  editor: SelectFieldEditor,
  preview: SelectFieldEditor,
  attributes: {
    basic: [
      attrs.FieldAttributeTitle,
      attrs.FieldAttributeDescription,
      attrs.FieldAttributeOption,
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