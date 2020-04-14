<template>
  <div class="open-form">
    <el-container>
      <el-aside width="265px" class="openForm-side left">
        <field-panel v-show="!hideFieldPanel" ></field-panel>
      </el-aside>
      <el-main>
        <the-form></the-form>
      </el-main>
    </el-container>
  </div>
</template>

<script>

import FieldPanel from './../../components/FieldPanel/FieldPanel'
import TheForm from './../../components/TheForm/TheForm'

export default {
  components: {
    FieldPanel,
    TheForm,
  },
  data() {
    return {
      hideFieldPanel: true,
    };
  },

  methods: {
    _hideFieldPanel(hide) {
      this.hideFieldPanel = hide;
    }
  },

  provide() {
    return {
      hideFieldPanel: this._hideFieldPanel,
    };
  },
};
</script>

<style lang="scss">

.open-form {
  width: 100vw;
  height: calc(100vh - 48px);

  .el-container{
    height: 100%;
    width: 100%;
    .show-left-aside{
      width: 30px;
      height: 30px;
      display: flex;
      display: -webkit-flex;
      justify-content: center;
      align-items: center;
      color: white;
      background: #7d7c7c;
      border-radius: 50%;
      position: absolute;
      left: 5px;
      top: 60px;
    }
    .el-main{
      width: 100%;
      // text-align: center;
      padding: 0;
    }
  }
}
</style>
