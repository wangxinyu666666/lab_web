<template>
  <div class="intro">
    <div id="details">
   </div>
   <br/>
   <div class="editimgs">
      <el-button icon="el-icon-edit" @click="editHTML">点击编辑</el-button>
  </div>
 </div>
</template>

<script>
import Axios from 'axios'
export default{
  methods: {
   Init(url){
      Axios.get(url)
      .then(function(res){
        document.getElementById("details").innerHTML=res.data.HTML+"<br/><br/>";
      })
      .catch(function(){
        console.log("error");
      })
   },
   editHTML(){
      //点击跳转到editor页面，通过不同的url关键字进行处理
      this.$router.push('/editor');
   },
 },
}
</script>

<style>
.intro{
 position: relative;
 width: 96%;
 min-height: 400px;
 color:white
}
.intro #details{
  width: 90%;
  position: relative;
  left:5%;
  background:rgba(234,234,234,0.1);
  border-radius:10px;
  min-height: 400px;
  overflow:visible
}
.block{
float: right;
}
.edit{
  position: absolute;
  bottom:5%;
  right:0px
}
</style>
