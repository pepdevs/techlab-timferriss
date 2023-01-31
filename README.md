# techlab-timferriss
This project is only for educational purposes. All the original podcasts and transcipts can be found in the [Tim Ferriss Show blog](https://tim.blog/).
## Goal
Scrap Tim Ferris podcast's transcripts and save them as structured data. After it, data can be easily used in other uses cases like:  
- Get a list of words in a episode and its translation 
- Get the list of episodes where a certain word appear (useful to find episodes about a certain topic)  

## Gather data.
- **Index URL**:  https://tim.blog/2018/09/20/all-transcripts-from-the-tim-ferriss-show/
- **PDF**: Episodes #0 to #129
- **Html**: Episodes #130 to #652 (and raising)

## Technical perspective
This project is written in **Python**. I think it could also be written in Powershell / Bash but Python's community have a really nice set of libraries. Specially PDF parsing would have been difficult in some other shell script language.  
Used modules:
- [pyodbc](https://github.com/mkleehammer/pyodbc/wiki) to interact with SQL Server
- [PyPDF2](https://pypi.org/project/PyPDF2/) to extract text from PDF files (could be migrated to [pypdf](https://pypi.org/project/pypdf/))
- [wget](https://pypi.org/project/wget/) to download PDF files
- [html.parser](https://docs.python.org/es/3.8/library/html.parser.html) to scrape the transcript links from the index
- [pycurl](http://pycurl.io/) To download html file. Maybe it could be used also wget.

## Database
Database needs to be created in SQL Server. File ***db-script.sql***.

## Others
- This markdown file is created using following [syntax](https://www.markdownguide.org/basic-syntax/)
- Commit approach based in [semanting commit messages](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716)