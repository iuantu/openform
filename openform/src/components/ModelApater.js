import allFieldMetas from './fields/index'

class AbstractConstraint {
  toRequestModel(viewModel) {
  }

  fromViewModelToAttribute(viewModel, attributeValues) {

  }

  fromAttributeToViewModel(fieldViewModel, attribute, value) {
    let found = null;
    fieldViewModel.constraints.forEach((constraint) => {
      if (constraint.discriminator == attribute) {
        found = constraint;
        return;
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
  toRequestModel(viewModel) {

  }
}

class ConstraintMin extends AbstractConstraint {
  toRequestModel(viewModel) {

  }

  fromAttributeToViewModel(fieldViewModel, attribute, value) {
    const found = super.fromAttributeToViewModel(fieldViewModel, attribute, value);
    found.min = value.min;

    return found;
  }
}

class ConstraintMax extends AbstractConstraint {
  toRequestModel(viewModel) {

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
    console.error(`constraint model adapter [${discriminator}] not found.`);
  }
  return adapter;
}

class FormModelAdapter {
  toRequestModel(viewModel) {
    const requestModel = {
      title: viewModel.title,
      description: viewModel.description,
      fields: viewModel.fields.map((fieldViewModel) => {
        return fieldModelAdapterFactory(fieldViewModel.discriminator).toRequestModel(fieldViewModel);
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
        const discriminator = fieldRequestModel.discriminator.replace('_', '-');
        const fieldViewModel = fieldModelAdapterFactory(discriminator).toViewModel(fieldRequestModel);
        return fieldViewModel;
      }),
    };

    viewModel.fields.sort((a, b) => {
      return a.layout_row_index - b.layout_row_index;
    });

    return viewModel;
  }
}
  
class AbstractConstraintModelAdapter {
  toRequestModel(view) {

  }

  toView(request) {

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
    requestModel.title = viewModel.title;
    requestModel.name = viewModel.name;
    requestModel.description = viewModel.description;
    requestModel.readonly = viewModel.readonly;

    requestModel.constraints = viewModel.constraints;
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
    if (this.attributeNames.indexOf(attribute) > -1) {
      viewModel[attribute] = value;
    }

    if (attribute.endsWith("_constraint")) {
      const constraintAdapter = constraintModelAdapterFactory(attribute);
      const constraint = constraintAdapter.fromAttributeToViewModel(viewModel, attribute, value);

      if (!constraint.id && viewModel.constraints.indexOf(constraint) == -1) {
        viewModel.constraints.push(constraint);
      }
    }
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
    console.log(attributeValues, viewModel);
    debugger;
  
    if (viewModel.constraints) {
      try {
        viewModel.constraints.forEach((constraint) => {
          attributeValues[constraint.discriminator] = constraint;
        })
      } catch (e) {
        // TODO: 不应该出现异常
      }
    } else {
      viewModel.constraints = [];
    }
  
    return attributeValues;
  }
}
  
class TextFieldModelAdapter extends AbstractFieldModelAdapter {
  constructor() {
    super();
    this.textFieldAttributeNames = ['default', 'placeholder'];
  }

  toRequestModel(viewModel) {
    const request = super.toRequestModel(viewModel);
    request.placeholder = viewModel.placeholder;
    request.default = viewModel.default;
    return request;
  }

  toViewModel(requestModel) {
    const viewModel = super.toViewModel(requestModel);
    viewModel.default = requestModel.default;
    viewModel.placeholder = requestModel.placeholder;
    return viewModel;
  }

  fromAttributeToViewModel(viewModel, attribute, value) {
    super.fromAttributeToViewModel(viewModel, attribute, value);
    if (this.textFieldAttributeNames.indexOf(attribute) > -1) {
      viewModel[attribute] = value;
    }
  }
}
  
class SelectFieldModelAdapter extends AbstractFieldModelAdapter {
  toRequestModel(field) {
    const request = super.toRequestModel(field);
    return request;
  }
}
  
const discriminators = {
  'text-field': new TextFieldModelAdapter(),
  'select-field': new SelectFieldModelAdapter()
}

function fieldModelAdapterFactory(discriminator) {
  const adapter = discriminators[discriminator];
  return adapter;
}

export { FormModelAdapter, fieldModelAdapterFactory }