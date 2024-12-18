let data2
let res
  function fetchData() {
    data2 =  fetch("api/sales_by_good");
    res =  data2.json();
    console.log(res);
  }
  fetchData();
  console.log("orderdata", res);
let ctx = document.getElementById('ex_chart');

let data = {
    labels: [],
    datasets: [{
        label: '合計金額',
        data: [],
        backgroundColor: 'rgba(255, 100, 100, 1)'
    }]
};
for(let i=0;i<5;i++){
  data.labels.push(objData.id[i])
  data.data.push(objData.sumprice[i])
}
let options = {
  indexAxis: 'y',
    scales: {
        x:{
            min: 300
            //beginAtZero: true
        }
    }
};

let ex_chart = new Chart(ctx, {
    type: 'bar',
    data: data,
    options: options
});
