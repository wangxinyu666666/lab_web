<template>
  <div id="app">
    <Header1></Header1>
    <div class="main">
    <router-view/>
   </div>
    <Footer1></Footer1>
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
/*  background-color:#191919;*/
  background:url('./assets/background.jpg') repeat 0px 0px;
  color:white;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.main{
  margin-top: 150px;
  min-height: 400px
}
</style>
