from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
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



def COVID_CHART():
    chart_url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdGubun=13"

    driver.get(chart_url)
    html = driver.page_source
    soup = bs(html, "html.parser")

    city = soup.find("tbody").find_all("th")
    day_confirmed = soup.find_all("td", {"headers": "status_level l_type1"})
    total_confirmed = soup.find_all("td", {"headers": "status_con s_type1"})
    total_isolation = soup.find_all("td", {"headers": "status_con s_type2"})
    total_n_isolation = soup.find_all("td", {"headers": "status_con s_type3"})
    total_death = soup.find_all("td", {"headers": "status_con s_type4"})

    '''
    # INSERT
    for i in range(len(city)):
        sql = "INSERT INTO `covid_chart`(`시도명`, `일일확진자`, `총확진자`, `격리중`, `격리해제`, `사망자`) " \
                      "VALUES('%s', '%s', '%s', '%s', '%s', '%s');" \
                      "" % (city[i].text, day_confirmed[i].text, total_confirmed[i].text,
                            total_isolation[i].text, total_n_isolation[i].text, total_death[i].text)
        print(sql)
        curs.execute(sql)
        conn.commit()
    '''
    x = []
    y = []
    for i in range(len(city)):
        sql = "UPDATE `covid_chart`" \
                      "SET `일일확진자`='%s', `총확진자`='%s', `격리중`='%s', `격리해제`='%s', `사망자`='%s'" \
                      "WHERE `covid_chart`.`시도명`='%s';" \
                      "" % (day_confirmed[i].text, total_confirmed[i].text, total_isolation[i].text,
                            total_n_isolation[i].text, total_death[i].text,
                            city[i].text)
        if (i >= 1 and i < len(city) - 1):
            x.append(int(total_confirmed[i].text.replace(",", "")))
            y.append(city[i].text)
        curs.execute(sql)
        conn.commit()

    x.reverse()
    y.reverse()
    plt.figure(figsize=(20, 15))
    plt.barh(y, x)
    plt.xlabel("총확진자")
    plt.ylabel("시도명")
    for a, b in zip(x, y):
        plt.text(a, b, str(a), fontsize=20, horizontalalignment='left', verticalalignment='center')
    plt.savefig("C:/Bitnami/wampstack-7.1.16-0/apache2/htdocs/crawling_covid19/covid_graph.png")


def COVID_MESSAGE():

    message_url = "https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgList.jsp?menuSeq=679"

    driver.get(message_url)
    driver.find_element_by_id("bbs_tr_0_bbs_title").click()

    for i in range(10):
        html = driver.page_source
        soup = bs(html, "html.parser")

        date = soup.find("h3", {"id": "sj"}).text.split()[0]
        time = soup.find("h3", {"id": "sj"}).text.split()[1]
        contents = (soup.find("div", {"id": "cn"}).text.split("-송출지역-")[0])[0:300]

        '''
        # INSERT
        sql = "INSERT INTO `covid_message`(`날짜`, `시간`, `내용`)" \
                  "VALUES('%s', '%s', '%s');" \
                  "" % (date, time, contents)
        curs.execute(sql)
        conn.commit()
        '''

        sql = "UPDATE `covid_message`" \
              "SET `날짜`='%s', `시간`='%s', `내용`='%s'" \
              "WHERE `covid_message`.`no`='%d';" \
              "" % (date, time, contents, i+1)
        curs.execute(sql)
        conn.commit()

        driver.find_element_by_id("bbs_gubun").click()





COVID_CHART()
COVID_MESSAGE()

driver.close()





