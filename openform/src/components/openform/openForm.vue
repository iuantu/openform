<template>
  <div class="open-form-setting">
    <el-button type="primary" @click="leftAside">左侧</el-button>
    <el-button type="primary" @click="rightAside">右侧</el-button>
    <div class="form-title">{{title}}</div>
    <div class="form-sub-title">{{subtitle}}</div>
    <draggable
      class="dragArea list-group"
      :list="list"
      group="people"
      ghost-class="ghost"
    >
      <div class="list-group-item" v-for="(formItm, formIndex) in list" :key="formIndex + '_form'">
        <form-components :formType="formItm.type" :formIndex="formIndex"></form-components>
        <div class="components-setting-btn">
          <el-button type="primary">设置</el-button>  
          <el-button type="danger">删除</el-button>
        </div>
      </div>
    </draggable>
  </div>
</template>

<script>
import draggable from "vuedraggable";

import formComponents from "./../../components/formComponent/formComponet";

export default {
  name: "clone",
  inject: ["reload", "leftAside", "rightAside"],
  components: {
    draggable,
    "form-components": formComponents
  },
  data() {
    return {
      title: '标题',
      subtitle: '副标题',
      list: []
    };
  },
  methods: {
  },
  mounted() {}
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
