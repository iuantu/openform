<template>
  <div class="open-form-setting">
    <el-container>
      <el-main class="inner-content">
        <div class="inner-title">
          <div class="form-title" :style="{textAlign: 'left'}">{{title}}</div>
          <div class="form-sub-title" :style="{textAlign: 'left'}">{{subtitle}}</div>
        </div>
        <draggable
          class="dragArea list-group"
          :list="list"
          group="people"
          ghost-class="ghost"
        >
          <div v-if="showList">
            <div class="list-group-item" v-for="(formItm, formIndex) in list" :key="formIndex + '_form'">
              <form-components :formItm="formItm" :formType="formItm.type" :formIndex="formIndex"></form-components>
              <div class="components-setting-btn">
                <el-button type="primary" @click="setChange(formIndex)">设置</el-button>  
                <el-button type="danger">删除</el-button>
              </div>
            </div>
          </div>
          
        </draggable>
      </el-main>
      <el-aside v-show="showRightAside" width="200px" class="openForm-side right">
        <right-aside :formItem="formItem" @formSet="formSets"></right-aside>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import draggable from "vuedraggable";

import formComponents from "./../../components/formComponent/formComponet";
import RightAside from './../../components/rightAside/rightAside'


export default {
  name: "clone",
  inject: ["reload", "leftAside"],
  components: {
    draggable,
    "form-components": formComponents,
    'right-aside': RightAside,
  },
  data() {
    return {
      title: '标题',
      subtitle: '副标题',
      list: [],
      showRightAside: true,
      formItem: {},
      settingIndex: null,
      showList: true
    };
  },
  methods: {

    // 显示/隐藏右侧栏
    showRA(){
      this.showRightAside = !this.showRightAside
    },
    setChange(index){
      this.settingIndex = index
      this.formItem = JSON.parse(JSON.stringify(this.list[index]))
    },
    // 右侧栏传值
    formSets(params){
      let _par = JSON.parse(JSON.stringify(params))
      let _type = this.list[this.settingIndex].type
      let _itm = JSON.parse(JSON.stringify(this.list[this.settingIndex]))
      if( _type == 'titles'){
        _itm.name = _par.title
        _itm.subTitle = _par.subtitle
      }
      else if(_type == 'inputs' || _type == 'textAreas' ){
        _itm.name = _par.title
        _itm.subTitle = _par.subtitle
        _itm.width = _par.width
        _itm.placeholder = _par.placeholder
        _itm.isRequired = _par.isRequired
        if(_type == 'textAreas'){
          _itm.textareaRows = parseInt(_par.textareaRows)
        }
      }
      else if(_type == 'divideLines'){
        _itm.height = _par.height
        _itm.background = _par.background
      }
      else if(_type == 'selects' || _type == 'multiSelects'){
        _itm.name = _par.title
        _itm.options = _par.options
        _itm.isRequired = _par.isRequired
      }
      this.list[this.settingIndex] = JSON.parse(JSON.stringify(_itm))
      this.showList = false
      this.$nextTick(()=>{
        this.showList = true
      })
      
      
    }
  },
  mounted() {}
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
