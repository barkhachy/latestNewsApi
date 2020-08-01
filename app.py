from lxml import html
from flask import *
import json
import requests
import os
import re
from collections import OrderedDict 

app = Flask(__name__)


@app.route('/news',methods = ['GET','POST'])
def home():
    if request.method=='GET':
	url = "https://time.com/"
	res = requests.get(url = url)
	tree = html.fromstring(res.content )
	#print(tree)
	li = []
	for i in range(1,6):
		tmp = str(i)
		sec = '/html/body/div[1]/section[5]/ol/li[' + tmp + ']/article/div/h2/a/text()'
		link1 = '/html/body/div[1]/section[5]/ol/li[' + tmp + ']/article/div/h2/a/@href'
		#print(sec, link1)
		data = str(tree.xpath(sec))
		data2 = str(tree.xpath(link1))
		obj1 = {}
		obj1["title"] = data[2:len(data)-2]
		obj1["link"] = url[:len(url)-1]+data2[2:len(data2)-2]
		li.append(obj1)
	j = json.dumps(li,  separators=(",\n ", ":"))
	#print (j)
	return j
        

if __name__=="__main__":
    app.debug = True
    app.run(host = "0.0.0.0",port = 5000)
