from PyPDF2 import PdfReader

debug = False

class EpisodeTalk:
    def __init__(self, speaker, speech):
        self.speaker = speaker
        self.speech = speech

def extract_text(pdfFile):
    def visitor_body(text, cm, tm, fontDic, fontSize):
        if text.strip() != '':
            if debug:
                print(f'{tm[0]} {tm[1]} {tm[2]} {tm[3]} {tm[4]} {tm[5]} {text}')

            if tm[5]<-2240:
                return

            nonlocal lastY 
            nonlocal listId 
            currentY = tm[5]
            currentX = tm[4]
            diffY = lastY - currentY
            lastY = currentY

            if diffY > 58 and currentX >= 588:
                text = "\n\n" + text;

            if currentX == 250: #Speaker name
                speaker = text.strip().rstrip(':')
                list.append(EpisodeTalk(speaker, ""))
                listId += 1
            elif currentX >= 588 and listId > -1: #Talk. >-1 comparision ignores PDF first page header
                list[listId].speech += text

    reader=PdfReader(pdfFile)
    number_of_pages = len(reader.pages)
    listId = -1
    list = []

    for i in range(number_of_pages):
        lastY=1000
        page = reader.pages[i]
        page.extract_text(visitor_text=visitor_body)

    return list