<template>
  <div class="open-form-view">
    <el-header>Header</el-header>
      <el-container>
        <el-aside width="200px" class="openForm-side left">

        </el-aside>
        <el-main>
          <el-menu :default-active="activeIndex" class="nav" mode="horizontal" @select="onSelect">
            <el-menu-item index="1">表单</el-menu-item>
            <el-menu-item index="2">
              <img src="" />
            </el-menu-item>
          </el-menu>
          <el-row type="flex" justify="center">
            <el-col :md="18"><router-view></router-view></el-col>
          </el-row>
        </el-main>
        <el-aside width="200px" class="openForm-side right">

        </el-aside>
      </el-container>
  </div>
</template>

<script>
export default {
  name: "openFormView",
  inject: ["reload", "leftAside", "rightAside"],
  components: {
  },
  data() {
    return {
    };
  },
  methods: {
  },
  mounted() {}
};
</script>

<style lang="scss">
@import './assets/css/index.scss'
</style>
