<template>
  <div class="form-input">
    <div class="title">
      {{formItm.name}}
      <span class="required" v-show="formItm.isRequired">*</span>
    </div>
    <el-radio-group v-model="select">
      <el-radio v-for="(radioItm, radioIndex) in formItm.options" :key="radioIndex + '_radio'" :label="radioItm.label">
        {{radioItm.value}}
        <i class="fa fa-times"></i>
      </el-radio>
    </el-radio-group>
    
  </div>
</template>

<script>
export default {
  name: "select",
  components: {},
  data() {
    return {
      select: null,
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
