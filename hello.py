print("hello world")
print ('*'*70)
data=[]
fr=open('1.txt')
for line in fr.readlines():
    line=line.strip()
    data_line=line.strip("\t")
    data.append(data_line)
print(data[0])
fr.close()    
f=open('1.txt','a+')
f.write('i love you!')
f.close()