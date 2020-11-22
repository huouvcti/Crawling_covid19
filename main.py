from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pymysql
from matplotlib import pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name, size=30)

driver = webdriver.Chrome(executable_path="chromedriver.exe")

conn = pymysql.connect(
    host= "localhost",
    user = "root",
    password = "nagyeong01",
    db = "crawling_covid19",
    charset = "utf8"
)
curs = conn.cursor()



def Covid_chart():
    covid_url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdGubun=13"

    driver.get(covid_url)
    html = driver.page_source
    soup = bs(html, "html.parser")

    covid_city = soup.find("tbody").find_all("th")
    covid_day_confirmed = soup.find_all("td", {"headers": "status_level l_type1"})
    covid_total_confirmed = soup.find_all("td", {"headers": "status_con s_type1"})
    covid_total_isolation = soup.find_all("td", {"headers": "status_con s_type2"})
    covid_total_n_isolation = soup.find_all("td", {"headers": "status_con s_type3"})
    covid_total_death = soup.find_all("td", {"headers": "status_con s_type4"})

    '''
    # INSERT
    for i in range(len(covid_city)):
        covid19_sql = "INSERT INTO `covid19`(`시도명`, `하루확진자`, `총확진자`, `격리중`, `격리해제`, `사망자`) " \
                      "VALUES('%s', '%s', '%s', '%s', '%s', '%s');" \
                      "" % (covid_city[i].text, covid_day_confirmed[i].text, covid_total_confirmed[i].text,
                            covid_total_isolation[i].text, covid_total_n_isolation[i].text, covid_total_death[i].text)
        print(covid19_sql)
        curs.execute(covid19_sql)
        conn.commit()
    '''
    x = []
    y = []
    for i in range(len(covid_city)):
        covid19_sql = "UPDATE `covid19`" \
                      "SET `하루확진자`='%s', `총확진자`='%s', `격리중`='%s', `격리해제`='%s', `사망자`='%s'" \
                      "WHERE `covid19`.`시도명`='%s';" \
                      "" % (covid_day_confirmed[i].text, covid_total_confirmed[i].text, covid_total_isolation[i].text,
                            covid_total_n_isolation[i].text, covid_total_death[i].text,
                            covid_city[i].text)
        if (i >= 1 and i < len(covid_city) - 1):
            x.append(int(covid_total_confirmed[i].text.replace(",", "")))
            y.append(covid_city[i].text)
        curs.execute(covid19_sql)
        conn.commit()

    x.reverse()
    y.reverse()
    plt.figure(figsize=(20, 15))
    plt.barh(y, x)
    plt.xlabel("총확진자")
    plt.ylabel("시도명")
    plt.savefig("covid_graph.png")






Covid_chart()

driver.close()





