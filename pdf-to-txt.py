from PyPDF2 import PdfReader

reader=PdfReader('01-kevin-rose.pdf')
 
number_of_pages = len(reader.pages)
text = ""

def visitor_body(text, cm, tm, fontDic, fontSize):
    if (text.strip() != ''):
        print(f'{tm[0]} {tm[1]} {tm[2]} {tm[3]} {tm[4]} {tm[5]} {text}')

        if tm[5]<-2240:
            return

        global lastY 
        currentY = tm[5]
        diffY = lastY - currentY
        lastY = currentY

        if (diffY > 58):
            text = "\n\n" + text;

        parts.append(text)
        #if tm[4]==250: Speaker name
        #if tm[4]>588: Talk
    

for i in range(number_of_pages):
    lastY=1000
    parts=[]
    page = reader.pages[i]
    page.extract_text(visitor_text=visitor_body)
    pageText = "".join(parts)
    print(pageText)
    text += pageText
    

file1=open(r"01-kevin-rose.txt","w")
file1.writelines(text)
file1.close()