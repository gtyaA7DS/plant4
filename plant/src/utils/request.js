import axios from 'axios'
import 'element-plus/theme-chalk/el-message.css'
import { ElMessage } from 'element-plus'
import { userinfostore} from '@/stores/userinfo.js'
import router  from "@/router";
const httpInstance=axios.create(
    {   //基地址
        baseURL: 'http://124.222.214.78:5000',
        //超时5miao
        timeout:5000,
    }
)


httpInstance.interceptors.request.use( config=> {
    const userinfo=userinfostore()
    const token=userinfo.userinfolist.value?.token;

    if(token){

        config.headers.Authorization= `Bearer ${token}`
        }




    return config },e=>{ return Promise.reject(e) })

httpInstance.interceptors.response.use(res=>{return res.data },e=>{


            console.log(e)
    if(e.response.status===401 || e.response.status===422 ){
        const userinfo=userinfostore()
        console.log(userinfo.userinfolist.value)
        userinfo.clearuserinfo();


        //
        router.push('/login')
        ElMessage( {type:'warning',message:e.response.data.msg+",请重新登录"|| "error"})

    }else{
        ElMessage( {type:'warning',message:e.response.data.msg|| "error"})
    }
    return Promise.reject(e)
})


export default httpInstance