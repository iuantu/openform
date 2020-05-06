<template>
  <el-row>
    <el-col>
      <DataTable v-bind:values="values" v-bind:columns="columns" />
    </el-col>
  </el-row>
</template>
<script>
import DataTable from '../DataTable'
import { loadForFormSummary } from '../../../service/form'
import { mapState, mapActions } from 'vuex'

export default {
  props: {
    id: {
      type: Number,
      default: 1,
    }
  },
  components: {
    DataTable
  },

  data() {
    return {
    }
  },

  async created() {
    await this.load({
      formId: this.$route.params.id,
      page: 1,
    })
  },

  computed: {
    ...mapState('row', ['rows', 'columns', 'form']),
    ...mapActions('row', ['load']),
  }
}
</script>