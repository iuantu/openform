import moment from 'moment'
export default{
    install(Vue, options){
        Vue.mixin({
            methods: {
                timeFormat(text, formatText){
                    return moment(text).format(formatText)
                }
            },
        })
    }
}