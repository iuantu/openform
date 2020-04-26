import {ofFetch} from "../functions";

export default class ValueHTTP {
  fetch(page) {

  }

  async add(formId, value) {
    const response = await ofFetch(`/api/v1/form/${formId}/value`, {
      method: 'POST',
      body: JSON.stringify(value)
    });

    return await response.json();
  }
}