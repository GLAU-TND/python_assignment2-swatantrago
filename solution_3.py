def check(a):
    c=0
    for i in range(len(a)):
        for j in range(0,i):
            if a[j]>a[i]:
                c+=1
            if c>1:
                return False
    else:
        return True

Arr=eval(input('Enter the Array\n'))
print(check(Arr))