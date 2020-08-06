from flask import *
import json
import requests
import os
import re
from collections import OrderedDict 
import urllib

app = Flask(__name__)

@app.route('/news')
def top_news():
	url = "https://time.com/"	
	response = urllib.request.urlopen("https://time.com/")
	html = response.read()
	#print(type(html))
	text = html.decode()
	#print(type(text))
	start = text.find("Latest Stories")+len('Latest Stories">')
	#print(start)
	finish = text.find("</section>", start)
	#print(text[start:finish])
	li = []
	while start < finish:

		link_pos = text.find("<a href", start)
		if link_pos < finish:
			link_finish = text.find(">", link_pos)
			#print(text[link_pos:link_finish])
			text_start = text.find(">", link_finish)
			text_finish = text.find("</a>",text_start)
			#print(text[text_start:text_finish])
			obj1 = {}
			obj1["title"] = text[text_start+1:text_finish]
			obj1["link"] = url+text[link_pos+9:link_finish]
			li.append(obj1)
			start = text_finish
		else:
			break
		
	j = json.dumps(li, separators=(",\n ", ":"))
	#print (j)
	return j

if __name__=="__main__":
    app.debug = True
    app.run(host = "0.0.0.0",port = 5000)
