for i in range(int(input())):
    p,f = map(int(input().split()))
    cs,cw = map(int(input().split()))
    s,w = map(int(input().split()))
    n,m = 0,0
    pn, pm = 0,0
    while(pn<=p && n<=cs):
        n = n+1
        pn = s*n
    while(pm<=p && m<=cw):
        m = m+1
        pm = s*m
    print(n+m)

