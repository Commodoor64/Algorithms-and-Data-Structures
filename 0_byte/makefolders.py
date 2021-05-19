import os
program = open('run.go','r').readlines()
print(program)
count = 1
directory1 = "C:/Users/xandi-pink/Desktop/Code\Algorithms and Data Structures/0_byte/code"


for line in program:
    for i in line:
        if i == ' ':
            i = '_'
        else:
            break
    line = line.replace("/", "{slash}")
    line = line.replace(":", "{col}")
    line = line.replace("*", "{star}")
    line = line.replace('"', "{quote}")
    line = line.replace("<", "{leftcarrot}")
    line = line.replace(">", "{rightcarrot}")
    line = line.rstrip("\n")
    print('line: ' + line)
    path = os.path.join(directory1,str(count) + line)
    os.mkdir(path)
    count+=1

