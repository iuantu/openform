<template>
    <div>
        <el-tabs v-model="activeName" @tab-click="onClick">
            <el-tab-pane label="概述" name="summary">
                <FormSummary />
            </el-tab-pane>
            <el-tab-pane label="编辑" name="edit">编辑</el-tab-pane>
            <el-tab-pane label="数据" name="data">数据</el-tab-pane>
            <el-tab-pane label="报表" name="reporter">报表</el-tab-pane>
            <el-tab-pane label="发布" name="publish">发布</el-tab-pane>
            <el-tab-pane label="协作" name="collaboration">协作</el-tab-pane>
        </el-tabs>
        <!-- TODO: 使用路由试图代替 -->
        <!-- <router-view></router-view> -->
    </div>
</template>
<script>
import FormSummary from './FormSummary'

export default {
    data() {
        return {
            activeName: 'edit',
        }
    },
    methods: {
        onClick() {

        },
    },
    
    components: {
        FormSummary,
    }
}
</script>