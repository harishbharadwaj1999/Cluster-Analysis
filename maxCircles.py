def maxCircle(queries):
    s=0
    d={}
    seen=set()
    for i in queries:
        a,b=i
        seen.add(a)
        seen.add(b)
        if d.get(a,None)==None:
            d[a]=[b]
        else:
            d[a].append(b)
        if d.get(b,None)==None:
            d[b]=[a]
        else:
            d[b].append(a)
    c=0
    seen=list(seen)
    for k in seen:
        t=[k]
        s=[k]
        while(True):
            for i in s:
                for j in d[i]:
                    if j not in s:
                        s.append(j)
                        seen.remove(j)
            if t==s:
                break
            else:
                t=s
        c+=1
    return c
