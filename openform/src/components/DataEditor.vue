<template>
  <el-dialog
    title="数据"
    :visible.sync="visible"
    width="80%">

    <span slot="footer" class="dialog-footer">
      <el-button size="small" type="primary" @click="visible = false">修 改</el-button>
      <el-button size="small" type="danger" @click="visible = false">删 除</el-button>
    </span>
  </el-dialog>
</template>
<script>
  export default {
    props: {
      visible: {
        type: Boolean,
        default: false
      }
    }
  }
</script>