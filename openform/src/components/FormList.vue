<template>
  <div>
    <el-row type="flex">
      <el-col>
        <el-button round size="medium">创建表单</el-button>
      </el-col>
    </el-row>
    <el-row type="flex">
      <el-col>
        <el-table
          :data="forms"
          style="width: 100%">
          <el-table-column
            prop="title"
            label="名字"
            width="*">
            <template slot-scope="scope">
              <router-link :to="{ name: 'cp_form_summary', params: { id: scope.row.id } }">{{scope.row.title}}</router-link>
            </template>
          </el-table-column>
          <el-table-column
            prop="name"
            label="数据"
            width="50">
          </el-table-column>
          <el-table-column
            prop="address"
            width="100"
            label="状态">
          </el-table-column>
          <el-table-column
            prop="address"
            width="100"
            label="创建时间">
          </el-table-column>
          <el-table-column
            prop="address"
            width="100"
            label="操作">
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { ofFetch } from '../functions'
export default {
  data() {
    return {
      forms: [],
    }
  },
  async created() {
    const response = await ofFetch('/api/v1/cp/form')
    const forms = await response.json()
    this.forms = forms.map((form) => {
      return {
        id: form.id,
        title: form.title,
        created_at: form.created_at
      }
    })
  }
}
</script>