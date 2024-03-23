t = int(input())

for i in range(t):
    s = input()
    slist = list(s)
    for j in range(2,len(slist)):
        for k in range(int(slist[0])):
            print(slist[j],end='')
    print('')   
