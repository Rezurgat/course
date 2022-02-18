n=input().replace('+','').replace('-','').replace('-','').replace('(','').replace(')','')
counter=0
if n[0]=='7':
    counter+=1

for i in range(len(n)):
    if 0<=int(n[i])<=9:
        counter+=1
if counter==12:
    print('ДА')
else:
    print('НЕТ')