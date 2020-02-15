<template>
    <div class="form-detail-content" :style="{width: formItm.width}">
        <div class="form-title" :style="{textAlign: formItm.alignType}">
            {{formItm.name}}
            <span class="form-require" v-if="formItm.isRequired">*</span>
        </div>
        <div class="form-subtitle" :style="{textAlign: formItm.alignType}">{{formItm.subTitle}}</div>
        <div class="select-opts">
            <el-radio-group size="small">
                <el-radio v-for="(optItm, optIndex) in formItm.options" :key="optIndex + '_opts'" :label="optItm.label">{{optItm.value}}</el-radio>
            </el-radio-group>
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