<template>
    <div class="form-detail-content">
        <div class="form-title">
            {{field.title}}
            <span class="form-require" v-if="field.constraints.isRequired">*</span>
        </div>
        <div class="form-subtitle">{{field.description}}</div>
        <div class="area-texts">
            <el-input size="small" :placeholder="field.placeholder" :disabled="field.readonly"></el-input>
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
          constraints: {
            isRequired: false
          }
        }
      }
    }
  },
  created() {
    console.log("TextField created");
  }
}
</script>