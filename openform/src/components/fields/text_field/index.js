import TextFieldEditor from './TextFieldEditor'
import * as attrs from '../../cp/form/field/attributes'
import AbstractFieldAssembler from '../AbstractFieldAssembler'


/*
class TextFieldAssembler extends AbstractFieldAssembler {
  fromRequestModelToViewModel(requestModel) {
    const viewModel = super.fromRequestToView(requestModel);
  }

  fromViewModelToRequestModel(viewModel) {
    const requestModel = super.fromViewModelToRequestModel(viewModel);
  }

  fromViewModelToAttributeModel(viewModel) {
    const attributeModel = super.fromViewModelToAttributeModel(viewModel);
  }

  fromAttribtueModelToViewModel(viewModel, attribute, value) {
    super.fromAttribtueModelToViewModel(viewModel, attribute, value);
  }
}
*/

class TextFieldAssembler extends AbstractFieldAssembler {
  fromRequestModelToViewModel(requestModel) {
    const viewModel = super.fromRequestModelToViewModel(requestModel);
    viewModel.default = requestModel.default;
    viewModel.placeholder = requestModel.placeholder;
    return viewModel;
  }

  fromViewModelToRequestModel(viewModel) {
    const requestModel = super.fromViewModelToRequestModel(viewModel);
    requestModel.placeholder = viewModel.placeholder;
    requestModel.default = viewModel.default;

    return requestModel;
  }

  fromViewModelToAttributeModel(viewModel) {
    const attributeModel = super.fromViewModelToAttributeModel(viewModel);

    return attributeModel;
  }

  fromAttribtueModelToViewModel(viewModel, attribute, value) {
    super.fromAttributeModelToViewModel(viewModel, attribute, value);

    const textFieldAttributeNames = ['default', 'placeholder'];
    if (textFieldAttributeNames.indexOf(attribute) > -1) {
      viewModel[attribute] = value;
    }
  }

  toFormValueForRequest(viewModel) {
    return viewModel.value;
  }
}

const define = {
  name: '文本字段',
  discriminator: 'text-field',
  category: 'basic',
  editor: TextFieldEditor,
  component: TextFieldEditor,
  assembler: new TextFieldAssembler(),
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
  },
  default() {
    return {
      discriminator: define.discriminator,
      title: '未命名',
      placeholder: '',
      default: '',
      constraints: [],
    }
  },
  validate(field) {
    const errors = [];
    if (!field.value || field.value === "") {
      errors.push("必选");
    }

    if (errors.length > 0) {
      field.has_error = true;
      field.errors = errors;
    }
  },
};

export default define