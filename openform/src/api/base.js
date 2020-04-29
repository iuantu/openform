import {ofFetch} from "../functions";

/**
 * @class
 */
class FieldError {
  /**
   * @type {string}
   */
  name;

  /**
   * @type {string}
   */
  code;



  constructor(name, code, description) {
    this.name = name;
    this.code = code;
    this.description = description;
  }
}

class InvalidFormException extends Error {
  /**
   * @type {Array.<FieldError>}
   */
  errors;

  constructor(errors) {
    super();
    this.errors = errors;
  }

  static fromJson(json) {
    return new InvalidFormException(json.errors.map(
      (error) => new FieldError(error.name, error.code, error.description))
    );
  }
}

export default class BaseHTTP {
  async request(path, options) {
    const response = await ofFetch(path, options);
    const json = await response.json();
    if (299 < response.status) {
      throw InvalidFormException.fromJson(json);
    }
    return json;
  }

}