s="WATER"
s1=s[0:len(s)//2]
s2=s[len(s)//2:]
s3=s2+s1
print
l1=list(s3)
print(l1)
for i in range(1,len(s3)+1):
    s4=""
    for j in range(0,i):
        s4+=s3[j]
        print(s4)