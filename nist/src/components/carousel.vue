<template>
    <div class="details">
      <el-carousel :interval="4000"  height="400px">
        <el-carousel-item v-for="item in imgs" >
        <img :src="item" style="width:80%;height:380px;position:relative;left:10%;top:10px" >
        </el-carousel-item>
      </el-carousel>
    </div>
</template>

<script>
export default{
  data(){
    return{
      imgs:[]
    }
  }
}
</script>

<style>
.details{
  position: relative;
  left:5%;
  background:#11334D;
  top:10px;
  border-radius:10px;
  min-height: 400px;
}
</style>
