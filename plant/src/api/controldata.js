import httpInstance from "@/utils/request.js";


export  function updataapi(Parameter) {

  return httpInstance({
    url: '/api/updata',
    method:"post",
    data:{
      Parameter:Parameter
    },
  })
}


export  function downdataapi(Parameter) {

  return httpInstance({
    url: '/api/downdata',
    method:"POST",
    data:{
      Parameter:Parameter
    },
  })
}
