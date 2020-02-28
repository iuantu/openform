<template>
  <div>
    <div class="right-title">选项</div>
      <div class="input-textarea">
        <draggable tag="ul" :list="field.options" class="list-group" handle=".handle" @sort="onDraggableSort" ghost-class="ghost">
          <div
            class="list-group-item"
            v-for="(option, index) in field.options"
            :key="index"
          >
            <i class="fa fa-align-justify handle"></i>
            <el-input v-model="option.value" @input="onOptionChange">
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
export default {
  props: {
    field: {
      type: Object
    }
  },
  data() {
    return {
    }
  },
  created() {

  },
  methods: {
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
      this.selfDefVal.splice(index, 1)
      this.setForms()
    },
    onAddClick() {
      let _leg = Math.random() * 1000
      const option = {
        label: "选项",
        editable: false
      }
      this.selfDefVal.push(_itm)
    }
  }
}
</script>