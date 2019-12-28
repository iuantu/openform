<template>
  <div class="form-input">
    <div class="title">
      {{title}}
      <span class="required" v-show="isRequired">*</span>
    </div>
    <el-select multiple v-model="select" clearable :placeholder="placeholder">
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
      title: "多选",
      select: [],
      placeholder: "请输入内容",
      isRequired: true,
      options: [
        {
          label: "1234234234",
          value: "1"
        },
        {
          label: "22342342erfwer",
          value: "2"
        },
        {
          label: "323423rawsef",
          value: "3"
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
