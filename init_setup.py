import os

print("Start")
print("creating environment")
os.system("conda create --prefix ./env python=3.7 -y")
print("activate environment")
os.system("source activate ./env")
print("Intsall Requirements")
os.system("pip install -r requirements.txt")
print("End")
