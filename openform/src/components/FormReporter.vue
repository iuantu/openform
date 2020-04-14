<template>
  <el-row>
    <el-col>
      <div style="margin: 40px 0px;" v-for="fieldReporter in reporter" v-bind:key="fieldReporter.key">
        <h3 style="line-height: 60px;">{{fieldReporter.title}}</h3>
        <el-table
          :data="fieldReporter.counter"
          style="width: 100%">
          <el-table-column
            prop="option"
            label="选项"
            width="*">
            <template slot-scope="scope">
              <span style="">{{ scope.row.option }}</span>
              <div style="height: 25px;" :style="a(scope)"></div>
            </template>
          </el-table-column>
          <el-table-column
            prop="count"
            label="数据量"
            width="70">
          </el-table-column>
          <el-table-column
            prop="percent"
            label="占比"
            width="70">
          </el-table-column>
        </el-table>
      </div>
    </el-col>
  </el-row>
</template>
<script>
import { loadFormAnalysis, loadForm } from './service/form'

export default {
  data() {
    return {
      id: 0,
      analysis: [],
      reporter: [],
      lines: [
        {backgroundColor: '#F14D4D', color: '#FFFFFF'},
        {backgroundColor: '#AB4DF1', color: '#FFFFFF'},
        {backgroundColor: '#F1984D', color: '#FFFFFF'}
      ]
    }
  },
  async created() {
    this.id = this.$route.params.id;
    const form = await loadForm(this.id);
    const analysis = await loadFormAnalysis(this.id);
    const analysisMap = {}
    const total = {}
    this.analysis = analysis.forEach((counter) => {
      analysisMap[counter.option_id] = counter;

      if (!total[counter.field_id]) {
        total[counter.field_id] = counter.count;
      } else {
        total[counter.field_id] += counter.count;
      }
    })

    this.reporter = form.fields.filter((field) => field.discriminator == "select_field").map((field) => {
      return {
        "key": field.id,
        "title": field.title,
        "counter": field.options.map((opt) => {
          let counter = analysisMap[opt.id];
          let t = total[opt.field_id];

          if (!counter) {
            counter = {
              option: opt.label,
              count: 0,
              percent: 0
            }
          }
          return {
            option: opt.label,
            count: counter.count,
            percent: counter.count ? counter.count / t * 100 : 0
          }
        })
      }
    })    
  },
  methods: {
    a(scope) {
      const line = this.lines[scope.$index % 3];
      const percent = scope.row.percent;

      return {
        width: (percent == 0 ? 1 : percent) + '%', 
        backgroundColor: line.backgroundColor,
        color: line.color,
      }
    }
  },
}
</script>