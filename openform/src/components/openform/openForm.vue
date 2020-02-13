<template>
  <div class="open-form-setting">
    <el-container>
      <el-main class="inner-content">
        <div class="add-new">
          <el-button type="primary" size="small" @click="saveForm">保存</el-button>
        </div>
        <div class="roll-contant">
          <div class="inner-title">
            <div class="form-title" :style="{textAlign: 'left'}" @click="setTitles">
              <span v-if="!changeTitle">{{title}}</span>
              <el-input v-model="title" ref="titles" placeholder="请输入表单标题" v-if="changeTitle" @blur="changeTitle = false"></el-input>
            </div>
            <div class="form-sub-title" :style="{textAlign: 'left'}" @click="setSubTitles">
              <span v-if="!changeSubTitle">{{subtitle}}</span>
              <el-input v-model="subtitle" ref="subTitles" placeholder="请输入表单副标题" v-if="changeSubTitle" @blur="changeSubTitle = false"></el-input>
            </div>
          </div>
          <draggable
            class="dragArea list-group"
            :list="list"
            group="people"
            ghost-class="ghost"
            v-if="showList"
            @sort="addItms"
          >
            <div class="list-group-item" v-for="(formItm, formIndex) in list" :key="formIndex + '_form'">
              <form-components :formItm="formItm" :formType="formItm.type" :formIndex="formIndex"></form-components>
              <div class="components-setting-btn">
                <el-button type="primary" size="small" icon="el-icon-edit" circle @click="setChange(formIndex)"></el-button>
                <div class="delete-btn">
                  <el-button type="danger" size="small" icon="el-icon-delete" circle @click="deleteList(formIndex)"></el-button>
                </div>
              </div>
            </div>
            <div class="no-list" v-if="list.length == 0">拖 拽 区</div>
          </draggable>
        </div>
        
      </el-main>
      <el-aside v-show="showRightAside" width="265px" class="openForm-side right">
        <right-aside :formItem="formItem" @formSet="formSets"></right-aside>
      </el-aside>
    </el-container>
  </div>
</template>

<script>
import draggable from "vuedraggable";

import formComponents from "./../../components/formComponent/formComponet";
import RightAside from './../../components/rightAside/rightAside'
import { SecurityService } from '../../functions';


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
      showList: true,
      formDetail: null,
      changeTitle: false,
      changeSubTitle: false,
      _id: null,

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
    deleteList(index){
      this.$confirm('此操作将删除该选项, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.list.splice(index, 1)
          this.formItem = {}
        })
    },
    addItms(){
      this.formItem = {}
    },
    // 右侧栏传值
    formSets(params){
      console.log(params)
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
        _itm.width = _par.width
        _itm.requireText = _par.requireText
        _itm.alignType = _par.align
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
        _itm.subTitle = _par.subtitle
        _itm.width = _par.width
        _itm.placeholder = _par.placeholder
        _itm.options = _par.options
        _itm.isRequired = _par.isRequired
        _itm.width = _par.width
        _itm.requireText = _par.requireText
        _itm.alignType = _par.align
        if(_par.id){
          _itm.id = _par.id
        }
      }
      this.list[this.settingIndex] = JSON.parse(JSON.stringify(_itm))
      this.showList = false
      this.$nextTick(()=>{
        this.showList = true
      })
    },
    saveForm(){
      // console.log(this.list)
      // return
      let postData = {
        title: this.title,
        fields: []
      }
      if(this._id){
        postData.id = this._id
      }
      this.list.map((itm, index)=>{
        if(itm.type == "inputs" || itm.type == "textAreas"){
          let _itm = {
            title: itm.name,
            name: "name" + index,
            discriminator: "text_field",
            multiple: false,
            placeholder: itm.placeholder,
            constraints: []
          }
          if(itm.id){
            _itm.id = itm.id
          }
          if(itm.isRequired){
            _itm.constraints = [
              {
                "discriminator": "required_constraint"
              }
            ]
          }
          if(itm.type == "textAreas"){
            _itm.multiple = true
            _itm.layout_row_index = itm.textareaRows
          }
          postData.fields.push(_itm)
        }
        else if(itm.type == "selects" || itm.type == "multiSelects"){
          let _itm = {
            title: itm.name,
            discriminator: "select_field",
            multiple: false,
            type: 'radio',
            constraints: [],
            options: []
          }
          if(itm.id){
            _itm.id = itm.id
          }
          if(itm.isRequired){
            _itm.constraints = [
              {
                "discriminator": "required_constraint"
              }
            ]
          }
          itm.options.map(opts=>{
            let _opts = {
              label: opts.value
            }
            if(opts.id){
              _opts.id = opts.id
            }
            _itm.options.push(_opts)
          })
          if(itm.type == "multiSelects"){
            postData.type == 'checkbox'
          }
          postData.fields.push(_itm)
        }
      })
      if(this._id){
        this.service.putApi('/cp/form/' + this._id, postData).then(({data})=>{

        })
      }
      else{
        this.service.postApi('cp/form', postData).then(({data})=>{
          // console.log(data)
        })

      }
    },
    getForm(){
      this.list = []
      this._id = this.$route.query.id
      if(this._id){
        this.service.getApi('cp/form/' + this._id).then(data=>{
          // console.log(data)
          this.title = data.title
          data.fields.map(itm=>{
            let _itm = {
              name: itm.title, 
              subTitle: itm.title, 
              width: 100, 
              isRequired: false, 
              requireText: '校验提示', 
              alignType: 'left', 
              id: itm.id,
              form_id: itm.form_id,
              constraints: itm.constraints
            }
            itm.constraints.map(requ => {
              if(requ.discriminator && requ.discriminator == 'required_constraint'){
                _itm.isRequired = true
              }
            })
            if(itm.discriminator == 'text_field' && !itm.multiple){
              _itm.type = 'inputs'
              _itm.showName = '文本字段'
              _itm.placeholder = itm.placeholder
            }
            if(itm.discriminator == "text_field" && itm.multiple){
              _itm.type = "textAreas"
              _itm.textareaRows = itm.layout_row_index
              _itm.showName = '多行文本'
              _itm.placeholder = itm.placeholder
            }
            if(itm.discriminator == 'select_field'){
              if(itm.type == "radio"){
                _itm.type = 'selects'
                _itm.showName = '单项选择'
              }
              else if(itm.type == 'checkbox'){
                _itm.type = 'multiSelects'
                _itm.showName = '多项选择'
              }
              _itm.options = []
              itm.options.map(opt => {
                let _opt = {
                  label: opt.value,
                  value: opt.label,
                  editable: opt.editable,
                  field_id: opt.field_id,
                  id: opt.id,
                  ordering: opt.ordering
                }
                _itm.options.push(_opt)
              })
            }
            this.list.push(_itm)
          })
        })
      }
    },
    // 修改form title
    setTitles(){
      this.changeTitle = true
      this.$nextTick(()=>{
        this.$refs.titles.$el.querySelector('input').focus()
      })
    },
    // 修改副标题
    setSubTitles(){
      this.changeSubTitle = true
      this.$nextTick(()=>{
        this.$refs.subTitles.$el.querySelector('input').focus()
      })
    }
  },
  created(){
    this.service = new SecurityService();
    this.getForm()
  },
  mounted() {}
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
