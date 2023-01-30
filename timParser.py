from html.parser import HTMLParser

class  TimParser(HTMLParser):
    #creating lists to parse the data in
    StartTags_list = list()
    EndTags_list = list()
    StartEndTags_list = list()
    Comments_list = list()
    LinksList = set()
    
    def  handle_starttag(self, startTag, attrs):
        if startTag=='a':
            for attr in attrs:
                if attr[0]=='href' and "wp-content/uploads/" in attr[1]:
                    self.LinksList.add(attr[1])
        self.StartTags_list.append(startTag)
    def  handle_endtag(self, endTag):
        self.EndTags_list.append(endTag)
    def  handle_startendtag(self,startendTag, attrs):
        self.StartEndTags_list.append(startendTag) 
    def  handle_comment(self,data):
        self.Comments_list.append(data)