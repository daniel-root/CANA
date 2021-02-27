def Heap(v,ini,t):
    for i in range(ini,t):
        cab = int(i/2)
        if v[i]>v[cab]:
            aux = v[i]
            v[i]=v[cab]
            v[cab]=aux
            if cab>1:
                return Heap(v,cab,t)
    return v
def Sort(v,t):
    while t>2:
        aux = v[1]
        v[1] = v[t-1]
        v[t-1]=aux
        t=t-1
        Heap(v,2,t)
    return v
v = [None,11,9,5,26,2,15,67,4,10,6]
print(Heap(v,2,len(v)))
print(Sort(v,len(v)))
a = [None,4,10,3,5,1]
print(Heap(a,2,len(a)))
print(Sort(a,len(a)))