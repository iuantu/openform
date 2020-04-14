<template>
  <div class="form-input" :style="{width: formItm.width + '%'}">
    <div class="title" :style="{textAlign: formItm.alignType}">
      {{formItm.title || '描述'}}
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
      input: ""
    };
  },
  methods: {
    onChange(text) {
      this.formItm.description = text;
    }
  },
  created() {
    this.input = this.formItm.description;
  },
  mounted() {},
  props: ['formIndex', 'formItm']
}
</script>