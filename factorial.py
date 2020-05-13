n=int(input("enter factorial number - "))
a= pow(n,2)
print("squre of ",n ,"is",a)
c=1
for i in range(n):
    c= c*n
    n=n-1

print("factorial is ",c)

