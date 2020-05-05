<template>
  <field-component :field="field" :index="index">
    <el-input
      class="input"
      v-bind:class="{ error: field.has_error }"
      size="small"
      v-model="text"
      :placeholder="field.placeholder"
      :disabled="field.readonly"
      @change="onInputChange">
    </el-input>
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
          title: '',
          readonly: false,
          description: '',
          placeholder: '',
          constraints: {
          }
        }
      }
    },
    index: {
      type: Number
    },
  },
  data() {
    return {
      text: ''
    }
  },
  components: {
    FieldComponent
  },
  methods: {
    onInputChange(text) {
      this.field.value = text;
      this.$emit("change", text);
    }
  },
  created() {
    this.text = this.field.value;
  }
}
</script>
<style>
  .input {
    width: 50%;
  }
  .error {

  }
</style>