let current
fetch("/api/sales_by_good")
  .then((res) => res.json())
  .then((data) => {
    console.log("orderdata", data);
    current=data;
  });
let objData = JSON.parse(current);
for(i=0;i<objData.id.length;i++){
  if(a==b){
    
  }
}