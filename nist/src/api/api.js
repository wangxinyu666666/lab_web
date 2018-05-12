//在该js中，定义并实现与后端对接的api

import {
  AllNewsUrl
} from "@/api/httpapi"
import Axios from 'axios'


//获取个人页上该学生的进出信息
export const getAllNews= () => {
    var p = new Promise(function (resolve, reject) {
        Axios.post(AllNewsUrl, {}, { headers: { 'Content-Type': 'application/json' } }).then(
            (respone) => {
                resolve(respone['data'])
            },
            (respone) => {
                resolve(respone['data'])
            }
        )
    })
    return p
    /* return {
        news:[{name：“新闻标题1”,time:"11-13"},
             {name:"新闻标题2"，title:"11-14"}]
       notice:[{name:'通知标题1',time:'11-21'},
              {name:'通知标题1'，time：‘11-24’}]
 }*/
}
