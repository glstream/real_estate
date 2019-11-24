import sys

if (sys.platform == 'win32'):
    pdf_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\pdfs\\'
    raw_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\data\\RAW\\'
    out_dir = 'C:\\Users\\grayson\\Documents\\project-folder\\realestate\\real_estate\\data\\PUB\\'
elif sys.platform == 'darwin':
    pdf_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/pdfs/'
    raw_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/data/RAW/'
    out_dir = '/Users/glstream/Documents/GitHub/home_prices/real_estate/data/PUB/'
elif sys.platform == 'linux':
    pdf_dir = '/home/pi/Documents/project-file/real_estate/pdfs/'
    raw_dir = '/home/pi/Documents/project-file/real_estate/data/RAW/'
    out_dir = '/home/pi/Documents/project-file/real_estate/data/PUB/'