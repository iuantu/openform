<template>
  <field-component :field="field" :index="index">
    <option-editor
      v-for="(option, optionIndex) in field.options"
      :key="index + '_' + optionIndex"
      :option="option"
      :type="field.type"
      @change="onRadioChange($event)">
    </option-editor>
  </field-component>
</template>

<script>
import FieldComponent from '../FieldComponent';
import OptionEditor from './OptionEditor';

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
          options: [],
          constraints: [],
          checkedOption: null,
        }
      }
    },
    index: {
      type: Number
    }
  },
  methods: {
    onRadioChange(label) {
      this.field.options.forEach((option) => {
        if (option.label === label) {
          this.field.checkedOptionValue = option.value;
        }
      })
    }
  },
  computed: {
    selectDescription() {
      let hasMin, hasMax, min, max;
      for (const constraint of this.field.constraints) {
        if (constraint.discriminator == "min_constraint") {
          hasMin = true;
          min = constraint.min;
        } else if (constraint.discriminator == "max_constraint") {
          hasMax = true;
          max = constraint.max;
        }
      }

      if (hasMin && ! hasMax) {
        return `最少选${min}项`;
      } else if (!hasMin && hasMax) {
        return `最多选${max}项`;
      } else {
        return `选${min}~${max}项`;
      }
    }
  },
  components: {
    FieldComponent,
    OptionEditor,
  }
};
</script>