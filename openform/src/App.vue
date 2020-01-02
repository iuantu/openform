<template>
  <div id="app">
    <el-container>
      <el-header>Header</el-header>
    </el-container>
    <el-container>
      <router-view class="main-container"></router-view>
    </el-container>

  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return {}
  },
  methods: {},
  components: {}
}
</script>

<style lang="scss">
  @import "./assets/css/index.scss";
</style>
