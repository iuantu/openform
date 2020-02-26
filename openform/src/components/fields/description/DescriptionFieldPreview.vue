<template>
  <div class="form-input" :style="{width: formItm.width + '%'}">
    <div class="title" :style="{textAlign: formItm.alignType}">
      {{field.title || '描述'}}
      <rich-editor :text="input" @change="onChange"></rich-editor>
    </div>
  </div>
</template>
<script>
import RichEditor from './../../formComponent/components/RichEditor'

export default {
  components: {
    RichEditor,
  },
  props: {
    field: {
      type: Object,
      default() {
        return {
          title: '',
          description: ''
        }
      }
    },
    index: {
      type: Number
    }
  },
  data() {
    return {
      title: "描述",
      input: ""
    };
  },
  methods: {
    onChange(text) {
      this.field.description = text;
    }
  },
  created() {
    this.input = this.field.description;
  },
  mounted() {},
}
</script>