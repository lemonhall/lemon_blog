# importing the modules
from bs4 import BeautifulSoup
import os,sys
import requests
import logging
import sqlite3
import datetime
log = logging.getLogger(__name__)
#https://docs.python.org/3/library/sqlite3.html
con = sqlite3.connect('sync.db')
cur = con.cursor()

# Create table
# cur.execute('''CREATE TABLE sync (id text, title text, href text, status int, time timestamp)''')

#这个主函数其实干的事情很简单，就是扫描某一个豆列，把所有的条目和sqlite数据库做比对
#把页面上有，而数据库里没有的数据插入到表里面去就结束了
#这个脚本最好是每几个小时就运行一次，然后就能扫描到需要处理的豆瓣日记了
#然后紧接着就可以运行cookbook_extractor.py，那个脚本拿过来稍微改一改就可以用了
#最后用一个shell脚本，串行化这个过程即可，先运行扫描器，再运行抽取器，一气呵成
def scraping(url):
	debug = {'verbose': sys.stderr}
	headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'}
	page = requests.get(url,headers=headers)
	page.encoding = 'utf-8'
	soup = BeautifulSoup(page.text, 'html.parser')
	#print(soup)
	#找到所有的items
	items = soup.find_all("div", class_="doulist-item")
	#print(notes_items)
	sync_counter = 0
	#处理列表里的每一个元素
	for item in items:
		#该条目的id编码
		id              = item["id"]
		title_container = item.find("div", class_="title")
		#如果可以拿到title元素
		if title_container :
			title_link = title_container.find("a")
			#如果可以拿到a元素
			if title_link:
				#该条目的超链接
				title_link_href = title_link["href"]
				#该条目的文字标题
				title_text      = title_link.text.rstrip().lstrip()
				saved_in_db = cur.execute("SELECT * FROM sync WHERE id=:id", {"id": id})
				if saved_in_db.fetchall():
					#数据库里查到了条目，暂时不需要去管它是什么状态，直接跳过就好
					pass
				else:
					#数据库里没有这个条目则插入之
					print("I am going to be synced....")
					sync_counter = sync_counter +1
					print(id)
					print(title_text)
					print(title_link_href)
# cur.execute('''CREATE TABLE sync (id text, title text, href text, status int, time timestamp)''')
					cur.execute("insert into sync values (?,?,?,?,?)", (id,title_text,title_link_href,0,datetime.datetime.now()))
	#提交所有不在数据库里，需要同步的数据库的记录
	con.commit()
	if not sync_counter:
		print("Nothing to be sync....."+ str(datetime.datetime.now()))

#=========main=============#
#python3 main.py https://www.douban.com/doulist/122405820/
s_url = sys.argv[1]
scraping(s_url)
con.close()
