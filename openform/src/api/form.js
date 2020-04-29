import {ofFetch} from "../functions";

export default class FormHTTP {
  async fetchOne(formId) {
    const response = await ofFetch(`/api/v1/form/${formId}`);
    return await response.json();
  }
}