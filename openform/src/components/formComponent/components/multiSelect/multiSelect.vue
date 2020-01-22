<template>
  <div class="form-input">
    <div class="title">
      {{formItm.name}}
      <span class="required" v-show="formItm.isRequired">*</span>
    </div>
    <el-checkbox-group v-model="select">
      <el-checkbox v-for="(checkItm, checkIndex) in formItm.options" :key="checkIndex + '_checkbox'" :label="checkItm.label">
        {{checkItm.value}}
        <i class="fa fa-times"></i>
      </el-checkbox>
    </el-checkbox-group>
  </div>
</template>

<script>
export default {
  name: "select",
  components: {},
  data() {
    return {
      select: []
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
