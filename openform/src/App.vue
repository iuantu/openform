<template>
  <div id="app">
    <el-menu :default-active="activeIndex" class="nav" mode="horizontal" @select="onSelect">
      <el-menu-item index="1">表单</el-menu-item>
      <el-menu-item index="2">
        <img src="" />
      </el-menu-item>
    </el-menu>
    <el-row type="flex" justify="center">
      <el-col :md="10"><router-view></router-view></el-col>
    </el-row>
  </div>
</template>
<style scoped>
  .nav {
    margin-bottom: 50px;
  }
</style>

<script>
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