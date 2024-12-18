fetch("/api/good_of_numberpiece")
  .then((res) => res.json())
  .then((data) => {
    console.log("customerData", data);
  });

  
