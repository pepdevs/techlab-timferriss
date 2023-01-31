from PyPDF2 import PdfReader

def extract_text(pdfFile):
    def visitor_body(text, cm, tm, fontDic, fontSize):
        if (text.strip() != ''):
            print(f'{tm[0]} {tm[1]} {tm[2]} {tm[3]} {tm[4]} {tm[5]} {text}')

            if tm[5]<-2240:
                return

            nonlocal lastY 
            currentY = tm[5]
            diffY = lastY - currentY
            lastY = currentY

            if (diffY > 58):
                text = "\n\n" + text;

            parts.append(text)
            #if tm[4]==250: Speaker name
            #if tm[4]>588: Talk

    reader=PdfReader(pdfFile)
    number_of_pages = len(reader.pages)
    text = ""

    for i in range(number_of_pages):
        lastY=1000
        parts=[]
        page = reader.pages[i]
        page.extract_text(visitor_text=visitor_body)
        pageText = "".join(parts)
        print(pageText)
        text += pageText

    txtFile = pdfFile.split('.')[0]
    file1=open(f"{txtFile}.txt","w")
    file1.writelines(text)
    file1.close()