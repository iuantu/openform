import SelectFieldEditor from './SelectFieldEditor';
import SelectFieldList from "./SelectFieldList";
import SelectFieldDetail from "./SelectFieldDetail";
import * as attrs from '../../cp/form/field/attributes';
import AbstractFieldAssembler from '../AbstractFieldAssembler';

class SelectFieldAssembler extends AbstractFieldAssembler {

  fromRequestModelToViewModel(requestModel) {
    const viewModel = super.fromRequestModelToViewModel(requestModel);

    let selectedOption = null;

    viewModel.multiple = requestModel.multiple;
    viewModel.type = requestModel.type;
    viewModel.options = requestModel.options.map((option) => {

      const optionViewModel = {
        id: option.id,
        label: option.label,
        value: option.value,
        ordering: option.ordering,
        checked: option.checked,
        editable: option.editable,
        text: "",
      };

      if (optionViewModel.checked) {
        selectedOption = optionViewModel;
      }

      return optionViewModel;
    }).sort((a, b) => {
      return a.ordering - b.ordering;
    });

    if (selectedOption) {
      viewModel.checkedOption = selectedOption.label;
      viewModel.checkedOptionValue = selectedOption.value;
    } else {
      viewModel.checkedOption = null;
      viewModel.checkedOptionValue = null;
    }

    return viewModel;
  }

  fromViewModelToRequestModel(viewModel) {
    const requestModel = super.fromViewModelToRequestModel(viewModel);

    requestModel.type = viewModel.type;
    requestModel.multiple = viewModel.type === "checkbox";
    requestModel.options = viewModel.options.map((option) => {

      const checked = viewModel.multiple ? option.checked
       : viewModel.checkedOptionValue === option.value;

      const requestOption = {
        label: option.label,
        editable: option.editable,
        ordering: option.ordering,
        checked: checked,
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
    return requestModel;
  }

  fromViewModelToAttributeModel(viewModel) {
    const attributeModel = super.fromViewModelToAttributeModel(viewModel);
    attributeModel.options = viewModel.options;
    attributeModel.checkedOption = viewModel.checkedOption;

    return attributeModel;
  }

  fromAttribtueModelToViewModel(viewModel, attribute, value) {
    super.fromAttributeModelToViewModel(viewModel, attribute, value);
    
    viewModel[attribute] = value;
  }

  toFormValueForRequest(viewModel) {
    return viewModel.options
        .filter(opt => opt.checked)
        .map((opt) => {
          return {
            "text": opt.editable ? opt.text : "",
            "value": opt.value,
          }
        })
  }
}

const assembler = new SelectFieldAssembler();

function createDefine() {
  const define = {
    name: '选择',
    discriminator: 'select-field',
    category: 'basic',
    editor: SelectFieldEditor,
    component: SelectFieldEditor,
    list: SelectFieldList,
    detail: SelectFieldDetail,
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
    assembler: assembler,
    default() {
      return {
        discriminator: define.discriminator,
        multiple: define.multiple,
        constraints: [],
        title: "未命名",
        viewId: Math.random(),
        options: [
          {
            label: "选项1",
            editable: false,
            checked: false,
            text: "",
          },
          {
            label: "选项2",
            editable: false,
            checked: false,
            text: "",
          },
          {
            label: "选项3",
            editable: false,
            checked: false,
            text: ""
          }
        ]
      }
    },
    validate(field) {
      const errors = [];
      const checked = field.options.filter(opt => opt.checked);

      if (checked.length === 0) {
        errors.push("必选");
      }

      if (errors.length > 0) {
        field.has_error = true;
        field.errors = errors;
      }
    },
  };

  return define;
}


export default createDefine;