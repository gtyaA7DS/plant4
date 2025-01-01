<script setup>
import {usewebsocketinfostore} from "@/stores/websocketinfo.js"
import { computed, onMounted, onUnmounted, reactive, ref ,watch} from "vue"
import { useToast } from "primevue/usetoast";
import { storeToRefs } from 'pinia';


const toast = useToast();


const websocketinfostore=usewebsocketinfostore()

const { msg,socket } = storeToRefs(websocketinfostore);
watch(msg, (newValue, oldValue) => {
  console.log("dwffefgr")
  showWarn(newValue)
});


// watch(currentTime,(newvalue,oldvalue)=>{
//   showWarn(newvalue)
// })
//
const showWarn = (message) => {
  toast.add({ severity: 'warn', summary: 'Warn Message', detail: message, life: 4000 });
};


onMounted(()=>{
  websocketinfostore.initWebSocket()

})


onUnmounted(()=>{
  socket.close();
  console.log("closesss")

})
</script>

<template>
  <Toast />
  <router-view />
</template>

<style scoped></style>
