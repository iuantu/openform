<template>
  <div class="input-textarea">
    <el-checkbox v-model="enabled" class="required-checkbox" @change="onCheckboxChange"></el-checkbox>
    <div class="checkbox-right">
      {{config ? config[0] : '最少填'}}
      <el-input v-model="min" type="number" size="mini" @input="onChange"></el-input>
      {{config ? config[1] : '字'}}
    </div>
  </div>
</template>
<script>
export default {
  key: 'min_constraint',
  props: {
    value: {
      type: Object
    },
    config: {
      type: Array 
    }
  },
  data() {
    return {
      enabled: false,
      min: null,
    }
  },
  created() {
    this.bind();
  },
  methods: {
    onCheckboxChange() {
      this.dispatchEvent();
    },
    onChange() {
      this.dispatchEvent();
    },
    dispatchEvent() {
      this.$emit('input', {
        enabled: this.enabled,
        min: this.min,
      })
    },
    bind() {
      if (this.value) {
        this.enabled = this.value.enabled;
        this.min = this.value.min;
      }
    }
  },
  watch: {
    value() {
      this.bind();
    }
  }
}
</script>

        