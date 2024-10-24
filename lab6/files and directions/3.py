import os

def check_path(path):
    if os.path.exists(path):
        print("The path exists.")
        
        dirname, filename = os.path.split(path)
        print("Directory:", dirname)
        print("Filename:", filename)
    else:
        print("The path does not exist.")

path = path = r"C:\Users\epmek\Desktop\1.txt" 
check_path(path)
