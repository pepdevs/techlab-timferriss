#PyCurl installed from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycurl
import pycurl
import certifi
from io import BytesIO
from timParser import TimParser
import wget
import os

url = "https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/"

# Creating a buffer as the cURL is not allocating a buffer for the network response
buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
c.close()

body = buffer.getvalue()
text = body.decode('iso-8859-1')

file1=open(r"intex.html","w", encoding='iso-8859-1')
file1.writelines(text)
file1.close()

parser = TimParser()
parser.feed(text)

if not os.path.exists("pdf"):
    os.makedirs("pdf")

for link in sorted(parser.LinksList):
    print(link)
    try: 
        wget.download(link, out = "./pdf")
    except:
        print(" \n \n Unable to Download A File \n")