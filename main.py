import os
path = input("Give Your Folder path : ")
file = open('data.csv', 'a')
def write_name(name):
    file.write(name+"\n")


x = os.listdir(path)
drive = '00'
for i in x:
    print(i+"\n")
    link = input("Give ttid: ")
    if link!='0':
        
        link = link[8:]
        x = link.split('/')
        print(x[2])
        ttid = x[2]
        data = ttid+','+i+','+path[2:]+','+drive
        write_name(data)

file.close()
    
