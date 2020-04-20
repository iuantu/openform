<template>
  <el-dialog
    title="数据"
    :visible.sync="dialogVisible"
    width="80%">
    <form-fields :fields="fields"></form-fields>
    <span slot="footer" class="dialog-footer">
      <el-button size="small" type="primary" @click="dialogVisible === false">修 改</el-button>
      <el-button size="small" type="danger" @click="dialogVisible === false">删 除</el-button>
    </span>
  </el-dialog>
</template>
<script>
import FormFields from "./FormFields";

export default {
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    id: {
    }
  },
  data() {
    return {
      dialogVisible: false,
      fields: [],
    };
  },
  created() {
    this.dialogVisible = this.visible;
    console.log("created");
  },
  components: {
    FormFields
  },
  methods: {
    onEditClick() {

    },
    onDeleteClick() {

    }
  }
}
</script>