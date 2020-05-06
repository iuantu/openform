<template>
  <div>
    <div v-if="field && field.multiple">
      <li
        v-for="(v, index) in displayValue"
        v-key="index"
      >{{v}}</li>
    </div>
    <div v-if="field && !field.multiple">{{displayValue[0]}}</div>
  </div>
</template>

<script>
export default {
  props: {
    field: {
      type: Object
    },
    value: {
      type: Array
    }
  },
  computed: {
    displayValue() {
      if (null == this.value) {
        return [];
      }
      return this.value.map((v) => {
        if (v.text.length > 0) {
          return v.text;
        } else {
          for (const opt of this.field.options) {
            if (opt.value === v.value) {
              return opt.label;
            }
          }
        }
      })
    }
  }
}
</script>
