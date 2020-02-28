<template>
  <div class="form-input" :style="{width: formItm.width + '%'}">
    <!-- <div class="title" :style="{textAlign: formItm.alignType}">
      {{formItm.name}}
      <span class="required" v-show="formItm.isRequired">*</span>
    </div> -->
    <div class="title">
      {{field.title || '标题'}}
      <span class="required" v-show="formItm.isRequired || false">*</span>
    </div>
    <div class="subtitle">
      {{field.description}}
    </div>
    <div>
      <el-checkbox-group v-model="select">
        <el-checkbox v-for="(checkItm, checkIndex) in formItm.options" :key="checkIndex + '_checkbox'" :label="checkItm.label">
          {{checkItm.value}}
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
@import "./../css/index.scss";
</style>
