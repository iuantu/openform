<template>
  <field-component :field="field" :index="index">

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
          description: ''
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