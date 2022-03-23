import tkinter as tk
from tkinter import messagebox
import time
client_BYN=1000.00
client_USD=round(client_BYN/2.58,2)
money_BYN={'100':400,
       '50':400,
       '20':400,
       '10':400,
       '5':400,
      }
money_USD={'100':400,
           '50':400,
           '20':400,
           '10':400,
           '5':400,
           '2':400,
           '1':400,
          }

def pin():
    global pin_code
    win_pin=tk.Tk()
    win_pin.title('Пин-код')
    win_pin.geometry('1000x600+400+150')
    
    pin_code=tk.Entry(win_pin,show='*')
    pin_code.place(relx=.5,rely=.5)
    
    label_pin=tk.Label(win_pin,text='Введите пин-код',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
    label_pin.place(relx=.37,rely=.5)
    
    button_pin=tk.Button(win_pin,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=menu)
    button_pin.place(relx=.63,rely=.5)
    
    button_pin_del=tk.Button(win_pin,text='Корректировать',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=del_entry_pin,)
    button_pin_del.place(relx=.7,rely=.5)
    
    win_pin.mainloop
    
def ost():
    win_ost=tk.Tk()
    win_ost.title('Остаток на счете')
    win_ost.geometry('1000x600+400+150')

    label_ost=tk.Label(win_ost,text='Остаток на счете',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_ost.pack()
    
    counter_ost=tk.Label(win_ost,text=f'{client_BYN} BYN ({client_USD} USD)',font=('Monotype Coursiva',50,'bold'),)
    counter_ost.place(relx=.18,rely=.2)

def del_entry_phonecash():
     phone_cash_entry.delete(len(phone_cash_entry.get())-1)   

def phone_cash():
    global phone_cash_entry
    win_phone_cash=tk.Tk()
    win_phone_cash.title('Сумма')
    win_phone_cash.geometry('1000x600+400+150')

    label_phone_cash=tk.Label(win_phone_cash,text='Введите сумму',bg='green',fg='white',font=('Monotype Coursiva',30,'bold'),)
    label_phone_cash.place(relx=.35,rely=.3)
    
    phone_cash_entry=tk.Entry(win_phone_cash,width=9,font=('Monotype Coursiva',20,'bold'))
    phone_cash_entry.place(relx=.43,rely=.42)
    
    label_phone_cash_minmax=tk.Label(win_phone_cash,text='Минимальная сумма = 1 BYN  Максимальная сумма = 100 BYN',font=('Monotype Coursiva',15,'bold'),)
    label_phone_cash_minmax.place(relx=.2,rely=.9)
    
    button_enter_cash=tk.Button(win_phone_cash,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',13,'bold'),command=phone_cash_plus)
    button_enter_cash.place(relx=.63,rely=.42)
    
    button_enter_del=tk.Button(win_phone_cash,text='Корректировать',bg='green',fg='white',font=('Monotype Coursiva',13,'bold'),command=del_entry_phonecash,)
    button_enter_del.place(relx=.75,rely=.42)    

def del_entry_phone():
    phone_number.delete(len(phone_number.get())-1)
        
def phone():
    global phone_number
    win_phone=tk.Tk()
    win_phone.title('Мобильная связь')
    win_phone.geometry('1000x600+400+150')

    label_phone=tk.Label(win_phone,text='Мобильная связь',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_phone.pack()
    
    label_phone_entry=tk.Label(win_phone,text='Введите девять цифр номера',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_phone_entry.place(relx=.32,rely=.4)
    
    label_country=tk.Label(win_phone,text='+375',font=('Monotype Coursiva',20,'bold'),)
    label_country.place(relx=.35,rely=.5)
    
    phone_number=tk.Entry(win_phone,width=9,font=('Monotype Coursiva',20,'bold'))
    phone_number.place(relx=.43,rely=.5)
    
    button_enter=tk.Button(win_phone,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',13,'bold'),command=phone_cash)
    button_enter.place(relx=.63,rely=.5)
    
    button_pin=tk.Button(win_phone,text='Корректировать',bg='green',fg='white',font=('Monotype Coursiva',13,'bold'),command=del_entry_phone,)
    button_pin.place(relx=.75,rely=.5)

def del_byn():
    cash_byn.delete(len(cash_byn.get())-1)

def output_byn():
    global cash_byn
    global client_BYN
    d=int(cash_byn.get())
    d_f=d
    c_100=0
    c_50=0
    c_20=0
    c_10=0
    c_5=0
    while d!=0:
        if d//100>0:
            d1=d-100
            c_100+=1
            d=d1
        elif d//50>0:
            d1=d-50
            c_50+=1
            d=d1
        elif d//20>0:
            d1=d-20
            c_20+=1
            d=d1
        elif d//10>0:
            d1=d-10
            c_10+=1
            d=d1
        elif d//5>0:
            d1=d-5
            c_5+=1
            d=d1
        
    counter={'100':c_100,
            '50':c_50,
            '20':c_20,
            '10':c_10,
            '5':c_5,
            }
    end={}
    for key,value in counter.items():
        if value>0:
            end[key]=value
    
    if client_BYN-d_f>0:
        client_BYN-=d_f
        messagebox.showinfo(title='Успешно', message=f'Выведено {end}')
    elif client_BYN-d_f<0:
        messagebox.showerror(title='Ошибка', message='Недостаточно средств')
        
    for key,value in money_BYN.items():
        for key1,value1 in end.items():
            if key==key1:
                money_BYN[key]-=end[key1]
    

def phone_cash_plus():
    global client_BYN
    a=float(str(phone_cash_entry.get()))
    if a<1 or a>100:
        messagebox.showerror(title='Ошибка', message='Неверная сумма')
    elif 1<a<100:    
        client_BYN-=a
        messagebox.showinfo(title='Успешно', message='Одобрено банком')
    
def byn():
    global cash_byn
    moneys=list()
    for i in money_BYN.keys():
        if money_BYN[i]==0:
            pass
        elif money_BYN[i]>0:
            moneys.append(i)
    
    num='          '.join(str(e) for e in moneys)
            
    win_cash_byn_out=tk.Tk()
    win_cash_byn_out.title('Выдача наличных')
    win_cash_byn_out.geometry('1000x600+400+150')
    
    label_win=tk.Label(win_cash_byn_out,text='Выдача наличных',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_win.pack()
      
    label_cash_info=tk.Label(win_cash_byn_out,text='Доступные номиналы',font=('Monotype Coursiva',20,'bold'),)
    label_cash_info.place(relx=.35,rely=.15)
    
    label_cash_inside=tk.Label(win_cash_byn_out,text=f'{num}',font=('Monotype Coursiva',20,'bold'),)
    label_cash_inside.place(relx=.25,rely=.25)
    
    label_cash_info=tk.Label(win_cash_byn_out,text='Введите сумму',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_cash_info.place(relx=.385,rely=.38)
    
    cash_byn=tk.Entry(win_cash_byn_out,font=('Monotype Coursiva',20,'bold'))
    cash_byn.place(relx=.34,rely=.48)
    
    button_enter=tk.Button(win_cash_byn_out,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',14,'bold'),command=output_byn,)
    button_enter.place(relx=.68,rely=.48)
    
    button_delete=tk.Button(win_cash_byn_out,text='Корректировать',bg='green',fg='white',font=('Monotype Coursiva',14,'bold'),command=del_byn,)
    button_delete.place(relx=.78,rely=.48)

def output_usd():
    global cash_byn
    global client_USD
    global client_BYN
    d=int(cash_byn.get())
    d_f=d
    c_100=0
    c_50=0
    c_20=0
    c_10=0
    c_5=0
    c_2=0
    c_1=0
    while d!=0:
        if d//100>0:
            d1=d-100
            c_100+=1
            d=d1
        elif d//50>0:
            d1=d-50
            c_50+=1
            d=d1
        elif d//20>0:
            d1=d-20
            c_20+=1
            d=d1
        elif d//10>0:
            d1=d-10
            c_10+=1
            d=d1
        elif d//5>0:
            d1=d-5
            c_5+=1
            d=d1
        elif d//2>0:
            d1=d-2
            c_2+=1
            d=d1
        elif d//1>0:
            d1=d-1
            c_1+=1
            d=d1
        
    counter={'100':c_100,
            '50':c_50,
            '20':c_20,
            '10':c_10,
            '5':c_5,
            '2':c_2,
            '1':c_1
            }
    end={}
    for key,value in counter.items():
        if value>0:
            end[key]=value
    
    if client_USD-d_f>0:
        client_USD-=d_f
        client_BYN-=(d_f * 2.58)
        messagebox.showinfo(title='Успешно', message=f'Выведено {end}')
    elif client_USD-d_f<0:
        messagebox.showerror(title='Ошибка', message='Недостаточно средств')
        
    for key,value in money_USD.items():
        for key1,value1 in end.items():
            if key==key1:
                money_USD[key]-=end[key1]
    
    
def usd():
    global cash_byn
    moneys=list()
    for i in money_USD.keys():
        if money_USD[i]==0:
            pass
        elif money_USD[i]>0:
            moneys.append(i)
    
    num='          '.join(str(e) for e in moneys)
            
    win_cash_byn_out=tk.Tk()
    win_cash_byn_out.title('Выдача наличных')
    win_cash_byn_out.geometry('1000x600+400+150')
    
    label_win=tk.Label(win_cash_byn_out,text='Выдача наличных',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_win.pack()
      
    label_cash_info=tk.Label(win_cash_byn_out,text='Доступные номиналы',font=('Monotype Coursiva',20,'bold'),)
    label_cash_info.place(relx=.35,rely=.15)
    
    label_cash_inside=tk.Label(win_cash_byn_out,text=f'{num}',font=('Monotype Coursiva',20,'bold'),)
    label_cash_inside.place(relx=.25,rely=.25)
    
    label_cash_info=tk.Label(win_cash_byn_out,text='Введите сумму',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_cash_info.place(relx=.385,rely=.38)
    
    cash_byn=tk.Entry(win_cash_byn_out,font=('Monotype Coursiva',20,'bold'))
    cash_byn.place(relx=.34,rely=.48)
    
    button_enter=tk.Button(win_cash_byn_out,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',14,'bold'),command=output_usd,)
    button_enter.place(relx=.68,rely=.48)
    
    button_delete=tk.Button(win_cash_byn_out,text='Корректировать',bg='green',fg='white',font=('Monotype Coursiva',14,'bold'),command=del_byn,)
    button_delete.place(relx=.78,rely=.48)
    
def byn_usd():
    win_preout=tk.Tk()
    win_preout.title('Выбор операции')
    win_preout.geometry('1000x600+400+150')

    label_preout=tk.Label(win_preout,text='Выберите валюту',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
    label_preout.pack()
         
    button_preout_byn=tk.Button(win_preout,text='BYN',bg='green',fg='white',width=15,font=('Monotype Coursiva',20,'bold'),command=byn)
    button_preout_byn.place(relx=.37,rely=.4)
         
    button_preout_usd=tk.Button(win_preout,text='USD',bg='green',fg='white',width=15,font=('Monotype Coursiva',20,'bold'),command=usd)
    button_preout_usd.place(relx=.37,rely=.5)
    
    
def menu():
    if pin_code.get()=='6464':
         win_menu=tk.Tk()
         win_menu.title('Выбор операции')
         win_menu.geometry('1000x600+400+150')

         label_menu=tk.Label(win_menu,text='Выберите операцию',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
         label_menu.pack()
         
         button_ost=tk.Button(win_menu,text='Остаток на счете',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),command=ost)
         button_ost.place(relx=.01,rely=.5)
         
         button_take=tk.Button(win_menu,text='Выдача наличных',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),command=byn_usd)
         button_take.place(relx=.37,rely=.5)
         
         button_phone=tk.Button(win_menu,text='Мобильная связь',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),command=phone)
         button_phone.place(relx=.73,rely=.5)
         
    elif pin_code.get()!='6464':
        messagebox.showerror(title='Ошибка', message='Неверный пин-код')    
        
def coworker():
    global money_USD
    global money_BYN
    if access_service.get()=='tms':
         win_cow=tk.Tk()
         win_cow.title('Инкассация')
         win_cow.geometry('1000x600+400+150')

         label_cow=tk.Label(win_cow,text='Инкассация',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
         label_cow.pack() 
         label_cow_100=tk.Label(win_cow,text='Купюра номиналом в 100',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_100.place(relx=.15,rely=.16)
         counter_100=tk.Label(win_cow,text=money_BYN['100'],font=('Monotype Coursiva',10,'bold'),)
         counter_100.place(relx=.34,rely=.16)
         label_cow_50=tk.Label(win_cow,text='Купюра номиналом в 50',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_50.place(relx=.15,rely=.26)
         counter_50=tk.Label(win_cow,text=money_BYN['50'],font=('Monotype Coursiva',10,'bold'),)
         counter_50.place(relx=.34,rely=.26)
         label_cow_20=tk.Label(win_cow,text='Купюра номиналом в 20',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_20.place(relx=.15,rely=.36)
         counter_20=tk.Label(win_cow,text=money_BYN['20'],font=('Monotype Coursiva',10,'bold'),)
         counter_20.place(relx=.34,rely=.36)
         label_cow_10=tk.Label(win_cow,text='Купюра номиналом в 10',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_10.place(relx=.15,rely=.46)
         counter_10=tk.Label(win_cow,text=money_BYN['10'],font=('Monotype Coursiva',10,'bold'),)
         counter_10.place(relx=.34,rely=.46)
         label_cow_5=tk.Label(win_cow,text='Купюра номиналом в 5',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_5.place(relx=.15,rely=.56)
         counter_5=tk.Label(win_cow,text=money_BYN['5'],font=('Monotype Coursiva',10,'bold'),)
         counter_5.place(relx=.34,rely=.56)
         
         label_cow_100_usd=tk.Label(win_cow,text='Купюра номиналом в 100',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_100_usd.place(relx=.515,rely=.16)
         counter_100_usd=tk.Label(win_cow,text=money_USD['100'],font=('Monotype Coursiva',10,'bold'),)
         counter_100_usd.place(relx=.7,rely=.16)
         label_cow_50_usd=tk.Label(win_cow,text='Купюра номиналом в 50',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_50_usd.place(relx=.515,rely=.26)
         counter_50_usd=tk.Label(win_cow,text=money_USD['50'],font=('Monotype Coursiva',10,'bold'),)
         counter_50_usd.place(relx=.7,rely=.26)
         label_cow_20_usd=tk.Label(win_cow,text='Купюра номиналом в 20',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_20_usd.place(relx=.515,rely=.36)
         counter_20_usd=tk.Label(win_cow,text=money_USD['20'],font=('Monotype Coursiva',10,'bold'),)
         counter_20_usd.place(relx=.7,rely=.36)
         label_cow_10_usd=tk.Label(win_cow,text='Купюра номиналом в 10',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_10_usd.place(relx=.515,rely=.46)
         counter_10_usd=tk.Label(win_cow,text=money_USD['10'],font=('Monotype Coursiva',10,'bold'),)
         counter_10_usd.place(relx=.7,rely=.46)
         label_cow_5_usd=tk.Label(win_cow,text='Купюра номиналом в 5',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_5_usd.place(relx=.515,rely=.56)
         counter_5_usd=tk.Label(win_cow,text=money_USD['5'],font=('Monotype Coursiva',10,'bold'),)
         counter_5_usd.place(relx=.7,rely=.56)
         label_cow_2_usd=tk.Label(win_cow,text='Купюра номиналом в 2',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_2_usd.place(relx=.515,rely=.66)
         counter_2_usd=tk.Label(win_cow,text=money_USD['2'],font=('Monotype Coursiva',10,'bold'),)
         counter_2_usd.place(relx=.7,rely=.66)
         label_cow_1_usd=tk.Label(win_cow,text='Купюра номиналом в 1',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
         label_cow_1_usd.place(relx=.515,rely=.76)
         counter_1_usd=tk.Label(win_cow,text=money_USD['1'],font=('Monotype Coursiva',10,'bold'),)
         counter_1_usd.place(relx=.7,rely=.76)
         
         button_out_byn=tk.Button(win_cow,text='Вывести купюры',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=out,)
         button_out_byn.place(relx=.16,rely=.66)
         
         button_input_byn=tk.Button(win_cow,text='Пополнить купюроприемник',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=inp,)
         button_input_byn.place(relx=.16,rely=.76)
         
         button_out_usd=tk.Button(win_cow,text='Вывести купюры',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=out_usd,)
         button_out_usd.place(relx=.53,rely=.83)
         
         button_input_usd=tk.Button(win_cow,text='Пополнить купюроприемник',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=inp_usd,)
         button_input_usd.place(relx=.53,rely=.92) 
              
         win_cow.mainloop()
    elif access_service.get()!='tms':
        messagebox.showerror(title='Ошибка', message='Неверный пароль')
        
def out():
    for i in money_BYN.keys():
        money_BYN[i]=0
    return coworker()

def inp():
    for i in money_BYN.keys():
        money_BYN[i]=400
    return coworker()

def out_usd():
    for i in money_USD.keys():
        money_USD[i]=0
    return coworker()

def inp_usd():
    for i in money_USD.keys():
        money_USD[i]=400
    return coworker()

    
def service():
    global access_service
    win_ink=tk.Tk()
    win_ink.title('Сервисное окно')
    win_ink.geometry('1000x600+400+150')
    
    access_service=tk.Entry(win_ink,show='*')
    access_service.place(relx=.5,rely=.5)
    
    label_ink=tk.Label(win_ink,text='Введите пароль',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),)
    label_ink.place(relx=.37,rely=.5)
    
    button_ink=tk.Button(win_ink,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=coworker,)
    button_ink.place(relx=.63,rely=.5)
    
    button_delete=tk.Button(win_ink,text='Корректировать',bg='green',fg='white',font=('Monotype Coursiva',10,'bold'),command=del_entry_service,)
    button_delete.place(relx=.7,rely=.5)
    
    win_ink.mainloop()
    
def del_entry_service():
    access_service.delete(len(access_service.get())-1)

def del_entry_pin():
    pin_code.delete(len(pin_code.get())-1)

win_intro=tk.Tk()
win_intro.title('Виртуальный банкомат')
win_intro.geometry('1000x600+400+150')

label_hello=tk.Label(win_intro,text='TMS-банк приветствует Вас!',font=('Monotype Coursiva',40,'bold'))

button_enter=tk.Button(win_intro,text='ВВОД',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),command=pin)
button_enter.place(relx=.61,rely=.5)

label_enter=tk.Label(win_intro,text='Вставьте карту и нажмите',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),)
label_enter.place(relx=.25,rely=.5)

button_service=tk.Button(win_intro,text='Сервисный вход',bg='green',fg='white',font=('Monotype Coursiva',20,'bold'),command=service)
button_service.place(relx=.35,rely=.9)

label_hello.pack()
win_intro.mainloop()

    





