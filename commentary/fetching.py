from urllib.request import Request, urlopen
import pyttsx3
from pathlib import Path
import os
from .models import Comm

url="https://www.cricbuzz.com/live-cricket-scores/36336/aus-vs-eng-2nd-test-the-ashes-2021-22"

#for defining base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# TO stop or start a function
act=True

# queue for storing the commentary files     and stores upto 10 files. Refreshes after that
que=[]

# Clearall function to emppty the que and delete the media. Runs on startup
def clearAl():
    folder=r"./media"
    while(len(que)):
        curr=que.pop(0)
        name=str(curr)
        mpformat=name+".mp3"
        fullname=folder+"\\"+mpformat
        os.remove(fullname)

#main fucntion 

def conti(url):
    url=url.replace("www","m")
    old=""
    while(act):
        new=commentary(url)
        
        
       
        if old in new and old!=new:
            print(new)
            name=checkingque(new)
            saving(new,name)
            # print(que)
            # saving(new)
            # speaking(new[len(old):])
            old =new
        elif old!=new:
            
            print(new)
            name=checkingque(new)
            # saving(new)
            saving(new,name)
            # speaking(new)
            # print(que)
            old=new
            


# function to name the next file
# also limits queue size to a given number
def checkingque(txt):
    num=10
    if len(que)==num:
        
        folder=r"./media"
        curr=que.pop(0)
        name=str(curr)
        mpformat=name+".mp3"
        fullname=folder+"\\"+mpformat
        os.remove(fullname)

    if len(que)>0:
        name=que[-1]+1
    else:
        name=1
    que.append(name)
    return str(name)
    

# function to scrap ball by ball commentary from html
def scraper(html):
    start_index = html.find("commtext") + len("commtext")+2
    end_index = html[start_index:].find("</p>")

    mytext=html[start_index:start_index+end_index]
    op=html[start_index+end_index:]
    return mytext,op



# Function to fetch the html page for given url

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


     
# function for text to speech conversion and playing on the go with runAndWait loop

def speaking(txt):
    speak = pyttsx3.init()
    # rate = speak.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    speak.setProperty('rate', 150)
    if len(txt):
    
        speak.say(txt)
        speak.runAndWait()



# function for saving text to speech conversion as an audio file(mp3)
def saving(txt,name):
    speak = pyttsx3.init()
    # rate = speak.getProperty('rate')   # getting details of current speaking rate
    # print (rate)                        #printing current voice rate
    speak.setProperty('rate', 150)
    
    folder=r"./media"
    mpformat=name+".mp3"
    fullname=folder+"\\"+mpformat
    # na=r"media/nam.mp3"

    speak.save_to_file(txt, fullname)
    speak.runAndWait() 
    print("saved!!")



# function to extract audio file name to be played
def toplay():
    if len(que):
        folder=r"./media"
        curr=que.pop(0)
        name=str(curr)
        mpformat=name+".mp3"
        fullname=folder+"\\"+mpformat
        return fullname,name
    else:
        return None,None



# Function to add the media file as a model object
# Render the player on page and play
# Delet the item from queue, media and DB after finishing.
# Yet to be updated for adding a model object and deleting it. 
# Doesn't play the audio as of now. Only works for media and queue. 
# Still in progess...

def playing():
    curr,title=toplay()
    if curr:
        # write function to save the file as model object
        # Display player in UI
        # Find out when file is played once
        #......
        com=Comm()
        Comm.title=title
        Comm.audio_file=curr

        #write function to delete the file from DB after played once
        # 
        #....
        os.remove(curr)


