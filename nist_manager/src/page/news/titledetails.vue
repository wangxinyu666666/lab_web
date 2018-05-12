<template>
  <div>
    <HtmlTitle ref="HtmlTitle"></HtmlTitle>
  </div>
</template>

<script>
import HtmlTitle from '../../components/show_html.vue'
export default{
  components:{HtmlTitle},
  data(){
    return{

    }
  },
  mounted(){
    var key=this.$store.state.news_key;
    //alert(key);
    var TitleDetailUrl="../mock/RenderHTML.json"
    this.$refs.HtmlTitle.Init(TitleDetailUrl);
  }
}
</script>

<style>
</style>
