from itertools import combinations_with_replacement

n = int(input("enter N: "))
k = int(input("enter K: ")) 
N = [x for x in range(1,n+1)]
ans = []
Nk = []
a=[]

if k == 1:
    for item in N:
        a = []
        a.append(item)
        ans.append(a)
     
else:
    ans = list(combinations_with_replacement(N, k))
    
    for item in ans:
        for i in range(k-1):
            if item[i+1] % item[i] !=0:
                ans.remove(item)

print(len(ans))

