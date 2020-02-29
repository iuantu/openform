<template>
  <div>
    <div class="right-title">选项</div>
      <div class="input-textarea">
        <draggable tag="ul" :list="value" class="list-group" handle=".handle" @sort="onDraggableSort" ghost-class="ghost">
          <div
            class="list-group-item"
            v-for="(option, index) in value"
            :key="index"
          >
            <i class="fa fa-align-justify handle"></i>
            <el-input v-model="option.label" @input="onOptionChange">
              <!-- <el-button slot="append" @click="setIsText(index)">
                <span :class="{'isText': optItm.isText}">T</span>
              </el-button> -->
            </el-input>
            <i class="fa fa-trash-o" @click="onRemoteClick(index)"></i>
          </div>
        </draggable>
        <el-button type="primary" size="small" @click="onAddClick">添加选项</el-button>
      </div>
  </div>
</template>
<script>
import draggable from "vuedraggable";

export default {
  key: 'options',
  props: {
    value: {
      type: Array
    }
  },
  data() {
    return {
      options: [],
    }
  },
  created() {
    this.bind();
  },
  methods: {
    bind() {
      this.options = this.value;
    },

    onDraggableSort() {

    },

    onRemoteClick(index){
      this.$confirm('此操作将删除该选项, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.deleteOption(index)
        })
    },
    deleteOption(index){
      this.options.splice(index, 1)
    },
    onAddClick() {
      const option = {
        label: "选项",
        editable: false
      };
      this.value.push(option);
    }
  },
  watch: {
    value() {
      this.field = this.value;
    }
  },
  components: {
    draggable,
  }
}
</script>