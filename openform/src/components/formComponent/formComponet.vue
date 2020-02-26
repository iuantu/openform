<template>
  <div class="form-components">
    <form-title :formIndex="formIndex" :formItm="formItm" v-if="formType == 'titles'"></form-title>
    <form-input :formIndex="formIndex" :formItm="formItm" v-if="formType == 'inputs'"></form-input>
    <form-text-area :formIndex="formIndex" :formItm="formItm" v-if="formType == 'textAreas'"></form-text-area>
    <form-select :formIndex="formIndex" :formItm="formItm" v-if="formType == 'selects'"></form-select>
    <form-multi-select :formIndex="formIndex" :formItm="formItm" v-if="formType == 'multiSelects'"></form-multi-select>
    <divide :formIndex="formIndex" :formItm="formItm" v-if="formType == 'divideLines'"></divide>
    <form-editor :formIndex="formIndex" :formItm="formItm" v-if="formType == 'editors'" :selectedIndex="selectedIndex" @setFormItm='setFormItm'></form-editor>
    <description :formIndex="formIndex" :formItm="formItm" v-if="formType == 'description'"></description>
  </div>
</template>

<script>
import formInput from "./components/input/inpu";
import formTextArea from './components/textArea/textArea'
import formSelect from './components/select/select'
import formMultiSelect from './components/multiSelect/multiSelect'
import divide from './components/divide/divide'
import formEditor from './components/editor/editor'
import formTitle from './components/title/title'
import Description from './components/Description'

export default {
  name: "clone",
  components: {
    "form-input": formInput,
    'form-text-area': formTextArea,
    'form-select': formSelect,
    'form-multi-select': formMultiSelect,
    'divide': divide,
    'form-editor': formEditor,
    'form-title': formTitle,
    Description,
  },
  data() {
    return {};
  },
  methods: {
    setFormItm(params){
      this.$emit('setFormItm', params)
    }
  },
  mounted() {},
  props: ['formType', 'formIndex', 'formItm', 'selectedIndex']
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
