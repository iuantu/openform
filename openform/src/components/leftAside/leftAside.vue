<template>
    <div class="left-aside">
        <h3>Draggable 1</h3>
            <draggable
                class="dragArea list-group"
                :list="list1"
                :group="{ name: 'people', pull: 'clone', put: false,  }"
                :sort="false"
                ghost-class="ghost">
                <div
                class="list-group-item"
                v-for="element in list1"
                :key="element.name"
                >
                {{ element.name }}
                </div>
            </draggable>
    </div>
      
</template>

<script>
import draggable from 'vuedraggable'
export default {
  name: "clone",
  components: {
    draggable
  },
  data() {
    return {
      list1: [
        { name: "单行输入", type: "input" },
        { name: "多行输入", type: "textArea" },
        { name: "单选", type: "select" },
        { name: "多选", type: "multiSelect" },
        { name: "分割线", type: "divideLine" },
        { name: "富文本", type: "editor" },
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
