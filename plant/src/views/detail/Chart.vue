<script setup>
import { computed, onMounted, ref, watch } from "vue";
import { useLayout } from '@/layout/composables/layout';
import {getalldataapi} from "@/api/getdata";

const { layoutConfig } = useLayout();
let documentStyle = getComputedStyle(document.documentElement);
let textColor = documentStyle.getPropertyValue('--text-color');
let textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
let surfaceBorder = documentStyle.getPropertyValue('--surface-border');

const temperatureData = ref(null);
const pm1Options=ref(null);
const pm1Data=ref(null);

const pm10Options=ref(null);
const pm10Data=ref(null);
const pm25Data=ref(null);
const pm25Options=ref(null);
const humidityData = ref(null);


const temperatureOptions = ref(null);


const humidityOptions = ref(null);

const  Date=ref([1,2,3,4,5,6,7])

const envdata=ref([])
const  getalldata=async()=> {
  const res = await getalldataapi()
  console.log(res.data)

  envdata.value = res.data
  console.log(1,envdata.value['temperature'])
  temperatureData.value.datasets[0]['data']=envdata.value['temperature']
  humidityData.value.datasets[0]['data']=envdata.value['humidity']
  pm1Data.value.datasets[0]['data']=envdata.value['pm1']
  pm10Data.value.datasets[0]['data']=envdata.value['pm10']
  pm25Data.value.datasets[0]['data']=envdata.value['pm25']
}


onMounted(()=>{
  getalldata();

})


const setColorOptions = () => {
    documentStyle = getComputedStyle(document.documentElement);
    textColor = documentStyle.getPropertyValue('--text-color');
    textColorSecondary = documentStyle.getPropertyValue('--text-color-secondary');
    surfaceBorder = documentStyle.getPropertyValue('--surface-border');
};

const setChart = () => {
  humidityData.value = {
        labels: Date,
        datasets: [
            {
                label: 'humidity',
                backgroundColor: documentStyle.getPropertyValue('--primary-500'),
                borderColor: documentStyle.getPropertyValue('--primary-500'),
                data:[]
            }
        ]
    };
  humidityOptions.value = {
        plugins: {
            legend: {
                labels: {
                    fontColor: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary,
                    font: {
                        weight: 500
                    }

                },
                grid: {
                    display: false,
                    drawBorder: false
                }
            },
            y: {

              suggestedMin:0,
              suggestedMax: 100,
                ticks: {
                    color: textColorSecondary,
                  callback: function(value) {
                    return value + '%';
                  }
                },
                grid: {
                    color: surfaceBorder,
                    drawBorder: false
                }
            }
        }
    };


  pm1Data.value={
    labels:Date,
    datasets: [
      {
        label: 'pm1',
        data: [],
        fill: false,
        backgroundColor: documentStyle.getPropertyValue('--primary-500'),
        borderColor: documentStyle.getPropertyValue('--primary-500'),
        tension: 0.4
      },

    ]
  };

    temperatureData.value = {
        labels:Date,
        datasets: [
            {
                label: 'temperature',
                data: [],
                fill: false,
                backgroundColor: documentStyle.getPropertyValue('--primary-500'),
                borderColor: documentStyle.getPropertyValue('--primary-500'),
                tension: 0.4
            }
        ]
    };

    temperatureOptions.value = {
        plugins: {
            legend: {
                labels: {
                    fontColor: textColor
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder,
                    drawBorder: false
                }
            },
            y: {
              suggestedMin:0,
              suggestedMax: 50,
                ticks: {
                    color: textColorSecondary
                },
                grid: {
                    color: surfaceBorder,
                    drawBorder: false
                }
            }
        }
    };
  pm1Options.value = {
    plugins: {
      legend: {
        labels: {
          fontColor: textColor
        }
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false
        }
      },
      y: {
        suggestedMin:0,
        suggestedMax: 100,
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false
        }
      }
    }
  };

  pm10Data.value = {
    labels: Date,
    datasets: [
      {
        label: 'pm10',
        backgroundColor: documentStyle.getPropertyValue('--primary-500'),
        borderColor: documentStyle.getPropertyValue('--primary-500'),
        data:[]
      }
    ]
  };
  pm10Options.value = {
    plugins: {
      legend: {
        labels: {
          fontColor: textColor
        }
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary,
          font: {
            weight: 500
          }
        },
        grid: {
          display: false,
          drawBorder: false
        }
      },
      y: {

        suggestedMin:0,
        suggestedMax: 100,
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false
        }
      }
    }
  };
  pm25Data.value={
    labels:Date,
    datasets: [
      {
        label: 'pm25',
        data: [],
        fill: false,
        backgroundColor: documentStyle.getPropertyValue('--primary-500'),
        borderColor: documentStyle.getPropertyValue('--primary-500'),
        tension: 0.4
      }
    ]
  };



  pm25Options.value={
    plugins: {
      legend: {
        labels: {
          fontColor: textColor
        }
      }
    },
    scales: {
      x: {
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false
        }
      },
      y: {
        suggestedMin:0,
        suggestedMax: 100,
        ticks: {
          color: textColorSecondary
        },
        grid: {
          color: surfaceBorder,
          drawBorder: false
        }
      }
    }
  };



};

watch(
    layoutConfig.theme,
    () => {
        setColorOptions();
        setChart();
    },
    { immediate: true }
);
</script>

<template>
    <div class="grid p-fluid">
        <div class="col-12 xl:col-6">
            <div class="card">
                <h5>temperature</h5>
                <Chart type="line" :data="temperatureData" :options="temperatureOptions"></Chart>
            </div>
        </div>
        <div class="col-12 xl:col-6">
            <div class="card">
                <h5>humidity</h5>
                <Chart type="bar" :data="humidityData" :options="humidityOptions"></Chart>
            </div>
        </div>
      <div class="col-12 xl:col-6">
        <div class="card">
          <h5>pm1</h5>
          <Chart type="line" :data="pm1Data" :options="pm1Options"></Chart>
        </div>
      </div>

      <div class="col-12 xl:col-6">
        <div class="card">
          <h5>pm10</h5>
          <Chart type="line" :data="pm10Data" :options="pm10Options"></Chart>
        </div>
      </div>
      <div class="col-12 xl:col-6">
        <div class="card">
          <h5>pm2.5</h5>
          <Chart type="line" :data="pm25Data" :options="pm25Options"></Chart>
        </div>
      </div>







    </div>
</template>
