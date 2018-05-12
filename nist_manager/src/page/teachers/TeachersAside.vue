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
          InitSecodRouter:[{index:"/teachers",name:"师资队伍"}]
      }
   },
   methods: {
     },
   }
</script>

<style>
</style>
