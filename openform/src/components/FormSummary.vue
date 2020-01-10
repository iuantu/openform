<template>
  <el-row type="flex" v-loading="!isFetched">
    <el-col v-if="isFetched">
      <el-row>
        <div class="form-analysis-info">
          <div class="analysis">
            <div class="analysis-summary clearfix">
              <dl class="float-left">
                <dt>全部数据</dt>
                <dd>{{submit_count}}</dd>
              </dl>
              <dl class="float-left">
                <dt>今日数据</dt>
                <dd>{{submit_count_today}}</dd>
              </dl>
              <dl class="float-left">
                <dt>今日浏览</dt>
                <dd>{{reads_today}}</dd>
              </dl>
            </div>
            <div class="analysis-chart">
              <div ref="month" style="width: 100%; height: 400px;"></div>
            </div>
          </div>
          <div class="form-info">
            <div class="form-info-inner">
              <div class="form-info-heading">创建时间</div>
              <div class="form-info-content">{{form.created_at}}</div>
              <div class="form-info-heading">每分钟提交</div>
              <div class="form-info-content">
                <div ref="minute" class="minute"></div>
              </div>
              <div class="form-info-content">
                <a class="button" href="#" @click="onClickExport">下载CSV</a>
              </div>
            </div>
          </div>
        </div>
      </el-row>
      <el-row>
        <el-col>
          <el-table :data="values" style="width: 100%;">
            <el-table-column
              v-for="(column, key) in columns"
              :key="key"
              :prop="column.property"
              :label="column.label"
              width="180">
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
        </el-col>
      </el-row>
    </el-col>
  </el-row>
</template>
<style scoped>
.minute {
  width: 140%;
  height: 220px;
  margin-left: -50px;
  margin-top: -50px;
}

.form-info-content .button {
  padding: 10px;
  background-color: #4C89EF;
  color: #FFF;
}

.form-analysis-info {
  overflow: hidden;
  position: relative;
  width: 100%;
}

.form-info {
  float: right;
  width: 283px;
  height: 98.5%;
  background-color: #3374E0;
  position: absolute;
  left: 660px;
  top: 0px;
  border: 1px solid #EBEEF5;
  box-shadow: 0px 2px 4px 0px #EEEEEE;
}

.form-info-inner {
  margin: 24px;
}

.form-info-heading {
  color: #FFF;
  font-weight: bold;
  font-size: 14px;
  line-height: 40px;
}

.form-info-content {
  color: #FFF;
  font-size: 14px;
}

.analysis {
  width: 644px;
  height: 492px;
  margin-bottom: 10px;
  box-shadow: 0px 2px 4px #EEEEEE;
  float: left;
}

.analysis-chart {
  height: 334px;
  width: 100%;
  margin-bottom: 30px;
}

.analysis-summary {
  height: 30px;
  padding: 20px;
}

.analysis-summary dl {
  margin: 10px;
  padding: 0px;
  font-weight: bold;
  float: left;
}

.analysis-summary dt {
  padding: 10px 0px 10px 0px;
}
</style>
<script>
import moment from 'moment'
import echarts from 'echarts'
import { ofFetch, baseURL } from '../functions'

export default {
  data() {
    return {
      values: [],
      columns: [],
      form: {},
      read_count_by_days: [],
      reads_today: 0,
      submit_count: 0,
      submit_count_by_days: [],
      submit_count_by_mintes: [],
      submit_count_today: 0,
      isFetched: false,
      baseURL: baseURL,
    }
  },

  async created() {
    let response = await ofFetch(`/api/v1/form/${this.$route.params.id}`);
    let data = await response.json();
    this.form = data;

    let val_res = await ofFetch(`/api/v1/cp/value/${this.$route.params.id}`);
    let val = await val_res.json();

    const valueColumns = data.fields.map((column) => {
      return {
        property: new String(column.id),
        label: column.title,
        width: "*",
      }
    });

    const systemColumns = [
      {
        property: 'sequence',
        label: '序号',
        width: '10',
      },
      {
        property: 'created_at',
        label: '创建时间',
        width: '100',
      },
      {
        property: 'updated_at',
        label: '更新时间',
        width: '100',
      },
    ];
    this.columns = [...systemColumns, ...valueColumns];

    const fieldsMapping = {}
    data.fields.forEach((field) => {
      fieldsMapping[field.id] = field;
    })

    this.values = val.data.map((v) => {
      const row = {};
      for (const field of data.fields) {
        const fieldValue = v.values[field.id];
        
        row[field.id] = this.fieldValue(field, fieldValue)
        row.sequence = v.sequence;
        row.created_at = v.created_at;
        row.updated_at = v.updated_at;
      }
      return row;
    });
    

    let summary_response = await ofFetch(`/api/v1/cp/form/${this.$route.params.id}/summary`)
    let summary = await summary_response.json();

    this.read_count_by_days = this.createCountByDays(summary.read_count_by_days);
    this.reads_today = summary.reads_today;
    this.submit_count = summary.submit_count;
    this.submit_count_by_days = this.createCountByDays(summary.submit_count_by_days);
    this.submit_count_by_mintes = this.createCountByMinutes(summary.submit_count_by_mintes);
    this.submit_count_today = summary.submit_count_today;

    this.isFetched = true;
    setTimeout(() => {
      this.initMonthChart();
      this.initMinuteChart();
    }, 500);
    
  },

  mounted() {
  },

  methods: {
    initMonthChart() {
      const chart = echarts.init(this.$refs.month);
      const option = {
          xAxis: {
              type: 'category',
              data: this.submit_count_by_days.labels
          },
          yAxis: {
              type: 'value'
          },
          series: [
            {
              data: this.submit_count_by_days.count,
              type: 'line'
            },
            {
              data: this.read_count_by_days.count,
              type: 'line',
              smooth: false,
              itemStyle: {
                normal: {
                  lineStyle: {
                    width: 2,
                    type:'dotted',
                  }
                }
              }
            }
          ],
      };

      chart.setOption(option, true);
    },

    initMinuteChart() {
      const chart = echarts.init(this.$refs.minute);
      const minutes = []
      for (let i = 0; i < 24; i++) {
        minutes.push('');
      }
      const option = {
        xAxis: {
          data: minutes,
          axisLabel: {
              inside: false,
              textStyle: {
                  color: '#fff'
              },
              show: false,
          },
          axisTick: {
              show: false
          },
          axisLine: {
              show: false
          },
          z: 10,
          splitLine: {
            show: false
          },
          splitArea: {
            show: false
          },
        },
        yAxis: {
          axisLine: {
            show: false,
          },
          splitLine: {
            show: false
          },
          splitArea: {
            show: false
          },
          axisTick: {
              show: false
          },
          axisLabel: {
            show: false,
            width: 0,
            padding: 0,
          }
        },
        series: [
        {
          type: 'bar',
          itemStyle: {
              color: 'rgba(0,0,0,0.0)'
          },
          barGap: '-100%',
          barCategoryGap: '30%',
          data: [],
          animation: false,
          label: {
              show: false
            },
        },
        {
          type: 'bar',
          itemStyle: {
              color: new echarts.graphic.LinearGradient(
                  0, 0, 0, 1,
                  [
                      {offset: 0, color: '#79AAFB'},
                  ]
              )
          },
          data: this.submit_count_by_mintes.count
        }
          ],
      };
      chart.setOption(option, true);
    },
    

    fieldValue(field, fieldValue) {
      if (field.discriminator == "text_field") {
        return fieldValue;
      }

      if (field.discriminator == 'select_field') {
        const options = {};
        for (const opt of field.options) {
          options[opt.value] = opt;
        }
        if (fieldValue) {
          return fieldValue.map((optValue) => {
            const opt = options[optValue.value];
            if (opt.editable) {
              const text = optValue.text || '无'
              return `${opt.label} ${text}`;
            }
            return opt.label;
          });
        }
      }

      return fieldValue;
    },

    createCountByDays(count) {
      const map = new Map();
      for (const c of count) {
        const key = `${c.year}-${c.month}-${c.day}`;
        map.set(key, c);
      }

      let start = moment().add(-8, 'days');
      const submit = [];
      const labels = [];
      for (let i = 0; i < 8; i++) {
        const m = start.add(1, 'days');
        const key = m.format("YYYY-M-D");
        labels.push(m.format("MM-DD"));
        if (map.has(key)) {
          submit.push(map.get(key).count);
        } else {
          submit.push(0);
        }
      }

      return {
        "count": submit,
        "labels": labels,
      }
    },

    createCountByMinutes(count) {
      const map = new Map();
      for (const c of count) {
        const key = `${c.minute}`;
        map.set(key, c);
      }

      let start = moment().add(-24, 'minutes');
      const submit = [];
      const labels = [];

      let max = 0;
      count.forEach((s) => {
        if (s.count > max) {
          max = s.count;
        }
      });


      for (let i = 0; i < 24; i++) {
        const m = start.add(1, 'minutes');
        const key = m.format("m");
        labels.push(m.format("m"));

        if (map.has(key)) {
          submit.push(map.get(key).count);
        } else {
          if (max > 0) {
            submit.push(max * 0.1);
          } else {
            submit.push(0);
          }
        }
      }

      return {
        "count": submit,
        "labels": labels,
      }
    },

    async onClickExport() {
      let exportResponse = await ofFetch(`/api/v1/cp/form/${this.$route.params.id}/export`)
      let e = await exportResponse.text();

      var element = document.createElement('a');
      element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(e));
      element.setAttribute('download', 'export.csv');

      element.style.display = 'none';
      document.body.appendChild(element);

      element.click();

      document.body.removeChild(element);
    }
  },
}
</script>