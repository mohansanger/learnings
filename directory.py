import os
print(os.getcwd())

#Change directory
os.chdir(r"C:\Users\Mohan.2.Singh\Downloads\Test PY")
print(os.getcwd())
print(os.listdir())
#os.mkdir("Mss")
os.rename("mss","kss")
os.rmdir("kss")
os.rename