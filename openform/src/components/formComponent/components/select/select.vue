<template>
  <div class="form-input">
    <div class="title">
      {{title}}
      <span class="required" v-show="isRequired">*</span>
    </div>
    <el-select v-model="select" clearable :placeholder="placeholder">
      <el-option
        v-for="(selectItem, selectIndex) in options"
        :key="selectIndex + '_select'"
        :label="selectItem.label"
        :value="selectItem.value"
      ></el-option>
    </el-select>
  </div>
</template>

<script>
export default {
  name: "select",
  components: {},
  data() {
    return {
      title: "单选",
      select: "",
      placeholder: "请输入内容",
      isRequired: true,
      options: [
        {
          label: "123",
          value: "123"
        },
        {
          label: "123",
          value: "123"
        },
        {
          label: "123",
          value: "123"
        }
      ]
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
