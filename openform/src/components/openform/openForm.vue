<template>
  <div class="open-form-setting">
    <el-container>
      <div class="inner-content">
        <div class="add-new">
          <el-button type="primary" size="small" @click="save">保存</el-button>
        </div>
        <el-tabs type="card" v-model="activeName" @tab-click="onTabClick">
          <el-tab-pane v-for="(option, key) in options" :key="key" :label="option.label" :name="option.name" :disabled="isCreate"></el-tab-pane>
        </el-tabs>
        <el-row type="flex">
          <el-col>
            <router-view
              :form="form"
              :fields="fields"
              @field-component-active="onFieldComponentActive"
              @change="onFormEditorChange"
              @fields-change='onFieldsChange'>

            </router-view>
          </el-col>
        </el-row>
      </div>
      <el-aside v-show="showRightAside" width="265px" class="openForm-side right">
        <field-attribute-panel :field="currentField" @input="onFieldAttributePanelChange"></field-attribute-panel>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import { SecurityService, FormService } from '../../functions';
import FieldAttributePanel from '../../components/cp/form/field/FieldAttributePanel'
import allFieldMetas from '../../components/fields/index';
import FormEditorController from './view'
import { forView } from './../control_panel/FormEditorViewAssembler'

export default {
  name: "clone",
  inject: ["reload", "leftAside", "hideLeftAside"],
  components: {
    // 'right-aside': RightAside,
    FieldAttributePanel,
  },

  data() {
    return {
      list: [],
      showRightAside: true,

      id: 0,
      activeName: 'first',
      editIndex: null,
      isCreate: true,

      currentField: {},
      form: {},
      fields: {},

      options: [
        {
          label: '概述',
          name: 'cp_form_summary'
        },
        {
          label: '编辑',
          name: 'cp_form_editor'
        },
        {
          label: '数据',
          name: 'cp_form_data',
        },
        {
          label: '报表',
          name: 'cp_form_reporter',
        },
        {
          label: '发布',
          name: 'cp_form_publish',
        }
      ]
    };
  },
  methods: {

    async save() {
      await this.controller.save();
      await this.created();
    },
    onTabClick(tab){
      this.$router.replace({name: tab.name});
    },
    onFieldComponentActive(field) {
      this.currentField = field;

      // 配置 AttributePanel 的Props
    },
    onFieldAttributePanelChange(attributeValues, attribute, value) {
      
      this.controller.fieldAttributeChange(this.currentField, attributeValues, attribute, value);
    },
    onFormEditorChange(action, value) {
      this.controller.formEditorChange(action, value);
    },
    onFieldsChange(fields) {
      // this.controller.setEditorFields(fields);
    }
  },
  async created() {
    this.id = this.$route.params.id
    if (this.id) {
      this.isCreate = false;
    }

    const formService = new FormService();
    this.form = forView(await formService.fetchForm(this.id));
    this.fields = this.form.fields;
    this.controller = new FormEditorController();
    this.controller.setFormId(this.id);
    this.controller.setForm(this.form);
  },

  computed: {
    formId() {
      return new Number(this.$route.params.id);
    }
  },

  provide() {
    return {
      setForm(form) {
        this.form = form;
        this.controller.setForm(form)
      }
    }
  },
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
