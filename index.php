<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Crawling COVID19</title>

    <style>
      body{
        background: #fff;
      }

      .main{
        width: 80%;
        margin: 2% 5%;
        padding: 2% 5%;
        border-radius: 30px;
        overflow: hidden;
        box-shadow: 5px 5px 20px #aaa;

      }
      #title{
        text-align: center;
        font-size: 50px;
      }
      h2{
        font-size: 30px;
      }
      .covid_chart{
        width: 100%;
        float: left;
      }
      .covid_chart1{
        background-color: #fff;
        box-shadow: 5px 5px 15px #aaa;
        padding: 1% 3% 3% 3%;
        width: 45%;
        text-align: center;
        float: left;
        overflow: hidden;
      }

      table, th, td{
        text-align: center;
        border-collapse: collapse;
      }
      table{
        margin: 0 auto;
        width: 100%;
      }
      td{
        border: 1px solid #eee;
        padding: 2%;
      }
      th{
        border: 1px solid #fff;
        padding: 3% 2%;
        background-color: #888;
        color: #fff;
      }

      .covid_day_confirmed{
        color: blue;
      }
      img{
        position: relative;
        width: 120%;
        left: -9%;
      }

    </style>
  </head>
  <body>
    <div class="main">
          <h1 id="title">COVID-19</h1>
          <div class="covid_chart">
            <div class="covid_chart1">
              <h2>국내 확진자 현황</h2>
              <table border="1">
                <tr>
                  <th>시도별</th>
                  <th>총확진자   <span>(+전일확진자)</span></th>
                  <th>격리중</th>
                  <th>격리해제</th>
                  <th>사망자</th>
                </tr>
                <?php require_once('crawling_covid19.php'); ?>
              </table>
              <img src="covid_graph.png">
            </div>
          </div>
          <script>
            document.getElementsByTagName("tr")[1].style = "font-weight:bold";
          </script>



    </div>
  </body>
</html>
