<template>
    <div class="left-aside">
        <div class="my-components">基本
          <!-- <i class="fa fa-arrow-left" @click="leftAside()"></i> -->
        </div>
        <draggable
            class="dragArea list-group"
            :list="list1"
            :group="{ name: 'components', pull: 'clone', put: false,  }"
            :sort="false"
            :clone="cloneComponent"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list1"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
        <div class="my-components">联系人
        </div>
        <draggable
            class="dragArea list-group"
            :list="list2"
            :group="{ name: 'components', pull: 'clone', put: false,  }"
            :sort="false"
            :disabled="true"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list2"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
        <div class="my-components">支付</div>
        <draggable
            class="dragArea list-group"
            :list="list3"
            :group="{ name: 'components', pull: 'clone', put: false,  }"
            :sort="false"
            :disabled="true"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list3"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
        <div class="my-components">高级</div>
        <draggable
            class="dragArea list-group"
            :list="list4"
            :group="{ name: 'people', pull: 'clone', put: false,  }"
            :sort="false"
            :disabled="true"
            ghost-class="ghost">
            <div class="list-group-item"
              v-for="(element, index) in list4"
              :key="index + element.name"
            >
              <div class="inner-items">
                <i class="fa fa-file-text-o"></i>
                {{element.showName}}
              </div>
            </div>
        </draggable>
    </div>
      
</template>

<script>
import draggable from 'vuedraggable'
import fieldComponents from './fieldComponents'

export default {
  name: "clone",
  inject: ['leftAside'],
  components: {
    draggable
  },
  data() {
    return {
      ...fieldComponents
    };
  },
  methods: {
    cloneComponent(component) {
      return JSON.parse(JSON.stringify(component));
    }
  },
  mounted() {
  },
};
</script>

<style lang="scss">
  @import "./css/index.scss";
</style>
