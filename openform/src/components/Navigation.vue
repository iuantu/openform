<template>
  <el-menu :default-active="activeIndex" class='of-menu' mode="horizontal" @select="handleSelect">
    <img src="../assets/openform/logo.png" />
    <el-menu-item index="1">表单</el-menu-item>
  </el-menu>
</template>
<style scoped>
.of-menu img {
  float: left;
  width: 39px;
  height: 32px;
  margin: 7px;
}

.el-menu-item, .el-submenu-title {
  height: 46px;
  line-height: 46px;
}
</style>

<script>
export default {
}
</script>
