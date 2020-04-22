<template>
  <div>
    <!--
    <div v-if="!field.multiple">
      <el-radio
        v-for="(option, optionIndex) in field.options"
        :key="optionIndex"
        :label="option.label"
        v-model="field.checkedOption"
        @change="onRadioChange($event)"
        >
      </el-radio>
    </div>
    <div v-if="field.multiple">
      <el-checkbox
        v-for="(option, optionIndex) in field.options"
        :key="`${field.viewId}${optionIndex}`"
        :label="option.label"
        v-model="option.checked"
      >
      </el-checkbox>
    </div>
    -->
    <el-radio
      v-if="type === 'radio'"
      :label="option.label"
      v-model="value"
      @change="$emit('change', $event)"
      >
    </el-radio>
    <el-checkbox
      v-if="type === 'checkbox'"
      :label="option.label"
      v-model="option.checked"
    >
    </el-checkbox>
    <el-input style="width: 200px;" size="mini" v-if="option.editable" v-model="option.text"></el-input>
  </div>
</template>
<script>
export default {
  data() {
    return {
      value: false,
    }
  },
  props: {
    option: {
    },
    type: {}
  }
}
</script>