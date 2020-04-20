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
        @change="onComponentChange">
      </component>
    </div>
  </div>
</template>
<script>
import { components as fieldComponents } from './fields/index'
export default {
  props: {
    fields: {
      // type: Array
    }
  },
  components: {
    ...fieldComponents
  },
  methods: {
    onComponentChange() {

    }
  }
}
</script>