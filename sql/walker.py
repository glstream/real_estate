import os 
import sys
cwd = os.getcwd()
print(cwd)
newdir = '/home/pi/Documents/project-file/real_estate/pdfs/'

print(newdir)
# print(pub_real_dir)


for (dirs, subDir, files) in os.walk(newdir):
    print(files)

print(sys.platform)

/home/pi/Documents/project-file/real_estate/pdfs/KCBreakouts_Oct.pdf