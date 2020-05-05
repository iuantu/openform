<template>
  <el-dialog
    title="数据"
    @close="$emit('close')"
    :visible.sync="dialogVisible"
    width="80%">
    <row v-if="isDetailMode" :fields="theForm && theForm.fields" :row="row"></row>
    <form-fields v-if="!isDetailMode" :fields="theForm && theForm.fields"></form-fields>
    <span slot="footer" class="dialog-footer">
      <el-button v-if="!isDetailMode" size="small" type="primary" @click="onSaveButtonClick">确 定</el-button>
      <el-button v-if="isDetailMode" size="small" type="primary" @click="onEditButtonClick">修 改</el-button>
      <el-button v-if="isDetailMode" size="small" type="danger" @click="dialogVisible === false">删 除</el-button>
    </span>
  </el-dialog>
</template>
<script>
import FormFields from "../../../FormFields";
import Row from "./Row";

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
      type: Boolean,
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
      isDetailMode: false,
    };
  },
  async created() {
    this.dialogVisible = this.visible;
    this.isDetailMode = this.isDetail;
    // console.log("isDetail", this.isDetail);
  },
  components: {
    FormFields,
    Row
  },
  methods: {
    onEditButtonClick() {
      this.isDetailMode = false;
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
    },
    isDetail(mode) {
      this.isDetailMode = mode;
      console.log("isDetail", mode);
    }
  }
}
</script>