import { constraintModelAdapterFactory } from './constraints'
import { getMeta } from './index'

class AbstractFieldAssembler {
  constructor() {
    this.attributeNames = [
      'title',
      'name',
      'description',
      'readonly',
      'error_message',
      'error_message_enabled',
      'layout_row_index'
    ]
  }

  copyValues(object) {
    const copy = {}
    for (const name of this.attributeNames) {
      copy[name] = object[name]
    }
    return copy;
  }

  fromViewModelToRequestModel(viewModel) {
    const requestModel = {
      ...this.copyValues(viewModel)
    }
    if (viewModel.id) {
      requestModel.id = viewModel.id;
    } else {
      requestModel.discriminator = viewModel.discriminator.replace('-', '_');
    }

    requestModel.constraints = viewModel.constraints.map((constraint) => {
      const assembler = constraintModelAdapterFactory(constraint.discriminator);
      return assembler.toRequestModel(constraint);
    });

    return requestModel;
  }

  fromRequestModelToViewModel(requestModel) {
    const viewId = Math.random();
    requestModel.viewId = viewId;
    if (!requestModel.constraints) {
      requestModel.constraints = [];
    }

    const viewModel = {
      id: requestModel.id,
      viewId,
      discriminator: requestModel.discriminator.replace("_", "-"),
      ...this.copyValues(requestModel),
      constraints: requestModel.constraints.map((constraint) => {
        // TODO: 重新构造对象
        const viewModel = JSON.parse(JSON.stringify(constraint));
        delete viewModel['created_at'];
        delete viewModel['updated_at'];
        delete viewModel['field_id'];
        return viewModel;
      }),
      // layout_row_index: requestModel.layout_row_index
    }
    return viewModel;
  }

  fromAttributeModelToViewModel(viewModel, attribute, value) {

    if (attribute === 'error_message') {
      viewModel.error_message = value['error_message'];
      viewModel.error_message_enabled = value.error_message_enabled;
      return;
    }

    if (this.attributeNames.indexOf(attribute) > -1) {
      viewModel[attribute] = value;
    }

    if (attribute.endsWith("_constraint")) {
      const constraintAdapter = constraintModelAdapterFactory(attribute);
      const constraint = constraintAdapter.fromAttributeToViewModel(viewModel, attribute, value);

      const constraintDoesNotExists = !constraint.id && viewModel.constraints.indexOf(constraint) === -1;
      if (constraintDoesNotExists) {
        viewModel.constraints.push(constraint);
      }
    }
  }

  fromViewModelToAttribute(viewModel) {
    const meta = getMeta(viewModel.discriminator);

    const attributeNameList = meta.attributes.basic.map((fieldAttribute) => {
      return fieldAttribute.key;
    });

    const attributeValues = {}
    attributeNameList.forEach((name) => {
      attributeValues[name] = viewModel[name];
    });

    attributeValues['error_message'] = {
      error_message: viewModel.error_message,
      error_message_enabled: viewModel.error_message_enabled,
    };

    if (!viewModel.constraints) {
      viewModel.constraints = [];
    }

    viewModel.constraints.forEach((constraint) => {
      attributeValues[constraint.discriminator] = constraint;
    });

    return attributeValues;
  }
}

export default AbstractFieldAssembler;