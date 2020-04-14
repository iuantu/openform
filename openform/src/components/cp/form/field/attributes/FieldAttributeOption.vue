<template>
  <div>
    <div class="right-title">选项</div>
    <div class="input-textarea">
      <!-- <el-radio-group v-model="checked"> -->
      <draggable
        tag="ul"
        :list="value"
        class="list-group"
        handle=".handle"
        @sort="onDraggableSort"
        ghost-class="ghost"
      >
        <div
          class="list-group-item"
          v-for="(option, index) in value"
          :key="index"
        >
          <i class="fa fa-align-justify handle"></i>
          <input
            v-if="!field.multiple"
            :type="field.multiple ? 'checkbox' : 'radio'"
            id="choice" 
            name="choice" 
            v-model="field.checkedOptionValue"
            :value="option.value"
            @change="onInputChange(option, $event)"
          />

          <input
            v-if="field.multiple"
            :type="field.multiple ? 'checkbox' : 'radio'"
            id="choice" 
            name="choice" 
            v-model="option.checked"
          />

          <el-input v-model="option.label">
            <!-- 其他选项 -->
            <!-- <el-button slot="append" @click="setIsText(index)">
              <span :class="{'isText': optItm.isText}">T</span>
            </el-button> -->
          </el-input>
          <i class="fa fa-trash-o" @click="onRemoteClick(index)"></i>
        </div>
      </draggable>
      <!-- </el-radio-group> -->
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
    },
    field: {
      type: Object,
    },
    meta: {
      type: Object
    },
  },
  data() {
    return {
      checkedOption: null,
    }
  },
  methods: {

    onDraggableSort() {

    },

    onInputChange(option, checkedLabel) {
      this.field.checkedOption = option.label;
      this.field.checkedOptionValue = option.value;
      this.value.forEach((opt) => {
        opt.checked = opt.label == checkedLabel;
      })
      // this.$emit('input', option);
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
      this.value.splice(index, 1)
    },
    onAddClick() {
      const option = {
        label: "选项",
        editable: false,
        checked: false,
      };
      this.value.push(option);
    }
  },
  components: {
    draggable,
  }
}
</script>
<style scoped>
.checkbox {
  display: inline;
}

</style>