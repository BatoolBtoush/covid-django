'use strict';
// function storeData() {
//     console.log("HEY")
// }


const storeData = () => {
    console.log("HEY")

}

// fetch(url, {
//     method: "POST",
//     credentials: "same-origin",
//     headers: {
//       "X-Requested-With": "XMLHttpRequest",
//       "X-CSRFToken": getCookie("csrftoken"),
//     },
//     body: JSON.stringify({payload: "data to send"})
//   })
//   .then(response => response.json())
//   .then(data => {
//     console.log(data);
//   });

$.ajax({
    url: url,
    type: "POST",
    dataType: "json",
    data: JSON.stringify({payload: payload,}),
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
    },
    success: (data) => {
      console.log(data);
    },
    error: (error) => {
      console.log(error);
    }
  });