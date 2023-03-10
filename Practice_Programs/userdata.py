from Practice_Programs.searching_a_file import SearchFiles
dirname=input("enter the dir name exapmle :D:\\data   \n")
filename=input("enter the filename with extension \n")
ob=SearchFiles()
print(ob.search(dirname,filename))