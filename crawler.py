import urlparse
import urllib
import subprocess
from bs4 import BeautifulSoup
#clean the screen
subprocess.call('clear',shell=True)
#input 
url = raw_input("Enter an url to start: ")
if "http" not in url:
	url="http://"+url
#initialize the queue
urls=[url]     		#queue of urls
visited = [url]		#historic record of urls, check if visted before enque
print "-"*60
print "start crawling from: "+url
print "-"*60
while len(urls)>0:	#while queue is not empty
	try:
		htmltext=urllib.urlopen(urls[0]).read()	#get http respond
	except:
		print urls[0]
	soup = BeautifulSoup(htmltext)			#use beautifulsoup
	
	urls.pop(0)					#deque the url handled
	for tag in soup.findAll('a',href=True):		#find all <a> tag
		tag['href']=urlparse.urljoin(url,tag['href'])	
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])
			print tag['href']
print "there are "+str(len(visited))+" urls visted."
