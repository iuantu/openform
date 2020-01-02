<template>
  <div class="open-form">
    <el-container>
      <el-container>
        <el-aside v-show="showLeftAside" width="200px" class="openForm-side left">
          <left-aside></left-aside>
        </el-aside>
        <el-main>
          <router-view v-if="reloadPage"></router-view>
        </el-main>
        <el-aside v-show="showRightAside" width="200px" class="openForm-side right">
          <right-aside></right-aside>
        </el-aside>
      </el-container>
    </el-container>
  </div>
</template>

<script>

import LeftAside from './../../components/leftAside/leftAside'
import RightAside from './../../components/rightAside/rightAside'

export default {
  name: "openFormSetting",
  components: {
    'left-aside': LeftAside,
    'right-aside': RightAside,
  },
  data() {
    return {
      showLeftAside: true,
      reloadPage: true,
      showRightAside: true,
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
      this.showLeftAside = !this.showLeftAside
    },
    // 显示/隐藏右侧栏
    showRA(){
      this.showRightAside = !this.showRightAside
    },
  },
  mounted() {},
  provide() {
    return {
      reload: this.reload,
      leftAside: this.showLA,
      rightAside: this.showRA,
    };
  },
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
