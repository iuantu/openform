
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

  export { constraintModelAdapterFactory }