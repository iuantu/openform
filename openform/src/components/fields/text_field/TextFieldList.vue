<template>
  <div>{{value}}</div>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: "",
    }
  },
  created() {
    console.log("test")
  }
}
</script>