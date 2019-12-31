<template>
  <div id="app">
<<<<<<< HEAD
    <!-- <router-view></router-view> -->
    <el-container>
      <el-header>Header</el-header>
      <el-container>
        <el-aside v-show="showLeftAside" width="200px" class="openForm-side left">
          <left-aside></left-aside>
        </el-aside>
        <el-main>
          <router-view v-if="reloadPage"/>
        </el-main>
        <el-aside v-show="showRightAside" width="200px" class="openForm-side right">
          <right-aside></right-aside>
        </el-aside>
      </el-container>
    </el-container>
=======
    <el-menu :default-active="activeIndex" class="nav" mode="horizontal" @select="onSelect">
      <el-menu-item index="1">表单</el-menu-item>
      <el-menu-item index="2">
        <img src="" />
      </el-menu-item>
    </el-menu>
    <el-row type="flex" justify="center">
      <el-col :md="18"><router-view></router-view></el-col>
    </el-row>
>>>>>>> c02c810230ec8f0d9fafcea9cbad71c0a49b6c60
  </div>
</template>
<style scoped>
  .nav {
    margin-bottom: 50px;
  }
</style>

<script>
<<<<<<< HEAD
import LeftAside from './components/leftAside/leftAside'
import RightAside from './components/rightAside/rightAside'
export default {
  name: 'App',
  data(){
    return {
      showLeftAside: true,
      reloadPage: true,
      showRightAside: true,
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
=======
export default {
  data() {
    return {
      activeIndex: '1'
    }
  },

  methods: {
    onSelect(/*idx*/) {

    }
  },
}
</script>
>>>>>>> c02c810230ec8f0d9fafcea9cbad71c0a49b6c60
