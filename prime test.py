n=eval(input("prime numbers under n， input n："))
a=[2]
d=[]
for i in range (3,n+1):
    b=0
    c=int(i/2)+1
    for m in a:
        if c>=m:
            d.append(m)
        for j in d:
            if i%j==0:
                break
            else:
                b=b+1
        if b==len(d):
            a.append(i)
print(a)
# i did not know how to do it at first, so i asked my classmates for the code and now i understood it
