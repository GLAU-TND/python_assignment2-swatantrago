def con(l,su):
    j=0
    s=0
    
    for i in range(len(l)):
        ll=[]
        if i==0:
            for j in range(len(l)):
                s+=l[j]
##                print(s)
                ll.append(l[j])
##                print(ll)
                if s==su:
                    return ll
        elif i>0:
            n=i-1
            s=0
            while n<len(l):
                s+=l[n]
##                print(s)
                ll.append(l[n])
##                print(ll)
                n+=1
                if s==su:
                    return ll
l=eval(input())
k=int(input())
print(con(l,k))
