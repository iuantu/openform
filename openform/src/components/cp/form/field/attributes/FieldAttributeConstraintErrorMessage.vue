

<template>
  <div class="input-textarea">
    <el-checkbox class="required-checkbox" v-model="enabled" @change="onCheckedChange">自定义错误提示</el-checkbox>
    <el-input class="mt-10" v-model="error_message" size="small" @input="onChange"></el-input>
  </div>
</template>
<script>
export default {
  key: 'error_message',
  props: {
    value: {
      type: Object
    },
  },
  data() {
    return {
      enabled: false,
      error_message: '',
    }
  },
  created() {
    this.bind();
  },
  methods: {
    onCheckedChange() {
      this.dispatchEvent();
    },
    onChange() {
      this.dispatchEvent();
    },
    bind() {
      if (this.value) {
        this.enabled = this.value.error_message_enabled;
        this.error_message = this.value.error_message;
      }
    },
    dispatchEvent() {
      this.$emit('input', {
        error_message_enabled: this.enabled,
        error_message: this.error_message,
      });
    },
  },
  watch: {
    value() {
      this.bind();
    }
  }
}
</script>