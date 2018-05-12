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
  //  var key="news_171123230041";
    var key="projects";
    var TitleDetailUrl=renderURL+key;
    //编辑关键字
    this.$store.state.Editor_key=key;
    this.$refs.HtmlTitle.Init(TitleDetailUrl);
  }
}
</script>

<style>
</style>
