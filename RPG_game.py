n = int(input("enter no. of monsters: ")) 
e = int(input("enter initial experiance: "))
power = []
bonus = []
defeated = 0
for i in range(0,n):
  p = int(input("enter powers of monster in order: "))
  power.append(p)

for i in range(0,n):
  b = int(input("enter bonus after defeating monster in order: "))
  bonus.append(b)

for l in range(0,n) :
  for i in power:
    if e >= i:
      # monster is defeated
      defeated+=1
      # add bonus to player exp
      index = power.index(i)
      e = e + bonus[index]
      del power[index]
      del bonus[index]
    
print(defeated)
