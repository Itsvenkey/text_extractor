from pypdf import PdfReader

#name of the file in the directory pdf
name = 'sample'

#pdf reader from the pypdf library to read the pdf file from the given directory
reader = PdfReader(r'./pdf/'+name+'.pdf')

#printing the number of pages
print(len(reader.pages))


#printing the data from the pdf file from its each page
for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)


    
