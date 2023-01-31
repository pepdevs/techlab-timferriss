#PyCurl installed from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycurl
import pycurl
import certifi
from io import BytesIO
from timParser import TimParser
import wget
import os
import shutil

url = "https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/"
tempFolder = "temp"
pdfFolder = "pdf"
encoding ='iso-8859-1'

# Create empty pdf and temp folder. If already exist, remove their contents
if os.path.exists(pdfFolder):
    shutil.rmtree(pdfFolder)

os.makedirs(pdfFolder)

if os.path.exists(tempFolder):
    shutil.rmtree(tempFolder)

os.makedirs(tempFolder)

# Download transcript's index
buffer = BytesIO()

c = pycurl.Curl()
c.setopt(c.URL, url)
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.CAINFO, certifi.where())
c.perform()
c.close()

body = buffer.getvalue()
text = body.decode(encoding)

file1=open(f"{tempFolder}/index.html","w", encoding=encoding)
file1.writelines(text)
file1.close()

# Parse index file and download Pdf files to /pdf folder
parser = TimParser()
parser.feed(text)

for link in sorted(parser.LinksList):
    print(link)
    try: 
        wget.download(link, out = f"./{pdfFolder}")
    except:
        print(" \n \n Unable to Download A File \n")