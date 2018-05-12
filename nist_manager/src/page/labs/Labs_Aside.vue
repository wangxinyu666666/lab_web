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
          InitSecodRouter:[{index:"/attack",name:"网络攻防技术研究室"},{index:"/virtual",name:"虚拟化技术研究室"},{index:"/domains",name:"域名体系安全技术研究室"},{index:"/yun",name:"云计算技术研究室"}]
      }
   },
   methods: {
     },
   }
</script>

<style>
</style>
