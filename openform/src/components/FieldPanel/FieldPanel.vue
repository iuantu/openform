<template>
  <div class="left-aside">
    <div v-for="(category, index) in categories" :key="index">
      <div class="my-components">{{category.label}}</div>
      <draggable
          class="dragArea list-group"
          :list="category.components"
          :group="{ name: 'components', pull: 'clone', put: false,  }"
          :sort="false"
          :clone="cloneComponent"
          ghost-class="ghost">
          <div class="list-group-item"
            v-for="(element, componentIndex) in category.components"
            :key="componentIndex"
          >
            <div class="inner-items">
              <i class="fa fa-file-text-o"></i>
              {{element.name}}
            </div>
          </div>
      </draggable>
    </div>
  </div>
</template>

<script>
import draggable from 'vuedraggable'
import { categories } from '../fields/index'

export default {
  components: {
    draggable
  },
  data() {
    return {
      categories,
    };
  },
  methods: {
    cloneComponent(component) {
      return component.default();
    }
  },
};
</script>

<style lang="scss">
  @import "./FieldPanel.scss";
</style>
