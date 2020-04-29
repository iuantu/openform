<template>
  <el-dialog
    title="数据"
    @close="$emit('close')"
    :visible.sync="dialogVisible"
    width="80%">
    <form-fields v-if="!isDetail" :fields="theForm && theForm.fields"></form-fields>
    <span slot="footer" class="dialog-footer">
      <el-button v-if="!isDetail" size="small" type="primary" @click="onSaveButtonClick">确 定</el-button>
      <el-button v-if="isDetail" size="small" type="primary" @click="dialogVisible === false">修 改</el-button>
      <el-button v-if="isDetail" size="small" type="danger" @click="dialogVisible === false">删 除</el-button>
    </span>
  </el-dialog>
</template>
<script>
import FormFields from "../../../FormFields";

export default {
  props: {
    form: {
      type: Object,
    },
    visible: {
      type: Boolean,
      default: false
    },
    id: {
      default: 0
    },
    row: {
      type: Object
    },
    isDetail: {
      type: boolean,
      default() {
        return true;
      }
    },
  },
  data() {
    return {
      dialogVisible: false,
      theForm: {},
      isEdition: false,
    };
  },
  async created() {
    this.dialogVisible = this.visible;
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
      const fields = this.form.fields;
      this.$emit('submit', { formId: this.form.id, fields });
    }
  },
  computed: {
  },
  watch: {
    visible(value) {
      this.dialogVisible = value;
    },
    form(form) {
      this.theForm = form;
    }
  }
}
</script>