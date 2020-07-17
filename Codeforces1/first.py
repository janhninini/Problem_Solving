t = int(input())
for i in range(t):
  l = list(map(int, input().split()))
  x = l[0]
  y = l[1]
  z = l[2]
  if x != y and y != z and x != z:
    print("NO")
  elif (x==y and x==z):
    print("YES")
    print(x, y,z)
  elif (x==y and x>z) :
    a = x
    b = z
    c = 1
    print("YES")
    print(a,b,c)
  elif (x==z and x>y):
    a = x
    b = y
    c = 1 
    print("YES")
    print(a,b,c)
  elif (y==z and y>x):
    a = x
    b = y
    c = 1 
    print("YES")
    print(a,b,c)
  else:
    print("NO")
