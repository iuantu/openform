<template>
  <div class="open-form-view">
      <el-container>
        <el-aside width="200px" class="openForm-side left">
        </el-aside>
        <el-main>
          <el-menu :default-active="activeIndex" class="nav" mode="horizontal" @select="onSelect">
            <el-menu-item index="1">
              <router-link :to="{ path: '/' }">表单</router-link>
            </el-menu-item>
            <el-menu-item index="2">
              <router-link :to="'FormData'">数据</router-link>
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
  components: {
  },
  data() {
    return {
      activeIndex: '1'
    };
  },
  methods: {
    onSelect(/*idx*/) {

    }
  },
  mounted() {}
};
</script>

<style lang="scss">
@import './assets/css/index.scss'
</style>
