import os 
import sys
cwd = os.getcwd()
print(cwd)
newdir = os.chdir('.././data/PUB/')

print(newdir)
# print(pub_real_dir)


# for (dirs, subDir, files) in os.walk(newdir):
#     print(files)

print(sys.platform)