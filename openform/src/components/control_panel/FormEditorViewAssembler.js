import { FormService } from '../../functions';
import { FormModelAdapter } from '../ModelApater'

const formModelAdapter = new FormModelAdapter();

function forView(requestModel) {
  return formModelAdapter.toViewModel(requestModel);
}

export { forView }