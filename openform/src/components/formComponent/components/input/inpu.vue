<template>
  <div class="form-input">
    <div class="title">
      {{formItm.name || '标题'}}
      <span class="required" v-show="formItm.isRequired || false">*</span>
    </div>
    <el-input :placeholder="formItm.placeholder" v-model="input" clearable></el-input>
  </div>
</template>

<script>
export default {
  name: "input",
  components: {},
  data() {
    return {
      title: "单行输入",
      input: "",
      placeholder: "请输入内容",
      isRequired: false
    };
  },
  methods: {},
  mounted() {},
  props: ['formIndex', 'formItm']
};
</script>

<style lang="scss">
@import "./../css/index.scss";
</style>
