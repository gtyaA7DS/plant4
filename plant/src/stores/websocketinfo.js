import { ref} from 'vue'
import { defineStore } from 'pinia'


export const usewebsocketinfostore=defineStore('websocketinfo',()=>{

     const msg=ref('')
     const  isconnect=ref(false)
    const  socket=ref(null)
  const initWebSocket = () => {
       if( isconnect.value) return

    socket.value = new WebSocket('ws://124.222.214.78:8764');

    socket.value.onopen = () => {
      console.log('WebSocket连接已建立');
      // 可以在此更新全局状态，表示连接成功
      isconnect.value=true
    };


    socket.value.onmessage = (event) => {

      msg.value = event.data
      console.log("haha",msg.value)
    };

// 连接关闭时触发
    socket.value.onclose = () => {
      console.log('WebSocket连接已关闭');
      isconnect.value=false;
    };
  }
    return {initWebSocket,socket,msg}
  }
)