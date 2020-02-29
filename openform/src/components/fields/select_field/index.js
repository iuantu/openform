import SelectFieldEditor from './SelectFieldEditor'
import * as attrs from '../../cp/form/field/attributes'

function createDefine() {
  const define = {
    name: '选择',
    discriminator: 'select-field',
    category: 'basic',
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
    },
    multiple: false,
    default() {
      return {
        discriminator: define.discriminator,
        multiple: define.multiple,
        options: [
          {
            label: "选项1",
            editable: false,
          },
          {
            label: "选项2",
            editable: false,
          },
          {
            label: "选项3",
            editable: false,
          }
        ]
      }
    }
  };

  return define;
}


export default createDefine;