<template>
  <div class="open-form-setting">
    <el-container>
      <div class="inner-content">
        <div class="add-new">
          <el-button
            type="primary"
            size="small"
            @click="onSaveClick"
            :loading="saving"
            v-show="isEditor"
          >保存
          </el-button>
        </div>
        <el-tabs type="card" v-model="activeName" @tab-click="onTabClick">
          <el-tab-pane 
            v-for="(option, key) in options"
            :key="key"
            :label="option.label"
            :name="option.name"
            :disabled="isCreate"
          >
          </el-tab-pane>
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
      <el-aside v-show="isEditor" width="265px" class="openForm-side right">
        <field-attribute-panel
          :meta="meta"
          :field="currentField"
          :attributes="attributes"
          :attributeValues="attributeValues"
          @input="onAttributeValuelsChange">
        </field-attribute-panel>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import { FormService } from '../../functions';
import FieldAttributePanel from '../../components/cp/form/field/FieldAttributePanel'
import { getMeta } from '../../components/fields/index';
import { FormModelAssembler } from './../ModelApater';

export default {

  inject: ["hideFieldPanel",],
  components: {
    FieldAttributePanel,
  },

  data() {
    return {
      list: [],
      showFieldAttributePanel: true,

      id: 0,
      activeName: 'cp_form_editor_edit',
      editIndex: null,
      isCreate: true,

      currentField: {},

      meta: {},
      attributes: {},
      attributeValues: {},

      form: {},
      fields: {},
      saving: false,
      isEditor: false,

      options: [
        {
          label: '概述',
          name: 'cp_form_summary'
        },
        {
          label: '编辑',
          name: 'cp_form_editor_edit'
        },
        {
          label: '预览',
          name: 'cp_form_preview',
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

    async onSaveClick() {
      this.saving = true;
      
      const remote = this.formModelAssembler.toRequestModel(this.form);

      try {
        if (this.id) {
          await this.service.changeForm(this.id, remote);
        } else {
          const form = await this.service.createForm(remote);
          this.$router.push({
            name: 'cp_form_editor_edit',
            params: {
              id: form.id
            }
          });
          this.isCreate = false;
          this.id = form.id;
        }
      } catch(e) {
        this.$message(e);
      } finally {
        this.saving = false;
      }
    },

    onTabClick(tab){
      if (tab.name == this.$route.name) {
        return;
      }

      if (tab.name.indexOf('cp_form_editor') > -1) {
        this.hideFieldPanel(false);
      }
      
      this.$router.replace({name: tab.name, id: this.$route.params.id,});
      
      this.showOrHiddenSaveButton(tab.name);
    },

    onFieldComponentActive(field) {
      this.currentField = field;

      const meta = getMeta(field.discriminator);
      const values = meta.assembler.fromViewModelToAttribute(field);

      this.attributes = meta.attributes;
      this.attributeValues = values;
      this.meta = meta;
    },

    onAttributeValuelsChange(attributeValues, attribute, value) {
      const field = this.currentField;
      const meta = getMeta(field.discriminator);
      meta.assembler.fromAttribtueModelToViewModel(field, attribute.key, value);
    },

    onFormEditorChange(action, value) {
      if ('titleChange' == action) {
        this.form.title = value;
      } else if ('descriptionChange' == action) {
        this.form.description = value;
      } else if ('fieldChange' == action) {
        this.form.fields.forEach((field) => {
          if (field.viewId == value.viewId) {
            field.description = value.description;
          }
        });
      }
    },

    onFieldsChange(/*fields*/) {
    },

    getIsEditor() {
      const routers = ['cp_form_editor_edit', 'cp_form_editor'];
      for (const router of routers) {
        if (this.$route.name == router) {
          return true;
        }
      }
      return false;
    },

    showOrHiddenSaveButton(tabName) {
      this.isEditor = this.getIsEditor();
      this.showFieldAttributePanel = tabName == "cp_form_editor_edit";
      this.hideFieldPanel(!this.isEditor);
    },
  },

  async created() {
    this.id = this.$route.params.id
    this.activeName = this.$route.name;
    this.showOrHiddenSaveButton('');

    if (this.id) {
      this.isCreate = false;
    }
    this.formModelAssembler = new FormModelAssembler();
    this.service = new FormService();

    if (!this.isCreate) {
      this.form = this.formModelAssembler.toViewModel(
        await this.service.fetchForm(this.id)
      );
    } else {
      this.form = this.formModelAssembler.toViewModel({
        title: "未命名表单",
        description: "未命名表单的描述",
        fields: [],
      });
    }
    this.fields = this.form.fields;
  },

  mounted() {
    this.hideFieldPanel(false);
  },

  computed: {
    formId() {
      return new Number(this.$route.params.id);
    },
  },

  provide() {
    return {
      setForm(form) {
        this.form = form;
      }
    }
  },
};
</script>

<style lang="scss">
@import "./TheForm.scss";
</style>
