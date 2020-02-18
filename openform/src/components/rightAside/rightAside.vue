<template>
    <div class="right-aside">
      <div v-if="itemType == 'titles'">
        <div class="right-title">标题</div>
        <div class="input-style">
          <el-input v-model="titleForm.title" placeholder="标题" @input="setForms"></el-input>
        </div>
        <div class="right-title">副标题</div>
        <div class="input-style">
          <el-input v-model="titleForm.subtitle" placeholder="副标题" @input="setForms"></el-input>
        </div>
        <div class="right-title">文字大小</div>
        <el-radio-group v-model="titleFormSize" @change="setForms">
          <el-radio-button label="default">默认</el-radio-button>
          <el-radio-button label="big">大</el-radio-button>
          <el-radio-button label="small">小</el-radio-button>
        </el-radio-group>
        <div class="right-title">对齐方式</div>
        <el-radio-group v-model="titleFormAlign" @change="setForms">
          <el-radio-button label="left">左对齐</el-radio-button>
          <el-radio-button label="center">剧中</el-radio-button>
          <el-radio-button label="right">右对齐</el-radio-button>
        </el-radio-group>
      </div>
      <div v-if="itemType == 'inputs' || itemType == 'textAreas'">
        <div class="title-name">属性设置</div>
        <div class="right-title">标题</div>
        <div class="input-style">
          <el-input size="small" v-model="inputForm.title" placeholder="标题" @input="setForms"></el-input>
        </div>
        <div class="right-title">说明</div>
        <div class="input-textarea">
          <el-input type="textarea" :row="3" size="small" v-model="inputForm.subtitle" placeholder="副标题" @input="setForms"></el-input>
        </div>
        <div class="right-title">是否必选</div>
        <div class="input-style">
          <el-switch size="small" v-model="itmRequired" @change="setForms"></el-switch>
        </div>
        <div class="right-title" v-if="itmRequired">校验提示</div>
        <div class="input-style" v-if="itmRequired">
          <el-input size="small" v-model="inputForm.requireText" placeholder="校验提示" @input="setForms"></el-input>
        </div>
        <div class="right-title">对齐方式</div>
        <div class="input-style">
          <el-radio-group size="small" v-model="titleFormAlign" @change="setForms">
            <el-radio-button label="left">左对齐</el-radio-button>
            <el-radio-button label="center">剧中</el-radio-button>
            <el-radio-button label="right">右对齐</el-radio-button>
          </el-radio-group>
        </div>
        <div class="right-title" v-if="itemType == 'textAreas'">行数</div>
        <div class="input-style" v-if="itemType == 'textAreas'">
          <el-input size="small" type="number" v-model="textareaRows" @input="setForms"></el-input>
        </div>
        <div class="right-title">宽度</div>
        <div class="slider-style">
          <el-slider size="small" :min='50' v-model="inputForm.width" :step="10" @input="setForms"></el-slider>
        </div>
        <div class="right-title">占位符</div>
        <div class="input-style">
          <el-input size="small" v-model="inputForm.placeholder" @input="setForms"></el-input>
        </div>
      </div>
      <div v-if="itemType == 'divideLines'">
        <div class="right-title">线条颜色</div>
        <div class="input-style">
          <el-color-picker v-model="divideColor" @change="setForms"></el-color-picker>
        </div>
        <div class="right-title">高度</div>
        <div class="input-style">
          <el-input type='number' v-model="lineHeight" @input="setForms"></el-input>
        </div>
      </div>
      <div v-if="itemType == 'selects' || itemType == 'multiSelects'">
        <div class="right-title">标题</div>
        <div class="input-style">
          <el-input size="small" v-model="selectForm.title" placeholder="标题" @input="setForms"></el-input>
        </div>
        <div class="right-title">说明</div>
        <div class="input-textarea">
          <el-input type="textarea" :row="3" size="small" v-model="selectForm.subtitle" placeholder="副标题" @input="setForms"></el-input>
        </div>
        <div class="right-title">是否必选</div>
        <div class="input-style">
          <el-switch size="small" v-model="itmRequired" @change="setForms"></el-switch>
        </div>
        <div class="right-title" v-if="itmRequired">校验提示</div>
        <div class="input-style" v-if="itmRequired">
          <el-input size="small" v-model="selectForm.requireText" placeholder="校验提示" @input="setForms"></el-input>
        </div>
        <div class="right-title">选项{{selectrows}}</div>
        <div class="input-textarea">
          <el-input size="small" v-model="selectForm.options" type="textarea" :rows="selectrows" @input="setForms"></el-input>
        </div>
        <div class="right-title">使用自定义值</div>
        <div class="input-style">
          <el-switch v-model="selfDef"></el-switch>
        </div>
        <div class="input-textarea">
          <el-table size="small" border v-if="selfDef && isTableChange" :data="selfDefVal" :show-header="false">
            <el-table-column prop="value"></el-table-column>
            <el-table-column prop="label">
              <template slot-scope="scope">
                <el-input size="small" v-model="scope.row.label"></el-input>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="right-title">对齐方式</div>
        <div class="input-style">
          <el-radio-group size="small" v-model="titleFormAlign" @change="setForms">
            <el-radio-button label="left">左对齐</el-radio-button>
            <el-radio-button label="center">剧中</el-radio-button>
            <el-radio-button label="right">右对齐</el-radio-button>
          </el-radio-group>
        </div>
        <div class="right-title">宽度</div>
        <div class="slider-style">
          <el-slider size="small" :min='50' v-model="selectForm.width" :step="10" @input="setForms"></el-slider>
        </div>
      </div>
    </div>
      
</template>

<script>
export default {
  name: "rightAside",
  components: {},
  data() {
    return {
      itemType: '',
      titleForm:{
        title: '标题',
        subtitle: '副标题'
      },
      titleFormSize: 'default',
      titleFormAlign: 'left',
      inputForm: {
        title: '标题',
        subtitle: '副标题',
        width: 20,
        placeholder: ''
      },
      itmRequired: false,
      textareaRows: 6,
      divideColor: '#eeeeee',
      lineHeight: 1,
      selfDef: false,
      selectForm: {
        title: '标题',
        options: ''
      },
      selfDefVal: [],
      selectrows: 3,
      isTableChange: true,
    };
  },
  methods: {
    setForms(){
      let postData = {}
      if(this.itemType == 'titles'){
        postData = this.titleForm
        postData.fontSize = this.titleFormSize
        postData.align = this.titleFormAlign
      }
      else if(this.itemType == 'inputs'|| this.itemType == 'textAreas'){
        postData = this.inputForm
        postData.align = this.titleFormAlign
        postData.isRequired = this.itmRequired
        if(this.itemType == 'textAreas'){
          postData.textareaRows = this.textareaRows
        }
      }
      if(this.itemType == 'divideLines'){
        postData = {
          height: this.lineHeight + 'px',
          background: this.divideColor
        }
      }
      if(this.itemType == 'selects' || this.itemType == 'multiSelects'){
        postData = JSON.parse(JSON.stringify(this.selectForm))
        postData.align = this.titleFormAlign
        postData.options = []
        postData.isRequired = this.itmRequired
        // postData = {
        //   options: [],
        //   title: this.selectForm.title,
        //   isRequired: this.itmRequired
        // }
        let _opts = this.selectForm.options.split('\n')
        this.selectrows = _opts.length < 10 ? _opts.length : 10
        this.selfDefVal = []
        _opts.map((itm, index)=>{
            let _itm = {
              value: itm,
              label: (this._selfDefVal[index] ? this._selfDefVal[index].label : itm)
            }
            if(this._selfDefVal[index] && this._selfDefVal[index].id){
              _itm.id = this._selfDefVal[index].id
            }
            postData.options.push(_itm)
            this.selfDefVal.push(_itm)
        })
        // console.log(this.selfDefVal)
      }
      this.$emit('formSet', postData)
    },
    // 选项改变
    setSelect(){
      // console.log(this.selectForm.options)
      let postData = {
        options: [],
        name: this.selectForm.title,
        isRequired: this.itmRequired
      }
      let _opts = this.selectForm.options.split('\n')
      _opts.map((itm, index)=>{
        if(index != _opts.length - 1){
          let _itm = {
            value: itm,
            label: (this.selfDefVal[index] ? this.selfDefVal[index].label : itm)
          }
          if(itm.id && this.selfDefVal[index]){
            _itm.id = this.selfDefVal[index].id
          }
          postData.options.push(_itm)
        }
      })
      // console.log(postData.options)


    }
  },
  mounted() {
  },
  props:['formItem'],
  watch: {
    formItem:{
      handler: function (newVal) {
        // console.log(newVal)
        this.itemType = newVal.type
        if(newVal.type == 'titles'){
          this.titleForm = {
            title: newVal.name,
            subtitle: newVal.subTitle
          }
        }
        else if(newVal.type == 'inputs' || newVal.type == 'textAreas'){
          this.inputForm= {
            title: newVal.name,
            subtitle: newVal.subTitle,
            width: newVal.width,
            placeholder: newVal.placeholder,
            requireText: newVal.requireText
          }
          this.itmRequired = newVal.isRequired
          if(newVal.type == 'textAreas'){
            this.textareaRows = newVal.textareaRows
          }
        }
        else if(newVal.type == 'selects' || newVal.type == 'multiSelects'){
          this.selectForm = {
            title: newVal.name,
            subtitle: newVal.subTitle,
            width: newVal.width,
            requireText: newVal.requireText,
            options: ''
          }
          this.selfDefVal = []
          newVal.options.map(itm=>{
            this.selectForm.options += itm.value + '\n'
            this.selfDefVal.push(itm)
          })
          this._selfDefVal = JSON.parse(JSON.stringify(this.selfDefVal))
          this.selectrows = newVal.options.length < 10 ? newVal.options.length: 10

          this.itmRequired = newVal.isRequired
        }
      } 
    },
    deep: true
  }
};
</script>

<style lang="scss">
  @import "./css/index.scss";
</style>
