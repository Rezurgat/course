import pickle

phonebookfile='phonebook.data'

phonebook= [ { "name":'Bob',
               "phone":'5415645'
             },
             { "name":'Tom',
               "phone": '74561544' 
             },
             { "name" : 'Oli',
               "phone":'45554513' 
             }
            ]

for contact in phonebook:
    print ('Номер контакта {0}:{1}'. format(contact['name'],contact['phone']))
    
some=input('>')

if some=='del':
    name_del= input ('Введите номер,который нужно удалить>')
    for contact  in phonebook:
        if name_del== contact['name']:
            phonebook.remove(contact)
            
for contact in phonebook:
    print ('Номер контакта {0}:{1}'. format(contact['name'],contact['phone']))
    
if some=='add':
    new_name=input('Введите новое имя>')
    new_phone=input('Введите номер>')
    new_contact={
                    "name":new_name,
                    "phone":new_phone
                }
    phonebook.append(new_contact)
    
for contact in phonebook:
    print ('Номер контакта {0}:{1}'. format(contact['name'],contact['phone']))
    
if some == 'edit':
    edit_contact=input('Введите контакт,который нужно изменить>')
    for index,contact in enumerate(phonebook):
        edit_name=input('Введите новое имя>')
        edit_phone=input('Введите новый номер>')
        contact_update={"name":edit_name,
                        "phone":edit_phone}
        phonebook[index]=contact_update
        index=1
        break
        if index==1:
            print('Контакт успешно добавлен')
            
for contact in phonebook:
    print ('Номер контакта {0}:{1}'. format(contact['name'],contact['phone']))
    
f=open(phonebookfile,'wb')
pickle.dump(phonebook,f)
f.close()

del phonebook

f=open(phonebook,'rb')
store=pickle.load(f)
print(store)