<template>
  <div class="field">
    <div class="field-title">
      {{field.title}}
      <span class="field-required" v-if="isRequired">*</span>
    </div>
    <div class="field-description" v-html="field.description"></div>
    <div class="field-component">
      <slot></slot>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    field: {
      type: Object,
      default() {
        return {
          title: '',
          readonly: false,
          description: '',
          placeholder: '',
          constraints: []
        }
      }
    },
    index: {
      type: Number
    }
  },
  computed: {
    isRequired() {
        console.log(this.field)
      for (const constraint of this.field.constraints) {
        if (constraint.discriminator == "required_constraint") {
          return true;
        }
      }
      return false;
    }
  },
}
</script>
<style scoped>
.field {
  margin-bottom: 30px;
}

.field-title {
  font-weight: bold;
  line-height: 200%;
}
</style>