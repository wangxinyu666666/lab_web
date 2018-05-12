<template>
  <div>
    <Card ref="HtmlTitle"></Card>
  </div>
</template>

<script>
import Card from '../../components/card.vue'
export default{
  components:{Card},
  data(){
    return{

    }
  },
  mounted(){
    //var key=this.$store.state.news_key;
    //alert(key);
    var TitleDetailUrl="../mock/RenderHTML.json"
    //this.$refs.HtmlTitle.Init(TitleDetailUrl);
    this.$store.state.ifstate="jishi";
  }
}
</script>

<style>
</style>