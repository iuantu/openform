<template>
  <div class="form-input">
    <div class="editor-preview" v-show="formItm.value != ''" v-html="formItm.value"></div>
  </div>
</template>

<script>
export default {
  name: "editor",
  components: {},
  data() {
    return {
    };
  },
  methods: {},
  created() {
  },
  mounted() {
  },
  props: ['formIndex', 'formItm']
};
</script>

<style lang="scss">
@import "./../css/index.scss";
</style>
