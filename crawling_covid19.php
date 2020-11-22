<meta charset="utf-8">
<?php

$conn = mysqli_connect('localhost','root','nagyeong01','crawling_covid19');


$covid_sql = "SELECT * FROM covid19;";
$covid_result = mysqli_query($conn, $covid_sql);

$covid_num = mysqli_num_rows($covid_result);


for($i=0; $i<$covid_num; $i++){
  $covid[$i] = mysqli_fetch_array($covid_result);
  $covid_city = $covid[$i]["시도명"];
  $covid_day_confirmed = $covid[$i]["하루확진자"];
  $covid_total_confirmed = $covid[$i]["총확진자"];
  $covid_total_isolation = $covid[$i]["격리중"];
  $covid_total_n_isolation = $covid[$i]["격리해제"];
  $covid_total_death = $covid[$i]["사망자"];

  echo "<tr>
          <td class='covid_city'>$covid_city</td>
          <td class='covid_total_confirmed'>$covid_total_confirmed
            <span class='covid_day_confirmed'>(+$covid_day_confirmed)</span>
          </td>
          <td class='covid_total_isolation'>$covid_total_isolation</td>
          <td class='covid_total_n_isolation'>$covid_total_n_isolation</td>
          <td class='covid_total_death'>$covid_total_death</td>
        </tr>";
}

?>
