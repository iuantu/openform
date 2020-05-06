<template>
  <el-table 
    border
    :data="values"
    @row-click="value => $emit('row-click', value)"
    style="width: 99.9%;"
  >
    <el-table-column
      v-for="(column, key) in columns"
      :key="key"
      :width="column.width"
      :prop="column.property"
      :label="column.label">
      <template slot-scope="scope">
        <div v-if="!isComponent(scope)">{{scope.row[scope.column.property]}}</div>
        <component
          v-if="isComponent(scope)"
          :is="getField(scope.column.property).discriminator"
          :field="getField(scope.column.property)"
          :value="scope.row[scope.column.property]">
        </component>

      </template>
    </el-table-column>
  </el-table>
</template>
<script>
import { list } from "../../fields";

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
    },
    fields: {
      type: Array,
      default() {
        return []
      }
    },
  },
  components: {
    ...list
  },
  methods: {
    getField(id) {
      for (const field of this.fields) {
        if (String(field.id) === id) {
          return field;
        }
      }
    },
    isComponent(scope) {
      const isComponent = (['sequence', 'created_at', 'updated_at'].indexOf(scope.column.property)) < 0;
      return isComponent;
    },
  }
}
</script>