# import PyPDF2
# from PyPDF2  import PdfReader
# pdf = PdfReader('Nonimmigrant Visa - Print Application ID.pdf')
# page = pdf.pages[0]
# if page.mediabox[0]:# > page.mediabox[1]:
#     print('Portrait')
# else:
#     print('Landscape')

# box= pdf.pages[0].mediabox
# box1= pdf.pages[0].cropbox
# print(box)
# print(box.width,box.height)

# if box.height >= box.width:
#     print("Portrait")
# else:
#     print("Landscape")

# print(box1)
# #print(PdfReader.page_mode[0])



# from PyPDF2  import PdfReader
    
# pdf = PdfReader("C:/Users/Mohan.2.Singh/Downloads/Nonimmigrant Visa - Print Application ID.pdf")
# page = pdf.pages[0].mediabox

# if page.right() - page.getUpperLeft_x() > page.getUpperRight_y() - page.getLowerRight_y():
#    print('Landscape')
# else:
#    print('Portrait')
#--------------------Reading PDF -------------------------

#from PyPDF2 import PdfReader
# reader = PdfReader("C:/Users/Mohan.2.Singh/Downloads/10062022_10-6-2022_1-rotated.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text)
#--------------------Reading PDF -------------------------

from PyPDF2 import PdfReader
pdf = PdfReader(open('C:/Users/Mohan.2.Singh/Downloads/10062022_10-6-2022_1-rotated.pdf', 'rb'))
orientation = pdf.pages[0].get('/Rotate')
print(orientation)

# from PyPDF2 import PdfReader

# pdf_path = 'C:/Users/Mohan.2.Singh/Downloads/Nonimmigrant Visa - Print Application ID.pdf'
# pdf_reader = PdfReader(pdf_path)
# deg = pdf_reader.reader.pages(0).get('/Rotate')    
# page = pdf_reader.greader.pages(0).mediaBox
# if page.getUpperRight_x() - page.getUpperLeft_x() > page.getUpperRight_y() -page.getLowerRight_y():
#     if deg in [0,180,None]:
#         print('Landscape')
#     else:
#         print('Portrait')
# else:
#     if deg in [0,180,None]:
#         print('Portrait')
#     else:
#         print('Landscape')

# from PyPDF2  import PdfReader
# pdf = PdfReader(file('C:/Users/Mohan.2.Singh/Downloads/Nonimmigrant Visa - Print Application ID.pdf'))
# page = pdf.reader.pages(1)
# if page.MediaBox[3] > page.MediaBox[4]:
#     print('P')
# else:
#     print('L')