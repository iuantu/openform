<template>
  <div class="open-form-public">
    <form-preview :list="list" :title="title" :subtitle="subtitle" :showseltype="false"></form-preview>
  </div>
</template>

<script>
import FormPreView from './../../components/openform/formPreView'
import { SecurityService } from '../../functions';

export default {
  name: "openFormPublic",
  components: {
    'form-preview': FormPreView,
  },
  data() {
    return {
        list: [],
        title: '',
        subtitle: '',
    };
  },
  methods: {
    getList(){
        let _id = 16
        this.service.getApi('cp/form/' + _id).then(data=>{
            // console.log(data)
            this.title = data.title
            if(data.description){
            this.subtitle = data.description
            }
            data.fields.map(itm=>{
            let _itm = {
                name: itm.title, 
                subTitle: itm.description? itm.description: '说明', 
                width: 100, 
                isRequired: false, 
                requireText: '校验提示', 
                alignType: 'left', 
                id: itm.id,
                form_id: itm.form_id,
                constraints: itm.constraints
            }
            itm.constraints.map(requ => {
                if(requ.discriminator && requ.discriminator == 'required_constraint'){
                _itm.isRequired = true
                }
                else if(requ.discriminator && requ.discriminator == 'min_constraint'){
                _itm.isMin = true
                _itm.min = requ.min
                }
                else if(requ.discriminator && requ.discriminator == 'max_constraint'){
                _itm.isMax = true
                _itm.max = requ.max
                }
            })
            if(itm.discriminator == 'text_field' && !itm.multiple){
                _itm.type = 'inputs'
                _itm.showName = '文本字段'
                _itm.placeholder = itm.placeholder
            }
            if(itm.discriminator == "text_field" && itm.multiple){
                _itm.type = "textAreas"
                // _itm.textareaRows = itm.layout_row_index
                _itm.showName = '多行文本'
                _itm.placeholder = itm.placeholder
            }
            if(itm.discriminator == 'select_field'){
                if(itm.type == "radio"){
                _itm.type = 'selects'
                _itm.showName = '单项选择'
                }
                else if(itm.type == 'checkbox'){
                _itm.type = 'multiSelects'
                _itm.showName = '多项选择'
                }
                _itm.options = []
                itm.options.map(opt => {
                let _opt = {
                    label: opt.value,
                    value: opt.label,
                    editable: opt.editable,
                    field_id: opt.field_id,
                    id: opt.id,
                    ordering: opt.ordering
                }
                _itm.options.push(_opt)
                })
            }
            this.list.push(_itm)
            })
        })
    }
  },
  created(){
    this.service = new SecurityService();
    this.getList()
  },
  mounted() {}
};
</script>

<style lang="scss">
@import "./css/index.scss";
</style>
