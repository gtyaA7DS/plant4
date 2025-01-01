import httpInstance from "@/utils/request.js";


export  function Loginapi(params) {

    return httpInstance({
        url: '/api/login',
        method:"POST",
        data:params,
    })
}