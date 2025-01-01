import { ref} from 'vue'
import { defineStore } from 'pinia'


export const userinfostore=defineStore('userinfo',()=>{

    const userinfolist=ref({  });
    const clearuserinfo=()=>{
      userinfolist.value={};
    }



    return {userinfolist,clearuserinfo}
  },

  {persist:true,

  }
)