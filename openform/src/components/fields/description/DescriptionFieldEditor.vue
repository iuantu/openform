<template>
  <div class="form-input">
    <div class="title">
      {{field.title || '描述'}}
      <rich-editor :text="input" @change="onChange"></rich-editor>
    </div>
  </div>
</template>
<script>
import RichEditor from '../../cp/form/RichEditor'

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
      this.$emit('change', this.field);
    }
  },
  created() {
    this.input = this.field.description;
  },
}
</script>