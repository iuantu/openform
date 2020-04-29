import {ofFetch} from "../functions";
import BaseHTTP from "./base";

export default class ValueHTTP extends BaseHTTP{
  async fetch(formId, page) {
    const response = await ofFetch(`/api/v1/cp/form/${formId}/value?page=${page}`);
    return await response.json();
  }

  async add(formId, value) {
    return await this.request(`/api/v1/form/${formId}/value`, {
      method: 'POST',
      body: JSON.stringify(value)
    });
  }
}