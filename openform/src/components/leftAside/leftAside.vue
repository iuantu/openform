<template>
    <div class="left-aside">
        <div class="my-components">基本
          <!-- <i class="fa fa-arrow-left" @click="leftAside()"></i> -->
        </div>
        <draggable
            class="dragArea list-group"
            :list="list1"
            :group="{ name: 'people', pull: 'clone', put: false,  }"
            :sort="false"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list1"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
        <div class="my-components">联系人
        </div>
        <draggable
            class="dragArea list-group"
            :list="list2"
            :group="{ name: 'people', pull: 'clone', put: false,  }"
            :sort="false"
            :disabled="true"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list2"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
        <div class="my-components">支付</div>
        <draggable
            class="dragArea list-group"
            :list="list3"
            :group="{ name: 'people', pull: 'clone', put: false,  }"
            :sort="false"
            :disabled="true"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list3"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
        <div class="my-components">高级</div>
        <draggable
            class="dragArea list-group"
            :list="list4"
            :group="{ name: 'people', pull: 'clone', put: false,  }"
            :sort="false"
            :disabled="true"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list4"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
    </div>
      
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name: "clone",
  inject: ['leftAside'],
  components: {
    draggable
  },
  data() {
    return {
      list1: [
        // { name: "标题", subTitle: '副标题', type: "titles", backimg: require('./static/img/formsetting/titles.png') },
        { name: "标题", subTitle: '说明', showName: '文本字段', defaults: '', isMax: false, isMin: false, max: 0, min: 0, width: 100, placeholder: '', isRequired: false, requireText: '校验提示', isRequiredText: false, alignType: 'left', type: "inputs", backimg: require('./static/img/formsetting/inputs.png') },
        { name: "标题", subTitle: '说明', showName: '多行文本', defaults: '', isMax: false, isMin: false, max: 0, min: 0, width: 100, placeholder: '', isRequired: false, requireText: '校验提示', isRequiredText: false, alignType: 'left', textareaRows: 6, type: "textAreas", backimg: require('./static/img/formsetting/textareas.png') },
        { name: "描述", subTitle: '说明', showName: '描述', defaults: '', isMax: false, isMin: false, max: 0, min: 0, width: 100, placeholder: '', isRequired: false, requireText: '校验提示', isRequiredText: false, alignType: 'left', textareaRows: 6, type: "description", backimg: require('./static/img/formsetting/textareas.png') },
        { 
          name: "标题", 
          subTitle: '说明',
          showName: '单项选择',
          isRequiredText: false,
          options: [
            {
              label: "选项1",
              value: "选项1",
              isText: false
            },
            {
              label: "选项2",
              value: "选项2",
              isText: false
            },
            {
              label: "选项3",
              value: "选项3",
              isText: false
            }
          ], 
          width: 100, isRequired: false, requireText: '校验提示', alignType: 'left', type: "selects", backimg: require('./static/img/formsetting/selects.png') },
        { 
          name: "标题", 
          subTitle: '说明',
          showName: '多项选择',
          isRequiredText: false,
          options: [
            {
              label: "选项1",
              value: "选项1",
              isText: false
            },
            {
              label: "选项2",
              value: "选项2",
              isText: false
            },
            {
              label: "选项3",
              value: "选项3",
              isText: false
            }
          ], 
          width: 100, isRequired: false, requireText: '校验提示', alignType: 'left', type: "multiSelects", backimg: require('./static/img/formsetting/multiSelects.png') },
        // { name: "文件上传", showName: '文件上传', height: '1px', background: '#eeeeee', type: "uploadFiles", backimg: require('./static/img/formsetting/divides.png') },
        // { name: "分割线", height: '1px', background: '#eeeeee', type: "divideLines", backimg: require('./static/img/formsetting/divides.png') },
        { name: "富文本", showName: '富文本', type: "editors", value: '', backimg: require('./static/img/formsetting/wangEditor.png') },
      ],
      list2: [
        { name: "真实姓名", subTitle: '请输入您的真实姓名', showName: '姓名', width: 100, placeholder: '', isRequired: false, requireText: '校验提示', alignType: 'left', type: "inputsNames", backimg: require('./static/img/formsetting/inputs.png') },
        { name: "手机号码", subTitle: '请输入您的手机号码', showName: '手机号码', width: 100, placeholder: '', isRequired: false, requireText: '校验提示', alignType: 'left', type: "inputsCells", backimg: require('./static/img/formsetting/inputs.png') },
      ],
      list3: [
        { name: "支付", subTitle: '支付', showName: '支付', width: 100, placeholder: '', isRequired: false, requireText: '校验提示', alignType: 'left', type: "payments", backimg: require('./static/img/formsetting/inputs.png') },
      ],
      list4: [
        { name: "NPS", subTitle: 'NPS', showName: 'NPS', width: 100, placeholder: '', isRequired: false, requireText: '校验提示', alignType: 'left', type: "NPS", backimg: require('./static/img/formsetting/inputs.png') },
        { name: "评分", subTitle: '评分', showName: '评分', width: 100, placeholder: '', isRequired: false, requireText: '校验提示', alignType: 'left', type: "counts", backimg: require('./static/img/formsetting/inputs.png') },
      ]
    };
  },
  methods: {
  },
  mounted() {
  },
};
</script>

<style lang="scss">
  @import "./css/index.scss";
</style>
