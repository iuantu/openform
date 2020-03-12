import allFieldMetas, { getMeta } from './fields/index'

class AbstractConstraint {
  toRequestModel(viewModel) {
    const requestModel = {
      id: viewModel.id,
      enabled: viewModel.enabled
    };

    if (!viewModel.id) {
      requestModel.discriminator = viewModel.discriminator;
    }

    return requestModel;
  }

  fromViewModelToAttribute(/*viewModel, attributeValues*/) {

  }

  fromAttributeToViewModel(fieldViewModel, attribute, value) {
    let found = null;
    fieldViewModel.constraints.forEach((constraint) => {
      if (constraint.discriminator === attribute) {
        found = constraint;
      }
    });

    if (!found) {
      found = JSON.parse(JSON.stringify(value));
      found.discriminator = attribute;
    }
    found.enabled = value.enabled;

    return found;
  }
}

class ConstraintRequired extends AbstractConstraint {
}

class ConstraintMin extends AbstractConstraint {
  toRequestModel(viewModel) {
    const requestModel = super.toRequestModel(viewModel);
    requestModel.min = viewModel.min;
    return requestModel;
  }

  fromAttributeToViewModel(fieldViewModel, attribute, value) {
    const found = super.fromAttributeToViewModel(fieldViewModel, attribute, value);
    found.min = value.min;

    return found;
  }
}

class ConstraintMax extends AbstractConstraint {
  toRequestModel(viewModel) {
    const requestModel = super.toRequestModel(viewModel);
    requestModel.max = viewModel.max;
    return requestModel;
  }

  fromAttributeToViewModel(fieldViewModel, attribute, value) {
    const found = super.fromAttributeToViewModel(fieldViewModel, attribute, value);
    found.max = value.max;

    return found;
  }
}

const constraintDiscriminators = {
  'required_constraint': new ConstraintRequired(),
  'min_constraint': new ConstraintMin(),
  'max_constraint': new ConstraintMax(),
}

function constraintModelAdapterFactory(discriminator) {
  const adapter = constraintDiscriminators[discriminator];
  if (!adapter) {
    throw new Error(`constraint model adapter [${discriminator}] not found.`);
  }
  return adapter;
}

class FormModelAdapter {

  constructor() {
    this.fieldModelAdapter = new AbstractFieldModelAdapter();
  }

  toRequestModel(viewModel) {
    const requestModel = {
      title: viewModel.title,
      description: viewModel.description,
      fields: viewModel.fields.map((fieldViewModel) => {

        const fieldRequestModel = this.fieldModelAdapter.toRequestModel(fieldViewModel);
        const fieldMeta = this.getMeta(fieldViewModel.discriminator);
        fieldMeta.viewModelToRequestModel(fieldViewModel, fieldRequestModel);
        return fieldRequestModel;
      })
    }
    if (viewModel.id) {
      requestModel.id = viewModel.id;
    }

    for (let i = 0, size = requestModel.fields.length; i < size; i++) {
      const field = requestModel.fields[i];
      field.layout_row_index = i;
    }

    return requestModel;
  }

  toViewModel(requestModel) {
    const viewModel = {
      id: requestModel.id,
      title: requestModel.title,
      description: requestModel.description,
      fields: requestModel.fields.map((fieldRequestModel) => {
        const viewModel = this.fieldModelAdapter.toViewModel(fieldRequestModel);
        const fieldMeta = this.getMeta(fieldRequestModel.discriminator);
        fieldMeta.requestModelToViewModel(fieldRequestModel, viewModel);
        return viewModel;
      }),
    };

    viewModel.fields.sort((a, b) => {
      return a.layout_row_index - b.layout_row_index;
    });

    return viewModel;
  }

  getMeta(discriminator) {
    return allFieldMetas[discriminator.replace("_", "-")];
  }
}


/**
 * 模型适配器
 */
class AbstractFieldModelAdapter {
  constructor() {
    this.attributeNames = ['title', 'name', 'description', 'readonly', 'error_message', 'error_message_enabled']
  }

  toRequestModel(viewModel) {
    const requestModel = {}
    if (viewModel.id) {
      requestModel.id = viewModel.id;
    } else {
      requestModel.discriminator = viewModel.discriminator.replace('-', '_');
    }

    this.attributeNames.forEach((attr) => {
      requestModel[attr] = viewModel[attr];
    });

    requestModel.constraints = viewModel.constraints.map((constraint) => {
      const assembler = constraintModelAdapterFactory(constraint.discriminator);
      return assembler.toRequestModel(constraint);
    });

    return requestModel;
  }

  toViewModel(requestModel) {
    const viewId = Math.random();
    requestModel.viewId = viewId;
    if (!requestModel.constraints) {
      requestModel.constraints = [];
    }

    return {
      id: requestModel.id,
      viewId,
      discriminator: requestModel.discriminator.replace("_", "-"),
      title: requestModel.title,
      description: requestModel.description,
      error_message: requestModel.error_message,
      error_message_enabled: requestModel.error_message_enabled,
      constraints: requestModel.constraints.map((constraint) => {
        // TODO: 重新构造对象
        const viewModel = JSON.parse(JSON.stringify(constraint));
        delete viewModel['created_at'];
        delete viewModel['updated_at'];
        delete viewModel['field_id'];
        return viewModel;
      }),
      layout_row_index: requestModel.layout_row_index
    }
  }

  fromAttributeToViewModel(viewModel, attribute, value) {

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

    getMeta(viewModel.discriminator).attribtueModelToViewModel(viewModel, attribute, value);
  }

  /**
   *
   * @param {*} viewModel 字段视图模型
   * @returns 属性值视图模型
   */
  fromViewModelToAttribute(viewModel) {
    const meta = allFieldMetas[viewModel.discriminator];

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

    meta.viewModelToAttributeModel(viewModel, attributeValues);

    return attributeValues;
  }
}

export { FormModelAdapter, AbstractFieldModelAdapter }
