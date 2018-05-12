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
    var key="gains";
    var TitleDetailUrl=renderURL+key;
    //编辑关键字
    this.$store.state.Editor_key=key;
    this.$refs.HtmlTitle.Init(TitleDetailUrl);
  }
}
</script>

<style>
</style>
