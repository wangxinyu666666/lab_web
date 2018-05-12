<template>
  <div>
  <AllAside :SecondRouter="InitSecodRouter"></AllAside>
  </div>
</template>

<script>
import AllAside from '../../components/aside.vue'
export default{
  components: {AllAside},
  data(){
      return{
          InitSecodRouter:[{index:"/",name:"中心新闻"},{index:"/notice",name:"通知公告"}]
      }
   },
   methods: {
     },
   }
</script>

<style>
</style>
