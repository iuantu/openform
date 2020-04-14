import DescriptionFieldEditor from './DescriptionFieldEditor'
import DescriptionFieldPreview from './DescriptionFieldPreview'
import * as attrs from '../../cp/form/field/attributes'
import AbstractFieldAssembler from '../AbstractFieldAssembler'

class DescriptionFieldAssembler extends AbstractFieldAssembler {
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
    super.fromAttribtueModelToViewModel(viewModel, attribute, value);
  }
}

const define = {
  name: '描述',
  discriminator: 'description-field',
  category: 'basic',
  editor: DescriptionFieldEditor,
  component: DescriptionFieldPreview,
  assembler: new DescriptionFieldAssembler(),
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