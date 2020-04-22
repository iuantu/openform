<template>
  <el-dialog
    title="数据"
    :visible.sync="dialogVisible"
    width="80%">
    <form-fields :fields="fields"></form-fields>
    <span slot="footer" class="dialog-footer">
      <el-button v-if="isCreation" size="small" type="primary" @click="onSaveButtonClick">确 定</el-button>
      <el-button v-if="!isCreation" size="small" type="primary" @click="dialogVisible === false">修 改</el-button>
      <el-button v-if="!isCreation" size="small" type="danger" @click="dialogVisible === false">删 除</el-button>
    </span>
  </el-dialog>
</template>
<script>
import FormFields from "./FormFields";
import { FormModelAssembler } from './ModelApater'
import { FormService } from '../functions'
import { getMeta } from "./fields";

export default {
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    form_id: {
      default: 0
    },
    id: {
      default: 0
    }
  },
  data() {
    return {
      dialogVisible: false,
      fields: [],
      form: null,
    };
  },
  async created() {
    this.dialogVisible = this.visible;

    this.formService = new FormService();
    const assembler = new FormModelAssembler();
    this.form = assembler.toViewModel(await this.formService.fetchForm(this.form_id));
    this.fields = this.form.fields;
  },
  components: {
    FormFields
  },
  methods: {
    onEditClick() {

    },
    onDeleteClick() {

    },
    onSaveButtonClick() {
      this.fields.forEach((field) => {
          getMeta(field.discriminator).validate(field);
      });
      this.formService.submit(this.form_id, this.id, this.fields);
    }
  },
  computed: {
    isCreation() {
      return this.id < 1;
    }
  }
}
</script>