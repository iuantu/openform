import { getMeta } from './fields/index'

class FormModelAssembler {

  toRequestModel(viewModel) {
    const requestModel = {
      title: viewModel.title,
      description: viewModel.description,
      fields: viewModel.fields.map((fieldViewModel) => {
        return getMeta(fieldViewModel.discriminator)
          .assembler
          .fromViewModelToRequestModel(fieldViewModel);
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
        return getMeta(fieldRequestModel.discriminator)
          .assembler
          .fromRequestModelToViewModel(fieldRequestModel);
      }),
    };

    viewModel.fields.sort((a, b) => {
      return a.layout_row_index - b.layout_row_index;
    });

    return viewModel;
  }
}

export { FormModelAssembler }
