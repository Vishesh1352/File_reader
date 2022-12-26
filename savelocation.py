import shutil
import os
def save_location(exist,des_path,dist):
    dir_name=""
    if os.path.exists(des_path):
        for v in dist:
         dir_name+=" "+ v
        mypath=os.path.join(des_path,dir_name)

        if not os.path.exists(mypath):
         os.mkdir(mypath)

        else:
            shutil.rmtree(mypath)
            os.makedirs(mypath)

        if len(exist) != 0:
         for i in exist:
            shutil.copy(i,mypath)
         mypath=mypath.split("\\")
         print("The file(s) are stored in directory called " + mypath[len(mypath)-1])
        elif os.path.exists(des_path)== False:
         print("Error: ---There is no such DIR found ---")