<template>
  <div class="form-components">
    <form-input :formIndex="formIndex" v-if="formType == 'input'"></form-input>
    <form-text-area :formIndex="formIndex" v-if="formType == 'textArea'"></form-text-area>
    <form-select :formIndex="formIndex" v-if="formType == 'select'"></form-select>
    <form-multi-select :formIndex="formIndex" v-if="formType == 'multiSelect'"></form-multi-select>
    <divide :formIndex="formIndex" v-if="formType == 'divideLine'"></divide>
    <form-editor :formIndex="formIndex" v-if="formType == 'editor'"></form-editor>
  </div>
</template>

<script>
import formInput from "./components/input/inpu";
import formTextArea from './components/textArea/textArea'
import formSelect from './components/select/select'
import formMultiSelect from './components/multiSelect/multiSelect'
import divide from './components/divide/divide'
import formEditor from './components/editor/editor'
export default {
  name: "clone",
  components: {
    "form-input": formInput,
    'form-text-area': formTextArea,
    'form-select': formSelect,
    'form-multi-select': formMultiSelect,
    'divide': divide,
    'form-editor': formEditor,
  },
  data() {
    return {};
  },
  methods: {},
  mounted() {},
  props: ['formType', 'formIndex']
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
