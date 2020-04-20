import AttachmentFieldEditor from './AttachmentFieldEditor'
import * as attrs from '../../cp/form/field/attributes'
import AbstractFieldAssembler from '../AbstractFieldAssembler'


class AttachmentFieldAssembler extends AbstractFieldAssembler {
  fromRequestModelToViewModel(requestModel) {
    const viewModel = super.fromRequestModelToViewModel(requestModel);
    return viewModel;
  }

  fromViewModelToRequestModel(viewModel) {
    const requestModel = super.fromViewModelToRequestModel(viewModel);

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
}

const define = {
  name: '文本字段',
  discriminator: 'attachment-field',
  category: 'basic',
  editor: AttachmentFieldEditor,
  component: AttachmentFieldEditor,
  assembler: new AttachmentFieldAssembler(),
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
  },
  default() {
    return {
      discriminator: define.discriminator,
      title: '未命名',
      constraints: [],
    }
  }
};

export default define