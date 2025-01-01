<script setup>
import { computed, onMounted, onUnmounted, reactive, ref } from "vue";

import {getalldataapi} from "@/api/getdata";
import { useToast } from "primevue/usetoast";


const envdata=ref([])




const  getalldata=async()=>{
       const res=await getalldataapi()
  console.log(res)

   envdata.value=res.data
  console.log(envdata.value['pm25'][0])



}



















const lineOptions = ref(null);


lineOptions.value = {
        plugins: {
            legend: {
                labels: {
                    color: '#495057'
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            },
            y: {
              suggestedMin:0,
              suggestedMax: 200,
                ticks: {
                    color: '#495057'
                },
                grid: {
                    color: '#ebedef'
                }
            }
        }
    };




onMounted(()=>{
  getalldata();
})

</script>

<template>
    <div class="grid">

      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3"> 温度（Temperature）</span>
              <div class="text-900 font-medium text-xl">{{ envdata['pm25'] ? envdata['temperature'][envdata['temperature'].length-1]:null }} ℃ </div>
            </div>
            <div class="flex align-items-center justify-content-center bg-purple-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-chart-bar text-purple-500 text-xl"></i>
            </div>
          </div>

          <span class="text-500">since lasted </span>
        </div>
      </div>

      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">湿度（Humidity） </span>
              <div class="text-900 font-medium text-xl">{{  envdata['pm25'] ? envdata['humidity'][envdata['humidity'].length-1]:null }} %</div>
            </div>
            <div class="flex align-items-center justify-content-center bg-green-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-table text-blue-500 text-xl"></i>
            </div>
          </div>
          <span class="text-green-500 font-medium"> </span>
          <span class="text-500">since lasted </span>
        </div>
      </div>

        <div class="col-12 lg:col-6 xl:col-3">
            <div class="card mb-0">
                <div class="flex justify-content-between mb-3">
                    <div>
                        <span class="block text-500 font-medium mb-3">pm1</span>
                        <div class="text-900 font-medium text-xl">{{ envdata['pm25'] ? envdata['pm1'][envdata['pm1'].length-1]:null}}</div>
                    </div>
                    <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
                        <i class="pi pi-sliders-h text-purple-500 text-xl"></i>
                    </div>
                </div>

                <span class="text-500">since lasterd</span>
            </div>
        </div>
      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">pm2.5</span>
              <div class="text-900 font-medium text-xl">{{envdata['pm25'] ? envdata['pm25'][envdata['pm25'].length-1]:null }}</div>
            </div>
            <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-sliders-h text-purple-500 text-xl"></i>
            </div>
          </div>

          <span class="text-500">since lasterd</span>
        </div>
      </div>
      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">pm10</span>
              <div class="text-900 font-medium text-xl">{{ envdata['pm25'] ? envdata['pm10'][envdata['pm10'].length-1]:null }}</div>
            </div>
            <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-sliders-h text-purple-500 text-xl"></i>
            </div>
          </div>

          <span class="text-500">since lasterd</span>
        </div>
      </div>

<!--        <div class="col-12 xl:col-6">-->


<!--          <div class="card">-->
<!--            <h5>Prophet model predicts the  future temperature  In the greenhouse</h5>-->
<!--            <Chart type="line" :data=" lineData_Prophet_Temperature " :options="lineOptions" />-->
<!--          </div>-->

<!--        </div>-->
<!--        <div class="col-12 xl:col-6">-->
<!--            <div class="card">-->
<!--                <h5>LSTM model predicts the  future temperature  In the greenhouse </h5>-->
<!--                <Chart type="line" :data="lineData_LSTM_Temperature" :options="lineOptions" />-->
<!--            </div>-->


<!--        </div>-->
<!--      <div class="col-12 xl:col-6">-->


<!--        <div class="card">-->
<!--          <h5>Prophet model predicts the  future Humidity In the greenhouse</h5>-->
<!--          <Chart type="line" :data=" lineData_Prophet_Humidity" :options="lineOptions" />-->
<!--        </div>-->

<!--      </div>-->
<!--      <div class="col-12 xl:col-6">-->


<!--        <div class="card">-->
<!--          <h5>LSTM model predicts the  future Humidity In the greenhouse</h5>-->
<!--          <Chart type="line" :data=" lineData_LSTM_Humidity " :options="lineOptions" />-->
<!--        </div>-->

<!--      </div>-->
<!--      <div class="col-12 xl:col-6">-->


<!--        <div class="card">-->
<!--          <h5>Prophet model and LSTM model predicts the  future   Light_Intensity In the greenhouse</h5>-->
<!--          <Chart type="line" :data=" lineData_Light_Intensity  " :options="lineOptions" />-->
<!--        </div>-->

<!--      </div>-->
<!--      <div class="col-12 xl:col-6">-->


<!--        <div class="card">-->
<!--          <h5>Prophet model and LSTM model predicts the  future   CO2_Concentration In the greenhouse</h5>-->
<!--          <Chart type="line" :data=" lineData_CO2_Concentration" :options="lineOptions" />-->
<!--        </div>-->

<!--      </div>-->
<!--      <div class="col-12 xl:col-6">-->


<!--        <div class="card">-->
<!--          <h5>Prophet model and LSTM model predicts the  future   Soil_pH In the greenhouse</h5>-->
<!--          <Chart type="line" :data=" lineData_Soil_pH " :options="lineOptions" />-->
<!--        </div>-->

<!--      </div>-->


    </div>



</template>
