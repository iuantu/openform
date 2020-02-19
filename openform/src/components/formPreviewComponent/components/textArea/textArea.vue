<template>
    <div class="form-detail-content" :style="{width: formItm.width}">
        <div class="form-title" :style="{textAlign: formItm.alignType}">
            {{formItm.name}}
            <span class="form-require" v-if="formItm.isRequired">*</span>
        </div>
        <div class="form-subtitle" :style="{textAlign: formItm.alignType}">{{formItm.subTitle}}</div>
        <div class="area-texts">
            <el-input size="small" type="textarea" :placeholder="formItm.placeholder" :rows="formItm.textareaRows"></el-input>
        </div>
    </div>
</template>
<script>
export default {
  props: ['formIndex', 'formItm']
}
</script>
<style lang="scss">

</style>