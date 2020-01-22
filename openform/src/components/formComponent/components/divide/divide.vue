<template>

  <div class="divide-line" :style="{height: formItm.height, background: formItm.background}"></div>
</template>

<script>
export default {
  name: "divide",
  props: ['formIndex', 'formItm'],
};
</script>

<style lang="scss">
@import "./../css/index.scss";
</style>
