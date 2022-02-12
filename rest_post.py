from urllib import request, parse
import json

body={'hello':'world'}#тело запроса

jsondata=json.dumps(body)
byte_json=jsondata.encode('utf-8')

req= request.Request('https://ya.ru', data=byte_json,method='POST')# если передаем через байты,то POST необязателенюВ основном,method прописывается,если нужно сделать PUT или DELETE
req.add_header('Content-Type', 'application/json; charset=utf-8')#заголовок

resp=request.urlopen(req)# и теперь с объектом resp мы можем работать (узнать status и тд.,как с GET)