<template>
  <div>
    <div
      v-for="(field, i) in fields"
      :key="i">
      <h3>{{field.title}}</h3>
      <component
        :is="field.discriminator"
        :field="field"
        :value="row && row.hasOwnProperty(field.id) && row[field.id]"
        :index="i"
        :key="i">
      </component>
    </div>
  </div>
</template>
<script>
  import { details } from "../../../fields";

  export default {
    props: {
      fields: {
        // type: Array
      },
      row: {
        type: Object
      },
    },
    components: {
      ...details
    }
  }
</script>