<template>
  <field-component :field="field" :index="index">
    <el-upload
        class="upload-demo"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        multiple>
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
        <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb</div>
      </el-upload>
  </field-component>
</template>
<script>
import FieldComponent from '../FieldComponent';

export default {
  props: {
    field: {
      type: Object,
      default() {
        return {
          constraints: {
          }
        }
      }
    },
    index: {
      type: Number
    }
  },
  components: {
    FieldComponent
  }
}
</script>