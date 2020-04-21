<template>
  <field-component :field="field" :index="index">
    <el-input
      class="input"
      size="small"
      v-model="text"
      :placeholder="field.placeholder"
      :disabled="field.readonly">
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
    }
  },
  data() {
    return {
      text: ''
    }
  },
  components: {
    FieldComponent
  }
}
</script>
<style>
  .input {
    width: 50%;
  }
</style>