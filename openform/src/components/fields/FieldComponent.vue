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
    <div class="errors" v-if="field.has_error">
      <ul>
        <li
          v-for="(error, idx) in field.errors "
          :key="field.id + '_' + idx">
          {{error}}
        </li>
      </ul>
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
      for (const constraint of this.field.constraints) {
        if (constraint.discriminator === "required_constraint") {
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

ul, li {
  margin: 0px;
  padding: 0;
}

ul {
  margin-left: 20px;
  line-height: 30px;
}

.errors {
  margin: 0px;
  color: darkred;
}
</style>