<template>
  <div class="right-aside">
    <div v-for="(section, i) in sections" :key="i">
      <div class="title-name">{{section.label}}</div>
      <component
        v-for="(attribute, i) in attributes[section.key]"
        :key="i" :is="attribute"
        :value="attributeValues[attribute.key]" 
        @input="onInput(attribute, $event)">
      </component>
    </div>
  </div>
</template>
<script>
import * as attributeComponents from './../../../cp/form/field/attributes'
import allFieldMetas from './../../../fields/index'
import { view, remote } from './FieldAttributePanelView'

export default {
  props: {
    field: {
      type: Object
    }
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
      ],
      attributes: {
      },
      attributeValues: {
      }
    }
  },
  components: {
    ...attributeComponents
  },
  created() {
    
  },
  methods: {
    onInput(attribute, value) {
      console.debug('FieldAttributePanel: attribute is ' + attribute.key);
      console.debug(value)
      this.attributeValues[attribute.key] = value;
      this.$emit('input', this.attributeValues, attribute, value);
      // remote(this.field, value);
    },
    fieldToAttributeValues(field, meta) {
      console.log('fieldToAttributeValues')
      this.attributeValues = view(field, meta)
    },
    getAttributeValue(key) {
      if (!this.attributeValues) {
        console.log("attribute values is empty");
        return null;
      }

      if (this.attributeValues[key]) {
        return this.attributeValues[key];
      }
    }
  },
  watch: {
    field() {
      if (!this.field) {
        return;
      }
      console.log("AttributePanel: field changed");
      const meta = allFieldMetas[this.field.discriminator];
      this.fieldToAttributeValues(this.field, meta);
      this.attributes = meta.attributes
    }
  }
}
</script>

<style lang="scss">
  @import "./FieldAttributePanel.scss";
</style>
