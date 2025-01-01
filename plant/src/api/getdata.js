import httpInstance from "@/utils/request.js";


export  function getalldataapi() {

  return httpInstance({
    url: '/api/getalldata',

  })
}


