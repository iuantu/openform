<template>
  <div class="form-preview">
    <el-radio-group size="small" v-model="showType">
      <el-radio-button label="computer">浏览器</el-radio-button>
      <el-radio-button label="mobile">手机</el-radio-button>
    </el-radio-group>
    <div class="preview-content" v-if="showType == 'computer'">
        <div v-for="(formItm, formIndex) in list" :key='formIndex + "_form"'>
            <form-preview :formType='formItm.type' :formIndex="formIndex" :formItm="formItm"></form-preview>
        </div>
    </div>
  </div>
</template>

<script>
import FormPreView from './../formPreviewComponent/formPreview'
export default {
  name: "formPreView",
  data() {
    return {
        showType: 'computer'
    };
  },
  components: {
      'form-preview': FormPreView,
  },
  methods: {
    
  },
  created(){

  },
  mounted() {
  },
  props: ['list']
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
