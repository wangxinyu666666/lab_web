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
          InitSecodRouter:[{index:"/intro",name:"中心简介"},{index:"/leaders",name:"中心领导"},{index:"/environment",name:"中心环境"}]
      }
   },
   methods: {
     },
   }
</script>

<style>
</style>
