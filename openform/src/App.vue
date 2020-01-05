<template>
    <div id="app">
      <Navigation></Navigation>
      <router-view></router-view>
    </div>
</template>
<style scoped>
body {
  font-size: 14px;
}
</style>

<script>

import Navigation from './components/Navigation'
export default {
  data(){
    return {
    }
  },
  methods: {
  },
  components: {
    Navigation: Navigation,
  }
}
</script>

<style lang="scss">
  @import "./assets/css/index.scss";
</style>
