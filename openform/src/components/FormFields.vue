<template>
  <div>
    <div
      v-for="(field, i) in fields"
      :key="i">
      <component
        :is="field.discriminator"
        :field="field"
        :index="i"
        :key="i"
        @change="(value) => onComponentChange(field, value, i)">
      </component>
    </div>
  </div>
</template>
<script>
import { getMeta, editors } from './fields/index'

export default {
  props: {
    fields: {
      // type: Array
    }
  },
  components: {
    ...editors
  },
  created() {
  },
  methods: {
    onComponentChange(field, value, index) {
      field.value = value;
    }
  },
  computed: {
    metaFields() {
      return this.fields.map(field => getMeta(field.discriminator));
    }
  }
}
</script>