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
          InitSecodRouter:[{index:'/activities',name:"中心纪实"},{index:"/happytime",name:"欢乐时光"}]
      }
   },
   methods: {
     },
   }
</script>

<style>
</style>
