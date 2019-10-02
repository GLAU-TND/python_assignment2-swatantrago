s=input()
n=int(input())
l=[]
ss1=''
k=0
c=0
for i in range(len(s)):
    if s[i]==' ':
        c+=1#1
    if c==2:
        l.append(ss1)
        ss1=''
        c=0
        continue
    ss1=ss1+s[i]
l.append(ss1)
        
        
    
        
print(l)
        
