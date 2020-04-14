<template>
  <div class="right-aside">
    <div
      v-for="(section, i) in sections"
      :key="i"
      v-show="attributes[section.key] && attributes[section.key].length > 0"
    >

      <div class="title-name">{{section.label}}</div>
      <component
        v-for="(attribute, i) in attributes[section.key]"
        :key="i"
        :is="attribute instanceof Array ? attribute[0] : attribute"
        :config="attribute instanceof Array ? attribute[1] : null"
        :meta="meta"
        :field="field"
        :value="attributeValues[attribute.key]"
        @input="onInput(attribute, $event)">
      </component>
    </div>
  </div>
</template>
<script>
import * as attributeComponents from './../../../cp/form/field/attributes'

export default {
  props: {
    attributes: {
      type: Object
    },
    attributeValues: {
      type: Object,
    },
    meta: {
      type: Object,
    },
    field: {
      type: Object,
    },
  },
  data() {
    return {
      sections: [
        {
          label: '基本设置',
          key: 'basic'
        },
        {
          label: '数据校验',
          key: 'validation',
        },
      ]
    }
  },
  components: {
    ...attributeComponents
  },
  created() {
    
  },
  methods: {
    onInput(attribute, value) {
      this.attributeValues[attribute.key] = value;
      this.$emit('input', this.attributeValues, attribute, value);
    },
  },
}
</script>

<style lang="scss">
  @import "./FieldAttributePanel.scss";
</style>
