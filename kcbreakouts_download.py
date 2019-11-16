import requests 

file_url = "https://www.nwmls.com/library/CorporateContent/statistics/KCBreakouts.pdf"

pdf_file = '/Users/gstream/Documents/ST/playground/pdf_breakouts/pdfs/TEST.pdf'

r = requests.get(file_url, stream = True) 
  
with open(pdf_file,"wb") as pdf: 
    for chunk in r.iter_content(chunk_size=1024): 
         # writing one chunk at a time to pdf file 
         if chunk: 
             pdf.write(chunk)

