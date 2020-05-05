<template>
  <div class="section">
    <div class="section-heading">选项</div>
    <div class="input-textarea">
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
            @click="onRadioClick(option)"
          />

          <input
            v-if="field.multiple"
            :type="field.multiple ? 'checkbox' : 'radio'"
            id="choice" 
            name="choice" 
            v-model="option.checked"
          />

          <el-input v-model="option.label" :disabled="option.editable">
          </el-input>
          <i class="fa fa-trash-o" @click="onRemoveClick(index)"></i>
        </div>
      </draggable>
      <el-button type="primary" size="small" @click="onAddClick">添加选项</el-button>
      <el-button type="primary" size="small" @click="onAddOtherClick" :disabled="this.hasEditable">添加其他选项</el-button>
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
      hasEditable: false,
      checkedOption: null,
    }
  },

  created() {
    this.calculateHasEditable();
  },

  methods: {

    onDraggableSort() {

    },

    onInputChange(option, checkedLabel) {
      this.field.checkedOption = option.label;
      this.field.checkedOptionValue = option.value;
      this.value.forEach((opt) => {
        opt.checked = opt.label === checkedLabel;
      })
    },

    onRemoveClick(index){
      this.$confirm('此操作将删除该选项, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.deleteOption(index)
        })
    },

    deleteOption(index){
      this.value.splice(index, 1);
      this.calculateHasEditable();
    },

    onAddClick() {
      const option = {
        label: "选项",
        editable: false,
        checked: false,
      };
      this.value.push(option);
    },

    onAddOtherClick() {
      this.value.push({
        label: '其他',
        editable: true,
        checked: false,
      });

      this.calculateHasEditable();
    },

    onRadioClick(option) {
      this.cancelRadioCheck(option)
    },

    cancelRadioCheck(option) {
      if (option.value === this.field.checkedOptionValue) {
        option.checked = false;

        this.field.checkedOption = null;
        this.field.checkedOptionValue = null;
      }
    },

    calculateHasEditable() {
      for (const option of this.value) {
        if (option.editable) {
          this.hasEditable = true;
          return;
        }
      }
      this.hasEditable = false;
    }
  },
  components: {
    draggable,
  }
}
</script>
<style scoped>
</style>