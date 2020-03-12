import TextFieldEditor from './TextFieldEditor'
import TextFieldPreview from './TextFieldPreview'
// import FieldAttributeTitle from '../../cp/form/field/attributes/FieldAttributeTitle'
import * as attrs from '../../cp/form/field/attributes'

const define = {
  name: '文本字段',
  discriminator: 'text-field',
  category: 'basic',
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
  },
  default() {
    return {
      discriminator: define.discriminator,
      title: '未命名',
      placeholder: '',
      default: '',
    }
  },
  viewModelToRequestModel(viewModel, requestModel) {
    requestModel.placeholder = viewModel.placeholder;
    requestModel.default = viewModel.default;
  },
  requestModelToViewModel(requestModel, viewModel) {
    viewModel.default = requestModel.default;
    viewModel.placeholder = requestModel.placeholder;
  },
  attribtueModelToViewModel(viewModel, attribute, value) {
    const textFieldAttributeNames = ['default', 'placeholder'];
    if (textFieldAttributeNames.indexOf(attribute) > -1) {
      viewModel[attribute] = value;
    }
  },
  viewModelToAttributeModel() {

  }
};

export default define