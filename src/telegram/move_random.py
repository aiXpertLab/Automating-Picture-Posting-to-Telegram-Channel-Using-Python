import os, random, shutil

#Prompting user to enter number of files to select randomly along with directory
source="E:/gDrive/38.Pic/Tele"
dest  ="E:/gDrive/38.Pic/Tele/web"

random_file=random.choice(os.listdir(source))
print(random_file)
source_file="%s/%s"%(source,random_file)
print(source_file)
dest_file=dest
shutil.move(source_file,dest_file)
