<template>
  <div class="form-list">
    <div class="list-content">
      <div class="add-new">
          <el-button type="primary" round @click="addNew(false)">创建表单</el-button>
      </div>
      <el-table border size="small" :data="formList">
        <el-table-column label="名字" prop="title"></el-table-column>
        <el-table-column label="数据" prop="record_count" width="90px"></el-table-column>
        <el-table-column label="状态" prop="" width="100px">
          <template slot-scope="scope">
            <el-switch size="small" v-model="formList[scope.$index].version"></el-switch>
          </template>
        </el-table-column>
        <el-table-column label="创建时间" prop="created_at" width="120px">
          <template slot-scope="scope">
            {{getTime(formList[scope.$index].created_at)}}
          </template>
        </el-table-column>
        <el-table-column label="Zip code" prop="" width="160px"></el-table-column>
        <el-table-column label="操作" width="100px">
            <template slot-scope="scope">
                <el-button type="text" size="small" @click="addNew(formList[scope.$index].id)">修改</el-button>
                <el-button type="text" size="small" @click="remove(formList[scope.$index].id)"><span class="color-red">删除</span></el-button>
            </template>
        </el-table-column>
      </el-table>
    </div>    
  </div>
</template>
<script>
// import axios from 'axios'
import { SecurityService } from '../../functions';
import moment from 'moment'
export default {
  data() {
    return {
      formList: [],
    }
  },
  methods: {
    getFormLists(){
        this.service.getApi('cp/form/').then(({data})=>{
            this.formList = data
        })
    },
    addNew(isId){
        let _que = {}
        if(isId){
            _que = {id: isId}
        }
        this.$router.push({
            path: '/openform',
            query: _que
        })
    },
    remove(id){
        this.$confirm('此操作将永久删除该表单, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
            // this.deleteForm(id)
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        })
    },
    // deleteForm(id){
    //     this.service.
    // },
    getTime(time){
      return moment(time).format('DD-MM-YYYY')
    }
  },

  created() {
    this.service = new SecurityService();
  },
  mounted(){
      this.getFormLists()
  }
}
</script>
<style lang="scss">
@import "./css/index.scss";
</style>