<template>
  <div class="report-form">
    <div v-for="(item, index) in formData" :key="index" class="report-form-item">
      <div class="report-form-chart">
        <div class="report-form-title">{{ item.name }}</div>
        <div v-for="(pItem, pIndex) in item.list" :key="pIndex" class="proportion">
          <div
                  class="proportion-line"
                  :style="{width: pItem.proportion, 'background-color': pIndex === 0 ? '#F14D4D' : pIndex === 1 ? '#AB4DF1' : ''}"
          >
          </div>
        </div>
      </div>
      <div class="report-form-table">
        <el-table
                :data="item.list"
                style="width: 100%;margin-top: 40px;"
        >
          <el-table-column prop="label" align="left" label="选项" />
          <el-table-column prop="count" align="left" label="数据量" />
          <el-table-column prop="proportion" align="left" width="100" label="占比" />
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        formData: [
          {
            name: '你使用最多的编程语言是什么？',
            list: [
              {
                label: 'Python',
                count: 1000,
                proportion: '100%'
              },
              {
                label: 'Java',
                count: 800,
                proportion: '80%'
              },
              {
                label: 'GoLang',
                count: 500,
                proportion: '50%'
              },
              {
                label: 'PHP',
                count: 500,
                proportion: '50%'
              },
            ]
          },
          {
            name: '你使用最多的编程语言是什么？',
            list: [
              {
                label: 'Python',
                count: 1000,
                proportion: '100%'
              },
              {
                label: 'Java',
                count: 800,
                proportion: '80%'
              },
              {
                label: 'GoLang',
                count: 500,
                proportion: '50%'
              },
              {
                label: 'PHP',
                count: 500,
                proportion: '50%'
              },
            ]
          }
        ]
      }
    }
  }
</script>

<style lang="scss" scoped>
.report-form {
  margin-top: 40px;
  border: 1px solid #f0f0f0;
  box-shadow: 0 1px 8px #f3f3f3;
  &-item {
    display: flex;
    border-bottom: 1px solid #f0f0f0;
    &:last-child {
      border-bottom: none;
    }
  }
  &-chart {
    flex: 2;
    padding: 30px;
    border-right: 1px solid #f0f0f0;
    .proportion {
      height: 48px;
      overflow: hidden;
      &-line {
        margin-top: 13px;
        height: 22px;
        background-color: #F1984D;
      }
    }
  }
  &-table {
    flex: 3;
    padding: 30px;
  }
  &-title {
    height: 88px;
  }
}
</style>
