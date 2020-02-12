<template>
  <div class="form-input">
    <!-- <div class="desTitle">
      {{formItm.name || "标题"}}
    </div>
    <div class="desSubTitle">{{formItm.subTitle || '副标题'}}</div> -->
    <div class="title" :style="{textAlign: formItm.alignType}">
      {{formItm.name || '标题'}}
    </div>
    <div class="subtitle" :style="{textAlign: formItm.alignType}">
      {{formItm.subTitle || '副标题'}}
    </div>
  </div>
</template>

<script>
export default {
  name: "input",
  components: {},
  data() {
    return {
      title: "标题",
      subtitle: '描述',
    };
  },
  methods: {},
  mounted() {},
  props: ['formIndex', "formItm"]
};
</script>

<style lang="scss">
@import "./../css/index.scss";
</style>
