<template>
    <div class="details">
      <el-carousel :interval="5000000" arrow="always" :type="Type"  height="400px">
        <el-carousel-item v-for="(item,index) in pictures" :key="index">
        <img :src="item"  style="width:100%;height:380px;position:relative;" >
        </el-carousel-item>
      </el-carousel>
    </div>
</template>

<script>
export default{
  data(){
    return{
      //  Type:"card", //根据不同场景选择其值为card或者就是空
    }
  },
  props:{
    pictures:{},
    Type:"", //根据不同场景选择其值为card或者就是空
  }
}
</script>

<style>
.details{
  position: relative;
  /*background:#11334D;*/
  top:10px;
  min-height: 400px;
}
</style>
