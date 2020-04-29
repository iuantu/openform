<template>
  <div class="open-form-setting">
    <div class="formSummary">
        <el-row type="flex" justify="space-between">
            <el-col :span="16" class="summary">
                <div class="summary-data">
                    <div class="summary-data1">
                        全部数据
                        <div>{{submit_count}}</div>
                    </div>
                    <div class="summary-data1">
                        今日数据
                        <div>{{submit_count_today}}</div>
                    </div>
                    <div class="summary-data1">
                        今日浏览
                        <div>{{reads_today}}</div>
                    </div>
                </div>
                <div id="summaryData"></div>
            </el-col>
            <el-col :span="7">
                <div class="summary-detail">
                    <div class="form-info-heading">创建时间</div>
                    <div class="form-info-content">{{getTime(form.created_at)}}</div>
                    <div class="form-info-heading">每分钟提交</div>
                    <div class="form-info-content">
                        <div ref="minute" class="minute"></div>
                    </div>
                    <div class="form-info-content">
                        <el-button type="primary" plain @click="onClickExport">下载CSV</el-button>
                    </div>
                </div>
            </el-col>
        </el-row>            
    </div>
    <div class="summary-table">
        <form-summary-data :id="id"></form-summary-data>
    </div>

  </div>
</template>

<script>
import moment from 'moment'
import { SecurityService, ofFetch, baseURL } from '../../functions';
import { loadForFormSummary } from './../service/form'
import echarts from 'echarts'
import DataTable from '../cp/form/DataTable'
import FormSummaryData from '../cp/form/summary/FormSummaryData'

export default {
  name: "formSummary",
  props: {
    id: {
      type: Number,
      default: 1,
    }
  },
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
    };
  },
  methods: {
    // timeFormat(text, formatText){
    //   return moment(text).format(formatText)
    // },

    getTime(time){
      return '';
        // return this.timeFormat(time, 'YYYY年MM月DD日')
    },
    initMonthChart() {
      const chart = echarts.init(document.getElementById('summaryData'));
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
  async created(){
    // this.service = new SecurityService();
    let _id = this.$route.query.id
    if(_id){
        const { form, values, columns } = await loadForFormSummary(_id);
        this.form = form;
        this.values = values;
        this.columns = columns;

        let summary_response = await ofFetch(`/api/v1/cp/form/${_id}/summary`);
        let summary = await summary_response.json();

        this.read_count_by_days = this.createCountByDays(summary.read_count_by_days);
        this.reads_today = summary.reads_today;
        this.submit_count = summary.submit_count;
        this.submit_count_by_days = this.createCountByDays(summary.submit_count_by_days);
        this.submit_count_by_mintes = this.createCountByMinutes(summary.submit_count_by_mintes);
        this.submit_count_today = summary.submit_count_today;

        this.isFetched = true;
    }

  },
  mounted() {
    setTimeout(() => {
        this.initMonthChart();
        this.initMinuteChart();
    }, 500);
  },
  components: {
    FormSummaryData,
  },
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
