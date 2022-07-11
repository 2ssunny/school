import requests
from bs4 import BeautifulSoup

crawling=open("D:\Coding\school\deposit\crawling.txt", "w")
url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bkVI&qvt=0&query=%EC%9D%80%ED%96%89%20%EC%98%88%EA%B8%88'

response = requests.get(url)

name_list=[]
basic_list=[]
max_list=[]

html = response.text
soup = BeautifulSoup(html, 'html.parser')

for a in range(1,31):
    for b in range(1,7):
        name = soup.select_one(f'#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({a}) > div > div > div:nth-child({b}) > div > div > div.title > div > strong > a')
        name_list.append(name.text)
        print (name_list)
        crawling.write(str(name_list))
    break


for c in range(1,31):
    for d in range(1,7):
        inter_basic = soup.select_one(f'#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({c}) > div > div > div:nth-child({d}) > div > div > div.info > dl > dd:nth-child(4) > span > strong')
        basic_list.append(inter_basic.text)

for e in range(1,31):
    for f in range(1,7):
        inter_max = soup.select_one(f'#main_pack > section.sc_new.cs_common_module.case_list.color_1._cs_interest_rate > div.cm_content_wrap > div > div > div._list._panel_wrapper > div:nth-child({e}) > div > div > div:nth-child({f}) > div > div > div.interest_info > span > em')
        max_list.append(inter_max.text)

for g in range(1,211):
    crawling.write(str(name_list[g]))
    crawling.write(basic_list[g])
    crawling.write(max_list[g])