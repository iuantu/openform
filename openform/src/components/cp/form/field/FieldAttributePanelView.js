import { fieldModelAdapterFactory } from './../../../ModelApater'

/**
 * 字段对象转换为字段的属性对象
 *
 * @param {*} field 
 * @param {*} meta 
 */
export function view(field, meta) {
  const adapter = fieldModelAdapterFactory(field.discriminator);
  return adapter.fromViewModelToAttribute(field);
}

// AttributeValue对象转换成 Field 视图对象 
export function remote(field, attributes) {
  const fieldConstraintMap = {}
  // field.constraints.forEach((constraint) => {

  // })
}