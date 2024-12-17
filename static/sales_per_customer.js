document.addEventListener("DOMContentLoaded", () =>  {

    const ctx = document.getElementById("sales_per_customer_graph").getContext("2d");


    fetch("/api/sales_per_customer")
        .then((res) => res.json())
        .then((data) => {
            // ランキングのための降順ソート
            sort_data = data.sort((a,b) => b.total_sales - a.total_sales);

            const id = sort_data.map((i) => i.id);
            const sales = sort_data.map((i) => i.total_sales);
            // グラフを作成
            new Chart(ctx, {
                type: "bar",
                data: {
                    labels: id,
                    datasets: [
                        {
                            label: "客単価ランキング",
                            backgroundColor: "rgba(54, 162, 235, 0.2)",
                            borderColor: "rgba(54, 162, 235, 1)",
                            borderWidth: 1,
                            data: sales,
                        },
                    ],
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true,
                            title: {
                              display: true,
                              text: '単価(円)' // y軸ラベル追加
                          }
                        },
                        x:{
                          title: {
                            display: true,
                            text: '客id' // x軸ラベル追加
                          }
                        }
                    },
                    responsive: false,
                    maintainAspectRatio: false,
                },
            });
        })
        .catch((r) => {
          console.log("データ取得エラーです:", r);
        });
});
