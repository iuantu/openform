<template>
  <div id="app">
    <router-view></router-view>
    <!-- <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside v-show="showLeftAside" width="200px" class="openForm-side left">
          <left-aside></left-aside>
        </el-aside>
        <el-main>
          <el-menu :default-active="activeIndex" class="nav" mode="horizontal" @select="onSelect">
            <el-menu-item index="1">表单</el-menu-item>
            <el-menu-item index="2">
              <img src="" />
            </el-menu-item>
          </el-menu>
          <el-row type="flex" justify="center">
            <el-col :md="18"><router-view v-if="reloadPage"></router-view></el-col>
          </el-row>
        </el-main>
        <el-aside v-show="showRightAside" width="200px" class="openForm-side right">
          <right-aside></right-aside>
        </el-aside>
      </el-container>
    </el-container> -->

  </div>
</template>
<style scoped>
  .nav {
    margin-bottom: 50px;
  }
</style>

<script>
import LeftAside from './components/leftAside/leftAside'
import RightAside from './components/rightAside/rightAside'
export default {
  name: 'App',
  data(){
    return {
      showLeftAside: true,
      reloadPage: true,
      showRightAside: true,
      activeIndex: '1'
    }
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

    onSelect(/*idx*/) {

    }
  },
  components: {
    'left-aside': LeftAside,
    'right-aside': RightAside,
  },
  provide() {
    return {
      reload: this.reload,
      leftAside: this.showLA,
      rightAside: this.showRA,
    };
  },
}
</script>

<style lang="scss">
  @import "./assets/css/index.scss";
</style>
