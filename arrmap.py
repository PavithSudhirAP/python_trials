arr = list(map(int, input().split()))
arr.sort()
print(arr)
win = arr[-1]
print(win)
while win in arr:
   arr.remove(win)
print(arr[-1])