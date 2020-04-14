<template>
  <div>
    <div class="right-title">描述</div>
      <div class="input-style">
        <el-input v-model="textValue" placeholder="请输入你的描述" @change="onChange"></el-input>
      </div>
  </div>
</template>
<script>
export default {
  key: 'description',
  props: {
    value: {
      type: String
    }
  },
  data() {
    return {
      textValue: '',
    }
  },
  created() {
    this.textValue = this.value;
  },
  methods: {
    onChange(e) {
      this.$emit('input', e);
    }
  },
  watch: {
    value() {
      this.textValue = this.value;
    }
  }
}
</script>