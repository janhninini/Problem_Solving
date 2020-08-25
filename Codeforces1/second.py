t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    if s == "1":
        print("1")
    else:
        s1 = s[n-1]*n
        print(s1)