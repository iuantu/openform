<template>
  <span>{{value}}</span>
</template>
<script>
export default {
  props: {

    field: Object,
    value: {
      type: String,
      default: ""
    },
  }
}
</script>