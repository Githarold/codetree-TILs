s = input()
s1 = s.upper()
slist = list(s1)
ulist = list(set(slist))

cntlist = []
for i in ulist:
    cntlist.append(slist.count(i))

if cntlist.count(max(cntlist)) > 1:
    print('?')

else:
    print(ulist[cntlist.index(max(cntlist))])
