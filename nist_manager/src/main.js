// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'

import store from './vuex/store'
import 'element-ui/lib/theme-chalk/index.css';

import '../static/UE/ueditor.config.js'
import '../static/UE/ueditor.all.min.js'
import '../static/UE/lang/zh-cn/zh-cn.js'
import '../static/UE/ueditor.parse.min.js'
Vue.config.productionTip = false

Vue.use(ElementUI,{ size: 'small' })
/* eslint-disable no-new */
router.beforeEach((to, from, next) => {
    var fir='';
    switch(to.path){
      //case '/news':
      //  fir="news";
      //  store.commit("HandleSecondRouter",{firstAct:fir});
      //  next();
      //  break;
      //case '/notice':
      //    fir="news";
      //    store.commit("HandleSecondRouter",{firstAct:fir});
      //    next();
      //    break;
      case '/labs':
        fir="labs";
        store.commit("HandleSecondRouter",{firstAct:fir});
        next()
        break;
      case '/teachers':
        fir="teachers";
        store.commit("HandleSecondRouter",{firstAct:fir});
        next();
        break;
      case '/intro':
        fir="intro";
        store.commit("HandleSecondRouter",{firstAct:fir});
        next();
        break;
      case '/activities':
         fir="activities";
         store.commit("HandleSecondRouter",{firstAct:fir});
         next();
         break;
      default:
         next();
         break;
    }
})
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
