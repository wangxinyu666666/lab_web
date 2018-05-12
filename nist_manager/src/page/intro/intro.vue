<template>
  <div>
    <HtmlTitle ref="HtmlTitle"></HtmlTitle>
  </div>
</template>

<script>
import {renderURL} from '../../api/httpapi.js'
import HtmlTitle from '../../components/show_html.vue'
export default{
  components:{HtmlTitle},
  data(){
    return{

    }
  },
  mounted(){
    //var key="news_171123230041";
    //修改编辑时的关键字
    this.$store.state.Editor_key="intro";
    var key="intro";
    var TitleDetailUrl=renderURL+key;
    this.$refs.HtmlTitle.Init(TitleDetailUrl);
  }
}
</script>

<style>
.edit{
  position:absolute;
  bottom:-10%;
  right:10%
}
</style>
