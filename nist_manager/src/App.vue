<template>
  <div id="container">
    <Header1 id="header"></Header1>
    <div class="main">
    <router-view/>
    </div>
    <Footer1 class="footer"></Footer1>
  </div>
</template>

<script>
import Header1 from '@/components/header.vue'
import Footer1 from '@/components/footer.vue'
export default {
      components: {Header1,Footer1},
      data(){
        return{

        }
      },
}
</script>

<style>
html,body{
  margin:0;
  padding: 0;
  background:url('./assets/background.jpg') repeat 0px 0px;
  height: 100%;
}
#container {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  margin: 0 auto;
  height: 100% !important;
  height:100%;
  min-height:100%;
}
#container .header{
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);
    z-index: 1000;
    width:100%;
    position: absolute;
    top:0;
}
#container .main{
    min-height:70%;
    padding-top:13%;
}
#container .footer{
    position:relative;
    width:100%;
    height: 5%;
}
</style>
