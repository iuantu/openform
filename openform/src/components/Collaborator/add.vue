<template>
  <el-dialog
          width="40%"
          title="添加协作者"
          :visible.sync="showDialog"
          @open="getData"
          @closed="closed"
          @close="close"
  >
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="协作者">
        <el-select
                v-model="form.name"
                filterable
                remote
                reserve-keyword
                placeholder="邮箱、手机号、用户名"
                :remote-method="remoteMethod"
                :loading="loading">
          <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="身份">
        <el-select v-model="form.status" placeholder="请选择活动区域">
          <el-option label="编辑" :value="0"></el-option>
          <el-option label="查看" :value="1"></el-option>
          <el-option label="管理" :value="2"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">添加</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>
  export default {
    data() {
      return {
        showDialog: false,
        options: [],
        value: [],
        list: [],
        loading: false,
        form: {
          name: '',
          status: 0
        },
        states: ["Alabama", "Alaska", "Arizona",
          "Arkansas", "California", "Colorado",
          "Connecticut", "Delaware", "Florida",
          "Georgia", "Hawaii", "Idaho", "Illinois",
          "Indiana", "Iowa", "Kansas", "Kentucky",
          "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Minnesota",
          "Mississippi", "Missouri", "Montana",
          "Nebraska", "Nevada", "New Hampshire",
          "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio",
          "Oklahoma", "Oregon", "Pennsylvania",
          "Rhode Island", "South Carolina",
          "South Dakota", "Tennessee", "Texas",
          "Utah", "Vermont", "Virginia",
          "Washington", "West Virginia", "Wisconsin",
          "Wyoming"]
      }
    },
    mounted() {
      this.list = this.states.map(item => {
        return { value: `value:${item}`, label: `label:${item}` };
      });
    },
    methods: {
      show() {
        this.showDialog = true
      },
      closed() {
      },
      close() {
        this.showDialog = false
      },
      getData() {

      },
      changHandle() {

      },
      onSubmit() {

      },
      remoteMethod(query) {
        if (query !== '') {
          this.loading = true;
          setTimeout(() => {
            this.loading = false;
            this.options = this.list.filter(item => {
              return item.label.toLowerCase()
                .indexOf(query.toLowerCase()) > -1;
            });
          }, 200);
        } else {
          this.options = [];
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
</style>
