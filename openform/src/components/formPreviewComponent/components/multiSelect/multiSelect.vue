<template>
    <div class="form-detail-content" :style="{width: formItm.width}">
        <div class="form-title" :style="{textAlign: formItm.alignType}">
            {{formItm.name}}
            <span class="form-require" v-if="formItm.isRequired">*</span>
        </div>
        <div class="form-subtitle" :style="{textAlign: formItm.alignType}">{{formItm.subTitle}}</div>
        <div class="select-opts">
            <el-checkbox-group v-model="select">
                <el-checkbox v-for="(checkItm, checkIndex) in formItm.options" :key="checkIndex + '_checkbox'" :label="checkItm.label">
                {{checkItm.value}}
                </el-checkbox>
            </el-checkbox-group>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return {
            select: []
        }
    },
  props: ['formIndex', 'formItm']
}
</script>
<style lang="scss">

</style>