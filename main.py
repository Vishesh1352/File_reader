import os
from collections import defaultdict

import docx2txt
import PyPDF2

from savelocation import save_location
from serchtext import serch_word

exist=[]
keywords=[]
dist=defaultdict(list)

keyinput= input("Please Enter Keywords seprated by space :")
keywords=keyinput.split()
ch=input("\nIf you want the file to contain all the given keyword Press Y otherwise N :")
dir_path= input("Enter a path from where you want to read:")

if os.path.exists(dir_path):
 for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path,file)
    
    if os.path.isfile(cur_path):
      if file.endswith(".txt"):
       with open(cur_path,'r',encoding='utf-8') as file:
        content=file.read()
        content=content.lower()
        serch_word(cur_path,keywords,content,ch,exist,dist)
      
      elif file.endswith(".docx") or file.endswith(".doc"):
       content=docx2txt.process(cur_path)
       content=content.lower()
       serch_word(cur_path,keywords,content,ch,exist,dist)

      elif file.endswith(".pdf"):
        contentopen= open(cur_path,'rb')
        contentread=PyPDF2.PdfReader(contentopen)
        size=len(contentread.pages)
        if len(contentread.pages) > 1:
          for i in range(contentread.pages[0],contentread.pages[size]):
            content=contentread.pages[i]
            content=content.extract_text()
            serch_word(cur_path,keywords,content,ch,exist,dist)

        else:
         content=contentread.pages[0]
         content=content.extract_text()
        serch_word(cur_path,keywords,content,ch,exist,dist)

if len(exist) != 0:
  for key in dist.keys():
      print("\nkeyword "+key.upper()+" exists in the following :")
      #for value in dist.values():
      for i in dist[key]:
        print(i)

  exist= set(exist)
  print("\nDo you wish to copy files containing keywords")
  copy_choice=input("\nPress Y for yes and N for no :")

  if copy_choice=="Y":
   print("Please input the PATH where you want to copy files")
   des_path=input("It will be copied to current file by default :")
   if des_path == None or " ":
    des_path=dir_path
   save_location(exist,des_path,dist)

  else:
   print("You have chhosen note to copy files in different locatin.")

elif os.path.exists(dir_path) == False:
  print("There is no such dir avaible.")