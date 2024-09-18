
import requests
import re
from bs4 import BeautifulSoup
url='https://cn.bing.com/sportsdetails?q=%E5%8E%86%E5%B1%8A%E5%A5%A5%E8%BF%90%E4%BC%9A%E9%87%91%E7%89%8C%E6%8E%92%E5%90%8D&sport=Olympics&TimezoneId=China%20Standard%20Time&intent=Standings&isolympics=True&segment=sports&isl2=true&form=QSRE4&'
resp=requests.get(url)
resp.encoding='UTF-8'
html_content = resp.text

soup = BeautifulSoup(html_content, 'html.parser')

# 假设每个国家的金牌数都在class为'gold-medal'的<div>内
gold_medals = []
for div in soup.find_all('div', class_='bsp_row_teamname'):
    # 这里需要根据你的HTML结构调整.text或.get_text()等方法的使用
    country_name = div.find_previous('h3').text  # 假设国家名在金牌数前的<h3>标签内
    gold_count = div.text.strip()  # 去除金牌数周围的空白字符
    gold_medals.append((country_name, gold_count))