import { FormService } from './../../functions'
import { FormModelAdapter, fieldModelAdapterFactory } from './../ModelApater'

/**
 * 表单设计器视图组件的适配器
 * 
 * 当前开发的表单设计器版本，存在 RouterView和不同的视图组件共享数据的问题创建。
 */
export default class FormEditorController {
  constructor() {
    this.service = new FormService();
    this.formModelAdapter = new FormModelAdapter();
  }

  setFormId(formId) {
    this.formId = formId;
  }

  setForm(form) {
    this.form = form;
  }

  async save() {
    const remote = this.formModelAdapter.toRequestModel(this.form);

    if (this.formId) {
      await this.service.changeForm(this.formId, remote);
    } else {
      this.service.createForm(remote);
    }
  }

  /**
   * 表单编辑器修改事件
   * 
   * 当前仅有描述的属性内容、标题和表单描述会出发通知
   * 
   * @param {*} action 
   * @param {*} value 
   */
  formEditorChange(action, value) {
    if ('titleChange' == action) {
      this.form.title = value;
    } else if ('descriptionChange' == action) {
      this.form.description = value;
    } else if ('fieldChange' == action) {
      this.form.fields.forEach((field) => {
        if (field.viewId == value.viewId) {
          field.description = value.description;
        }
      })
    }
  }

  /**
   * 属性面板中的属性值修改事件
   * 
   * @type {{attributeValues: Object.<string, object>}}
   * @param {*} fieldViewId 
   * @param {attributeValues} attribute 
   * @param {*} value 
   */
  fieldAttributeChange(field, attributeValues, attribute, value) {
    console.log('FormEditorController: field attribute change');
    console.log('field view id is ' + field.viewId);

    // const fieldAttributeName = ['title', 'description', 'name']
    this.form.fields.forEach((fieldIter) => {
      if (fieldIter.viewId == field.viewId) {
        console.log('find: current field view id is ' + fieldIter.viewId);
        const found = fieldIter;
      
        // if (fieldAttributeName.indexOf(attribute.key) > -1) {
        //   found[attribute.key] = value;
        // }

        fieldModelAdapterFactory(field.discriminator).fromAttributeToViewModel(field, attribute.key, value);
      }
    });
  }
}