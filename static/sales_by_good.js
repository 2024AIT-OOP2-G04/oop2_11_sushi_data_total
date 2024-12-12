fetch("/api/sales_by_good")
  .then((res) => res.json())
  .then((data) => {
    console.log("orderdata", data);
  });
