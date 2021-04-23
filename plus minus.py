n=int(input())
arr=arr = list(map(int, input().rstrip().split()))

i=0
p=0
q=0
z=0
for i in range(len(arr)):
    if arr[i]>0:
        p+=1
    elif arr[i]<0:
        q+=1
    else:
        z+=1
plus=p/n
minus=q/n
zero=z/n
print(plus)
print(minus)
print(zero)    
