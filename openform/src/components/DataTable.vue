<template>
  <el-table 
    border
    :data="values"
    @row-click="onRowClick"
    style="width: 99.9%;"
  >
    <el-table-column
      v-for="(column, key) in columns"
      :key="key"
      :prop="column.property"
      :label="column.label">
      <template slot-scope="scope">
        <div v-if="!Array.isArray(scope.row[scope.column.property])">{{scope.row[scope.column.property]}}</div>
        <div v-if="Array.isArray(scope.row[scope.column.property])">
          <ul>
            <li v-for="(value, key) in scope.row[scope.column.property]" :key="key">{{value}}</li>
          </ul>
        </div>
      </template>
    </el-table-column>
  </el-table>
</template>
<script>
export default {
  props: {
    columns: {
      type: Array,
      default() {
        return [];
      },
      required: true
    },
    values: {
      type: Array,
      default() {
        return [];
      },
      required: true
    }
  },
  methods: {
    onRowClick(row) {
      console.log(row)
    }
  }
}
</script>