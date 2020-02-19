<template>
  <div class="form-input" :style="{width: formItm.width + '%'}">
    <div class="title" :style="{textAlign: formItm.alignType}">
      {{formItm.name || '标题'}}
      <span class="required" v-show="formItm.isRequired || false">*</span>
    </div>
    <div class="subtitle" :style="{textAlign: formItm.alignType}">
      {{formItm.subTitle || '副标题'}}
    </div>
    <div>
      <el-input readonly="" :min="(formItm.min?formItm.min: 0)" size="small" :placeholder="formItm.placeholder" v-model="input" clearable></el-input>
      <div class="require-text" v-show="(formItm.isRequiredText && formItm.isRequired) || false">{{formItm.requireText || '校验提示'}}</div>
    </div>
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
