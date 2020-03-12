import SelectFieldEditor from './SelectFieldEditor';
import * as attrs from '../../cp/form/field/attributes';

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
        constraints: [],
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
    },
    viewModelToRequestModel(viewModel, requestModel) {
      requestModel.type = viewModel.type;
      requestModel.options = viewModel.options.map((option) => {
        const requestOption = {
          label: option.label,
          editable: option.editable,
          ordering: option.ordering,
        }
        if (option.id) {
          requestOption.id = option.id;
        }
        return requestOption;
      });
  
      for (let i = 0, size = requestModel.options.length; i < size; i++) {
        const option = requestModel.options[i];
        option.ordering = i;
      }
    },
    requestModelToViewModel(requestModel, viewModel) {
      viewModel.multiple = requestModel.multiple;
      viewModel.type = requestModel.type;
      viewModel.options = requestModel.options.map((option) => {
        return {
          id: option.id,
          label: option.label,
          value: option.value,
          ordering: option.ordering,
          editable: option.editable,
        }
      }).sort((a, b) => {
        return a.ordering - b.ordering;
      });
    },
    attribtueModelToViewModel(viewModel, attribute, value) {
      const textFieldAttributeNames = ['default', 'placeholder'];
      if (textFieldAttributeNames.indexOf(attribute) > -1) {
        viewModel[attribute] = value;
      }
    },
    viewModelToAttributeModel(viewModel, attributeValues) {
      attributeValues.options = viewModel.options;
    }
  };

  return define;
}


export default createDefine;