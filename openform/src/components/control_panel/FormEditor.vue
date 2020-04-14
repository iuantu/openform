<template>
<div class="roll-contant">
  <div class="inner-title">
    <div class="form-title" :style="{textAlign: 'left'}">
      <el-input v-model="title" placeholder="请输入表单标题" @change="onTitleChange"></el-input>
    </div>
    <div class="form-sub-title" :style="{textAlign: 'left'}">
      <rich-text :text="description" @change="onDescriptionChange"></rich-text>
    </div>
  </div>
  <draggable
    class="dragArea list-group"
    :list="fields"
    group="components"
    ghost-class="ghost"
    @add="onAdd"
    @change="onChange"
  >
    <div
      class="list-group-item"
      v-for="(field, i) in fields"
      :key="i"
      @click="onFieldComponentClick(i, field)"
    >
    
      <component
        :is="field.discriminator"
        :field="field"
        :index="i"
        :key="i"
        @change="onComponentChange">
      </component>
      <div class="components-setting-btn" v-if="i == activeIndex">
        <el-button type="danger" size="small" icon="el-icon-delete" circle @click.stop="deleteList(i)"></el-button>
      </div>
    </div>
    <!-- <div class="list-group-item" v-for="(formItm, formIndex) in list" :key="formIndex + '_form'" @click="editIndex = formIndex; setChange(formIndex)">
      <form-components :class="{isActive: editIndex == formIndex}" :formItm="formItm" :formType="formItm.type" :formIndex="formIndex"></form-components>
      
      <div class="components-setting-btn" v-if="editIndex == formIndex">
        <el-button type="danger" size="small" icon="el-icon-delete" circle @click.stop="deleteList(formIndex)"></el-button>
      </div>
    </div> -->
    <div class="no-list" v-if="fields.length == 0">拖 拽 区</div>
  </draggable>
</div>
</template>
<script>
import draggable from "vuedraggable";

import RichText from '../formComponent/components/RichEditor'
import { editors } from '../fields/index'

export default {
  props: {
    id: {
      type: Number,
      default: 0
    },
    form: {
      type: Object
    },
    fields: {

    }
  },
  data() {
    return {
      title: '',
      description: '',
      activeIndex: -1,
    }
  },
  components: {
    draggable,
    RichText,
    ...editors
  },
  async created() {
    this.title = this.form.title;
    this.description = this.form.description;
  },
  methods: {
    onTitleChange(text) {
      this.$emit('change', 'titleChange', text);
    },

    onDescriptionChange(text) {
      this.$emit('change', 'descriptionChange', text);
    },
    onComponentChange(field) {
      this.$emit('change', 'fieldChange', field);
    },
    onFieldComponentClick(index, field) {
      this.activeIndex = index;

      this.$emit('field-component-active', field);
    },
    onAdd(/*newIndex, element*/) {
      
    },
    onChange(e) {
      if (e.added) {
        e.added.element.viewId = Math.random();
      }
      this.$emit('fields-change', this.fields, e);
    },
    deleteList(index) {
      this.$confirm('此操作将删除该选项, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.fields.splice(index, 1)
          // this.$emit('field-component-active', null);
        })
    },
  },
  watch: {
    form() {
      this.title = this.form.title;
      this.description = this.form.description;
    }
  }
}
</script>