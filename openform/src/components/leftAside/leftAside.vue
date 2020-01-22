<template>
    <div class="left-aside">
        <div class="my-components">我的组件
          <i class="fa fa-arrow-left" @click="leftAside()"></i>
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
                    <img :src="element.backimg">
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
        { name: "标题", subTitle: '副标题', type: "titles", backimg: require('./static/img/formsetting/titles.png') },
        { name: "标题", subTitle: '副标题', width: 20, placeholder: '', isRequired: false, type: "inputs", backimg: require('./static/img/formsetting/inputs.png') },
        { name: "标题", subTitle: '副标题', width: 20, placeholder: '', isRequired: false, textareaRows: 6, type: "textAreas", backimg: require('./static/img/formsetting/textareas.png') },
        { 
          name: "标题", 
          options: [
            {
              label: "选项1",
              value: "选项1"
            },
            {
              label: "选项2",
              value: "选项2"
            },
            {
              label: "选项3",
              value: "选项3"
            }
          ], 
          isRequired: false, type: "selects", backimg: require('./static/img/formsetting/selects.png') },
        { 
          name: "标题", 
          options: [
            {
              label: "选项1",
              value: "选项1"
            },
            {
              label: "选项2",
              value: "选项2"
            },
            {
              label: "选项3",
              value: "选项3"
            }
          ], 
          isRequired: false, type: "multiSelects", backimg: require('./static/img/formsetting/multiSelects.png') },
        { name: "分割线", height: '1px', background: '#eeeeee', type: "divideLines", backimg: require('./static/img/formsetting/divides.png') },
        { name: "富文本", type: "editors", backimg: require('./static/img/formsetting/wangEditor.png') },
      ],
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
