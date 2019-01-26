import pandas as pd
li = []
import fileinput
import re
for line in fileinput.FileInput('schedule_Sample.txt'):
    line = re.sub('^,','', line.rstrip())
    line = line.rstrip(',')
    li.append(line.split(","))
li2 = []
li3=[]
for i in li:
    if('Every 'in i[0]):
        li2.append(i)
    if('Monthly 'in i[0]):
        li2.append(i)
for i in li:
    if i not in li2:
        li3.append(i)
li3_head = li3.pop(0)
df = pd.DataFrame(li3, columns=li3_head)
display(df)
newtest = [x[0] for x in li2]
df['exact']=newtest
df.groupby(['Frequency','Report Name']).sum()