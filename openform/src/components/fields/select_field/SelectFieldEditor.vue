<template>
  <div class="form-input">
    <!-- <div class="title" :style="{textAlign: formItm.alignType}">
      {{formItm.name}}
      <span class="required" v-show="formItm.isRequired">*</span>
    </div> -->
    <div class="title">
      {{field.title || '未命名'}}
      <!-- <span class="required" v-show="formItm.isRequired || false">*</span> -->
    </div>
    <div class="subtitle">
      {{field.description}}
    </div>
    <div>
      <el-radio-group v-model="field.options" v-if="!field.multiple">
        <el-radio v-for="(option, optionIndex) in field.options" :key="optionIndex" :label="option.label"></el-radio>
      </el-radio-group>
      <el-checkbox-group v-model="field.options" v-if="field.multiple">
        <el-checkbox v-for="(option, optionIndex) in field.options" :key="optionIndex" :label="option.label">
          <!-- <i class="fa fa-times"></i> -->
          <!-- <el-input size="small" v-if="checkItm.isText"></el-input> -->
        </el-checkbox>
      </el-checkbox-group>
      <!-- <div class="require-text" v-show="formItm.isRequired || false">{{formItm.requireText || '校验提示'}}</div> -->
    </div>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      select: []
    };
  },
  methods: {},
  mounted() {},
  props: ['index', 'field']
};
</script>

<style lang="scss">
// @import "./../css/index.scss";
</style>
