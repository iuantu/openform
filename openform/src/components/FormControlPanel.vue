<template>
  <el-row type="flex" justify="center">
    <el-col :md="16">
      <el-row type="flex" justify="center">
        <el-col :md="10">
          <el-tabs class="tabs" v-model="$route.name" @tab-click="onClick">
            <el-tab-pane v-for="(option, key) in options" :key="key" :label="option.label" :name="option.name"></el-tab-pane>
          </el-tabs>
        </el-col>
      </el-row>
      <el-row type="flex">
        <el-col>
          <router-view></router-view>
        </el-col>
      </el-row>

    </el-col>
  </el-row>
</template>
<style scoped>
  .tabs {
    margin: 50px 0px 50px 0px;
  }
</style>
<script>
export default {
  data() {
    return {
      activeName: 'cp_form_summary',
      options: [
        {
          label: '概述',
          name: 'cp_form_summary'
        },
        {
          label: "编辑",
          name: "cp_form_edit"
        },
        {
          label: "数据",
          name: "cp_data_form"
        },
        {
          label: "报表",
          name: "cp_report_form"
        },
        {
          label: "发布",
          name: "cp_publish_form"
        },
        {
          label: "协作",
          name: "cp_collaborator_form"
        }
      ]
    }
  },
  methods: {
    onClick(tab) {
      this.$router.replace({name: tab.name});
    },
  },
}
</script>
