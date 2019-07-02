import os
OS = os.name
if OS == "nt":
    path = 'C:\\Poisk\\'
elif OS == 'posix':
    path = 'home\\'


for rootdir, dirs, files in os.walk(path):
    for file in files:
        if ((file.split('.')[-1]) == 'txt'):
            print(os.path.join(rootdir, file))