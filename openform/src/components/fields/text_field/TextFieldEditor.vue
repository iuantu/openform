<template>
  <field-component :field="field" :index="index">
    <el-input size="small" :placeholder="field.placeholder" :disabled="field.readonly"></el-input>
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
  components: {
    FieldComponent
  }
}
</script>