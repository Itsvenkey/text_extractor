from pypdf import PdfReader

name = 'sample'
reader = PdfReader(r'./pdf/'+name+'.pdf')

print(len(reader.pages))


for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)


    
