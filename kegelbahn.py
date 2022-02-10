n,k=[int(i) for i in input('>').split()]
bahn=['I']*n
for i in range(n):
    l,r=[int(s) for s in input('>>').split()]
    for j in range(l,r+1):
        bahn[j]='.'
        print(''.join(bahn))
    