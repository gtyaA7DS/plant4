<script setup>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import { updataapi, downdataapi} from "@/api/controldata";
import { ref, onMounted, onUnmounted } from "vue";
import { ElMessage } from "element-plus";
import 'element-plus/theme-chalk/el-message.css'



import { useToast } from "primevue/usetoast";
const toast = useToast();


const selectopenParameter=ref(null)
const selectcloseParameter=ref(null)


const Parameter=ref(['空调_热',"空调_制冷","空气净化器","除湿器","加湿器"])






const confirmup = async () => {

      if (!selectopenParameter.value)
      {  ElMessage( {type:'warning',message:"no selected"});
       return

      }
        await  updataapi(selectopenParameter.value).then(
          ()=>{
            ElMessage( {type:'success',message:"success"});
            selectopenParameter.value=null;
          }

        ).catch(
          ()=>{

            ElMessage( {type:'error',message:"error"});
            selectopenParameter.value=null;
          }
        )


};
 const comfiredown =async () => {
   if (!selectcloseParameter.value)
   {  ElMessage( {type:'warning',message:"no selected"});
     return

   }
   await  downdataapi(selectcloseParameter.value).then(
     ()=>{
       ElMessage( {type:'success',message:"success"});
       selectcloseParameter.value=null;
     }

   ).catch(
     ()=>{

       ElMessage( {type:'error',message:"error"});
       selectcloseParameter.value=null;
     }
   )


 };





</script>

<template>

    <div class="grid">




      <div class="col-12 lg:col-6">
        <div class="card ">
          <Dropdown v-model="selectopenParameter" :options="Parameter"  placeholder="选择要开启的设备" class="w-full md:w-14rem" />
          <br>
          <br>

          <Button  @click="confirmup" icon="pi pi-angle-up" label="开启" class="mr-2"></Button>
        </div>
      </div>



        <div class="col-12 lg:col-6">
            <div class="card p-fluid">
              <Dropdown v-model="selectcloseParameter" :options="Parameter" placeholder="选择要关闭的设备" class="w-full md:w-14rem" />

              <Button label="关闭" icon="pi pi-angle-down" class="p-button-danger" style="width: auto;margin-top: 20px;" @click="comfiredown" />

            </div>

        </div>
<!--      <div class="col-12 lg:col-6">-->
<!--        <div class="card">-->
<!--          <DataTable :value="settingdata" :size="large" tableStyle="min-width: 25rem">-->
<!--            <Column field="type" header="Type"></Column>-->
<!--            <Column field="value" header="Value"></Column>-->

<!--          </DataTable>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="col-12 lg:col-6">-->
<!--        <div class="card">-->
<!--          <div  class="flex flex-wrap align-items-center mb-3 gap-2">-->
<!--            <Dropdown v-model="form.crop" :options="Crops"  placeholder="Change Crops" class="w-full md:w-14rem" />-->
<!--          </div>-->

<!--           <div   style="margin-top: 20px" >-->
<!--             <Button type="button" label="Change" icon="pi pi-check" @click="changesetting"  />-->
<!--           </div>-->
<!--        </div>-->
<!--      </div>-->






    </div>
</template>
