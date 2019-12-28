<template>
  <div class="form-input">
    <div class="title">
      {{title}}
      <span class="required" v-show="isRequired">*</span>
    </div>
    <el-input type="textarea" :placeholder="placeholder" v-model="input" clearable></el-input>
  </div>
</template>

<script>
export default {
  name: "input",
  components: {},
  data() {
    return {
      title: "多行输入",
      input: "",
      placeholder: "请输入内容",
      isRequired: true
    };
  },
  methods: {},
  mounted() {},
  props: ['formIndex']
};
</script>

<style lang="scss">
@import "./../css/index.scss";
</style>
