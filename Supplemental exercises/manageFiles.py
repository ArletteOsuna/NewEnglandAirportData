import os, os.path, shutil
while True:
    choice = input ("""    1 - List Files
    2 - Copy Images
    3 - Quit
    Enter choice: """)
    
    if choice == "1":
        
        # List Files
        dirpath = input("Enter directory path or <Enter> for the current directory:\n   ")
        ext = input("Enter file extension with dot, or <Enter> for all files: ")
        if dirpath == "":
            currentDirectoryPath = os.getcwd()
        else:
            currentDirectoryPath= dirpath   
        listofFileNames = os.listdir(currentDirectoryPath)
        for fname in listofFileNames:
            if ext == "" or ext.upper() in fname.upper():
                print ("%20s - %6d bytes"%(fname, os.path.getsize(fname)))
        print ("\n")
    elif choice == "2":
    # Copy Images
        dirpath = input("Enter directory path or <Enter> for the current directory:\n   ")
        IMAGE_EXTENSIONS = (".jpg", ".gif", ".jpeg", ".png", ".bmp")  # this is a tuple!
        if dirpath == "":
            currentDirectoryPath = os.getcwd()
        else:
            currentDirectoryPath= dirpath   
        listofFileNames = os.listdir(currentDirectoryPath)
        for fname in listofFileNames:
            fnp = fname.rsplit(".")[0]  # get the file name part
            ext = "." + fname.rsplit(".")[-1]  # get the extension, include the dot
            if ext in IMAGE_EXTENSIONS:
                newfname = fnp+"_copy"+ext
                shutil.copyfile(fname, newfname)
                print ("Copied {0} to {1}".format(fname, newfname))  # note the format string here
             
                
        print ("\n")
    else:
    # Quit
        break
