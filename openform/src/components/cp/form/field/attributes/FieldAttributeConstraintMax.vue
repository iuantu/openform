<template>
  <div class="input-textarea">
    <el-checkbox v-model="enabled" class="required-checkbox" @change="onCheckboxChange"></el-checkbox>
    <div class="checkbox-right">
      最多填
      <el-input v-model="max" type="number" size="mini" @input="onChange"></el-input>
      个字
    </div>
  </div>
</template>
<script>
export default {
  key: 'max_constraint',
  props: {
    value: {
      type: Object
    }
  },
  data() {
    return {
      enabled: false,
      max: null,
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
        max: parseInt(this.max),
      })
    },
    bind() {
      if (this.value) {
        this.enabled = this.value.enabled;
        this.max = this.value.max;
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

        