with open("num.txt") as file_object:
    contents = file_object.read()
print(contents)

fout = open('pi.txt', 'rt')
pi = fout.read()
fout.close()
print(pi)

path = 'D:\\_WorkPlace\\#1 Разработка\\LessonPy\\Lessons-Intro\\lesson-file\\num.txt'

with open(path) as file_object:
    contents = file_object.read()
print(contents)

print("+++++")
# read line
f3 = 'data.txt'
with open(f3) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(f3) as file_obj:
    lines_list = file_obj.readlines()
print(lines_list)

for line in lines_list:
    print(line.rstrip())

# 

filename = 'pi.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))


# write to file

f4 = 'lang.txt'
with open(f4, 'w') as myfile:
    myfile.write("Russian lang in pc - 1C :)\n")
    myfile.write("Eng lang in pc - Python :)\n")

with open(f4, 'a') as myfile:
    myfile.write("i love programming \n")
