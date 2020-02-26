<template>
  <div class="open-form">
    <el-container>
      <el-aside width="265px" class="openForm-side left">
        <left-aside v-show="showLeftAside" ></left-aside>
      </el-aside>
      <el-main>
        <open-form></open-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>

import LeftAside from './../../components/leftAside/leftAside'
import OpenForm from './../../components/openform/openForm'

export default {
  name: "openFormSetting",
  components: {
    'left-aside': LeftAside,
    OpenForm,
  },
  data() {
    return {
      showLeftAside: true,
      reloadPage: true,
      // showRightAside: true,
    };
  },
  methods: {
    // 全页面刷新
    reload(){
      this.reloadPage = false
      this.$nextTick(()=>{
        this.reloadPage = true
      })
    },
    // 显示/隐藏左侧栏
    showLA(){
      this.showLeftAside = true
    },
    hideLA(){
      this.showLeftAside = true
    }
  },
  mounted() {},
  provide() {
    return {
      reload: this.reload,
      leftAside: this.showLA,
      hideLeftAside: this.hideLA
    };
  },
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
