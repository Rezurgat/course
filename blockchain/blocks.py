import hashlib
import json

def block():
    name_first_from=input()
    name_first_to=input()
    prs_first=int(input())
    hashes=[]
    
    account={
             'from':name_first_from,
             'to':name_first_to,
             'prize':prs_first
    }
    data=json.dumps(account)
    binary_data=data.encode()
    sec=hashlib.sha224(binary_data).hexdigest()
    hashes.append(sec)
    
    with open('info.txt','a') as f:
        f.write(str(account)+'\n')
    
    
    qu=input('Do you want to make another transaction?:')
    while qu=='y':
        name_another_from=input()
        name_another_to=input()
        prs_another=int(input())
        account_={
             'from':name_another_from,
             'to':name_another_to,
             'prize':prs_another
    }
        data_=json.dumps(account_)
        binary_data_=data_.encode()
        sec_=hashlib.sha224(binary_data_).hexdigest()
        account_['prehash']=hashes[-1]
        hashes.append(sec_)
        
        with open('info.txt','a') as f1:
            f1.write(str(account_)+'\n')
        qu=input('Do you want to make another transaction?:')     
    else:
        with open('info.txt','r') as f2:
            for line in f2:
                print(line)
    with open('info.txt','a') as f3:
        f3.write('hashes: '+ str(hashes[:-1]) + '\n')
    
    print(str(hashes))
block()
            

    