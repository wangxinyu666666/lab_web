//与后端真实交互的可复用函数均写在这里，方便随时切换调试和线上状态

const basicUrl = "api"

//线下测试
//export const AllNewsURL='../mock/allnews.json';      //获取新闻标题
/*export const AllNoticeURL="../mock/allnotice.json";    //获取通知标题
export const IndexIMGURL="../mock/indeximgs.json" */     //获取首页图片地址集合*/

//在线状态
export const AllNewsURL=basicUrl+'/getdata?key=news';      //获取新闻标题
export const AllNoticeURL=basicUrl+"/getdata?key=notice";    //获取通知标题
export const IndexIMGURL=basicUrl+"/getdata?key=index_imgs"      //获取首页图片地址集合

export const PostDataURL=basicUrl+'/postdata?key=';
export const renderURL=basicUrl+"/getdata?key=";
