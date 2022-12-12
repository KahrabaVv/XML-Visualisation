import re
file1 = open("E:\sample.xml", 'r')
Lines = file1.readlines()
f = open("E:\sample2.xml", 'w')
def smallest_between_two(a, b, text):
    return re.findall(re.escape(a)+"(.?)"+re.escape(b),text)
open_tag=[]
close_tag=[]
count=-1
flag_close=False
flag_data=True
f.writelines(Lines[0])
for line in Lines[1:]:
    flag_data=True
    flag_close=False
    size=len(smallest_between_two('<', '>',line ))
    if(size!=0):
        for tag in smallest_between_two('<', '>',line ):
            flag_data=False
            if("/" in tag):
                close_tag.append(tag)
                flag_close=True
            else:
                open_tag.append(tag)
                count+=1
    if(flag_data):
        count+=1
    f.writelines("\t"*count+line)
    if(flag_close or flag_data):
        count=count-1