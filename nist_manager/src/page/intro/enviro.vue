<template>
  <div class="intro">
        <div id="details">
            <Carousel :pictures="pictures" :Type="type"></Carousel>
       </div>
       <br/>
       <div class="editimgs">
       <el-button icon="el-icon-edit" @click="editIndexImgs">编辑图片</el-button>
      </div>
  </div>
</template>

<script>
import Axios from 'axios'
import {renderURL} from '../../api/httpapi.js'
import Carousel from '../../components/carousel.vue'
export default{
  components:{Carousel},
  data(){
    return{
      pictures:[],
      type:"card",
    }
  },
  methods: {
    editIndexImgs(){
        this.$store.state.Editor_key="enviro_imgs_html";
        this.$router.push('/editor');
    }
  },
  mounted(){
    var EnviroURL=renderURL+"enviro_imgs";
  //  var EnviroURL=renderURL+"index_imgs";
    Axios.get(EnviroURL)
    .then(function(res){
      var len=res.data.pictures.length
      var tem=[];
      for(var i=0;i<len;i++){
         tem.push(res.data.pictures[i]);
      }
      this.pictures=tem;
    }.bind(this))
    .catch(function(){
      console.log("error");
    })
  }
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
  min-width: 600px;
  overflow:visible
}
.block{
float: right;
}
</style>
