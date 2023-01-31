# techlab-timferriss
This project is only for educational purposes. All the original podcasts and transcipts can be found in the [Tim Ferriss Show blog](https://tim.blog/).
## Goal
Use Python to apply data analysis over Tim Ferris podcast's transcripts. 3 steps needed:
- **Collect the data**: All podcast transcripts can be found [here](https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/)
  - **PDF**: Episodes #0 to #150
  - **Html**: Episodes #130 to #652 (and raising)
- **Clean the data**: Parse pdf and Html files and save them as structured data (SQL Server)
- **Analyze the data**. After it, data could be used to support uses cases like:  
  - Get a list of words in a episode and its translation 
  - Get the list of episodes where a certain word appear (useful to find episodes about a certain topic)  

## Technical perspective
This project is written in **Python**. I think it could also be written in Powershell / Bash but Python's community have a really nice set of libraries. Specially PDF parsing would have been difficult in some other shell script language.  
Used modules:
- [pyodbc](https://github.com/mkleehammer/pyodbc/wiki) to interact with SQL Server
- [PyPDF2](https://pypi.org/project/PyPDF2/) to extract text from PDF files (could be migrated to [pypdf](https://pypi.org/project/pypdf/))
- [wget](https://pypi.org/project/wget/) to download PDF files
- [html.parser](https://docs.python.org/es/3.8/library/html.parser.html) to scrape the transcript links from the index
- [pycurl](http://pycurl.io/) To download html file. Maybe it could be used also wget.

## Database
- Database names Transcripts needs to be created in SQL Server (defaults to locahost). If changed, connection string in ***transcripts_repository.py*** also needs to be changed.
- Create schema using the contets of ***db-script.sql*** file.

## Others
- This markdown file is created using following [syntax](https://www.markdownguide.org/basic-syntax/)
- Commit approach based in [semanting commit messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)
- See [naming convention](https://github.com/naming-convention/naming-convention-guides/tree/master/python) used

## How to run it
- Install [Python 3.11](https://www.python.org/downloads/)
- Install Pip (Package manager for Python)
- Install dependencies
  - pip install pyodbc
  - pip install wget
  - pip install certifi
  - pip install PyPDF2
  - pip install pycurl (Only for Windows Users: Pycurl needs to be [manually downloaded](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycurl) and then install it using local path (pip install whl_path_in_local_computer)
- Create a database called Transcripts in SQL Server (defaults to localhost)
- Execute using ***python init.py***