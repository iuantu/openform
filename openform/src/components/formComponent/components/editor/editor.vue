<template>
  <div class="form-input">
    <div :ref="'editorElem' + randoms" style="text-align:left;"></div>
  </div>
</template>

<script>
import E from "wangeditor";
export default {
  name: "editor",
  components: {},
  data() {
    return {
      randoms: 0,
      editor: null,
      editorContent: ""
    };
  },
  methods: {},
  created() {
    this.randoms = this.formIndex
  },
  mounted() {
    let editorElem = "editorElem" + this.randoms;
    this.editor = new E(this.$refs[editorElem]);
    // 编辑器的事件，每次改变会获取其html内容
    this.editor.customConfig.onchange = html => {
      this.editorContent = html;
    };
    this.editor.customConfig.menus = [
      // 菜单配置
      "head", // 标题
      "bold", // 粗体
      "fontSize", // 字号
      "fontName", // 字体
      "italic", // 斜体
      "underline", // 下划线
      //'strikeThrough', // 删除线
      "foreColor", // 文字颜色
      "backColor", // 背景颜色
      //'link', // 插入链接
      //'list', // 列表
      "justify", // 对齐方式
      //'quote', // 引用
      //'emoticon', // 表情
      "image", // 插入图片
      "table", // 表格
      //'code', // 插入代码
      "undo", // 撤销
      "redo" // 重复
    ];
    this.editor.create(); // 创建富文本实例
  },
  props: ['formIndex']
};
</script>

<style lang="scss">
@import "./../css/index.scss";
</style>
