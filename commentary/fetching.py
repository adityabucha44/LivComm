

from urllib.request import Request, urlopen
import pyttsx3
# url=input()
url="https://www.cricbuzz.com/live-cricket-scores/36336/aus-vs-eng-2nd-test-the-ashes-2021-22"

act=True

def conti(url):
    url=url.replace("www","m")
    old=""
    while(act):
        new=commentary(url)
        if old in new and old!=new:
            print(new)
            speaking(new[len(old):])
            old =new
        elif old!=new:
            print(new)
            speaking(new)
            old=new
            
     
def scraper(html):
    start_index = html.find("commtext") + len("commtext")+2
    end_index = html[start_index:].find("</p>")

    mytext=html[start_index:start_index+end_index]
    op=html[start_index+end_index:]
    return mytext,op


def commentary(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()
    
    html = page.decode("utf-8")

    ret=scraper(html)
    mytext=ret[0]
    html=ret[1]
    summary=""
    flag=1
    while(flag):
        if ("span id=" in mytext):
            ret=scraper(html)
            mytext=ret[0]
            html=ret[1]
        elif ('class="over-summary"' in mytext):
            summary=mytext
            ret=scraper(html)
            mytext=ret[0]
            html=ret[1]
        else:
            flag=0

            
    if summary!="":
        mytext= mytext+"\n <strong> over summary .</strong>  \n" +summary
    return mytext


     
def speaking(txt):
    speak = pyttsx3.init()
    # rate = speak.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    speak.setProperty('rate', 150)
    if len(txt):
    
        speak.say(txt)
        speak.runAndWait()

  