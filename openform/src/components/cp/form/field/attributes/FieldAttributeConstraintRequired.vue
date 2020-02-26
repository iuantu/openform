<template>
  <div class="input-textarea">
    <el-checkbox class="required-checkbox" v-model="enabled" @change="onChange">必填项</el-checkbox>
    <div class="commands">
      必填项的数据如果没有填写会提示错误
    </div>
  </div>
</template>
<script>
export default {
  key: 'required_constraint',
  props: {
    value: {
      type: Object
    }
  },
  data() {
    return {
      enabled: false,
    }
  },
  methods: {
    onChange(e) {
      this.$emit('input', { 'enabled': e });
    },
    bind() {
      if (!this.value) {
        this.enabled = false;
        return;
      }
      this.enabled = this.value.enabled;
    }
  },
  created() {
    this.bind();
  },
  watch: {
    value() {
      this.bind();
    }
  }
}
</script>

        