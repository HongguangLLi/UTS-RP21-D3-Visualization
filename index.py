
import threading
import time
import requests
import re
import json

def action(arr):
    print(len(arr))
    for i in arr:
        url = 'https://dblp.uni-trier.de/search/author/api?&q='+i+'&p=2&h=6&c=0&format=jsonp&compl=score&rd=2d&_=1629091570276'
        try:
            result = requests.get(url)
            bb = re.search('callback\((.*)\)', str(result.content)).group(1)
            res = json.loads(bb.replace(r'\r\n','').replace('\\','\\\\'))
            info = res['result']['hits']['hit'][0]['info']
            if "note" in info:
                note = info['note']
            else:
                note = ""
            if "Australia" in note or "australia" in note:
                with open("in.txt","a+",encoding='utf-8') as f:
                    f.write(i[:len(i)-1]+"---"+note+"\n")
            else:
                with open("out.txt","a+",encoding='utf-8') as f:
                    f.write(i[:len(i)-1]+"---"+note+"\n")
        except:
            with open(".txt","a+",encoding='utf-8') as f:
                f.write(i)
        time.sleep(0.01)

threads = []   
with open("./data.txt","r",encoding='utf-8') as f:
    a = f.readlines()
    for i in range(40):
        th = threading.Thread(target=action, args=(a[i*1000:(i+1)*1000],))
        threads.append(th)    
for th in threads:
    th.start() 

for th in threads:
    th.join() 
