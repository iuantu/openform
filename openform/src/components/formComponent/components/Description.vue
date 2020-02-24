<template>
  <div class="form-input" :style="{width: formItm.width + '%'}">
    <div class="title" :style="{textAlign: formItm.alignType}">
      {{formItm.title || '描述'}}
      <!-- <el-input readonly="" size="small" :placeholder="formItm.placeholder" v-model="input" clearable></el-input> -->
      <rich-editor :text="input" @change="onChange"></rich-editor>
    </div>
  </div>
</template>
<script>
import RichEditor from './RichEditor'

export default {
  name: "input",
  components: {
    RichEditor,
  },
  data() {
    return {
      title: "描述",
      input: "123"
    };
  },
  methods: {
    onChange(text) {
      this.formItm.description = text;
    }
  },
  created() {
    console.log(this.formItm.description)
    this.input = this.formItm.description;
  },
  mounted() {},
  props: ['formIndex', 'formItm']
}
</script>