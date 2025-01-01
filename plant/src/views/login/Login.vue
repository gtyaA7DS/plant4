<script setup>
import {useRouter} from "vue-router";
import { ref, computed } from 'vue';
import AppConfig from '@/layout/AppConfig.vue';
import  {Loginapi} from "@/api/login.js"
import 'element-plus/theme-chalk/el-message.css'
import { ElMessage } from 'element-plus'
import { userinfostore} from '@/stores/userinfo.js'

const userinfo=userinfostore()
const router=useRouter();

const username = ref('admin');
const password = ref('admin');
const checked = ref(false);



const  form=ref({
   'username':username,
  'password':password
})

const logoUrl = "/layout/images/logo-dark.svg";
const login= async()=>{

  if(username.value === '' || password.value === '')
  {ElMessage({type:'warning',message:"empty username or password" })

    return ;
  }
   else if(checked.value===false){
      ElMessage({type:'warning',message:"please check the box" })

       return;
    }
   else{

      const res=await Loginapi(form.value)
    console.log(res)

      userinfo.userinfolist.value=res;

      console.log(userinfo.userinfolist.value);
      ElMessage({type:'success',message:"login success" })
      router.replace({path:'/'})

    }
}

</script>

<template>
    <div class="surface-ground flex align-items-center justify-content-center min-h-screen min-w-screen overflow-hidden">
        <div class="flex flex-column align-items-center justify-content-center">
            <img :src="logoUrl" alt="Sakai logo" class="mb-5 w-6rem flex-shrink-0" />
            <div style="border-radius: 56px; padding: 0.3rem; background: linear-gradient(180deg, var(--primary-color) 10%, rgba(33, 150, 243, 0) 30%)">
                <div class="w-full surface-card py-8 px-5 sm:px-8" style="border-radius: 53px">
                    <div class="text-center mb-5">
                        <img src="/demo/images/login/avatar.png" alt="Image" height="50" class="mb-3"  />
                        <div class="text-900 text-3xl font-medium mb-3">欢迎,</div>
                        <span class="text-600 font-medium">登录后才能继续操作</span>
                    </div>

                    <div>
                        <label for="username" class="block text-900 text-xl font-medium mb-2">用户名</label>
                        <InputText id="username11" type="text" placeholder="username" class="w-full md:w-30rem mb-5" style="padding: 1rem" v-model="username" />

                        <label for="password1" class="block text-900 font-medium text-xl mb-2">密码</label>
                        <Password id="password1" v-model="password" placeholder="Password" :toggleMask="true" class="w-full mb-3" inputClass="w-full" :inputStyle="{ padding: '1rem' }"></Password>

                        <div class="flex align-items-center justify-content-between mb-5 gap-5">
                            <div class="flex align-items-center">
                                <Checkbox v-model="checked" id="rememberme1" binary class="mr-2"></Checkbox>
                                <label for="rememberme1">同意我们的协议</label>
                            </div>
                            <a class="font-medium no-underline ml-2 text-right cursor-pointer" style="color: var(--primary-color)">忘记密码</a>
                        </div>
                        <Button label="Sign In" class="w-full p-3 text-xl" @click="login"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <AppConfig simple />
</template>

<style scoped>
.pi-eye {
    transform: scale(1.6);
    margin-right: 1rem;
}

.pi-eye-slash {
    transform: scale(1.6);
    margin-right: 1rem;
}
</style>
