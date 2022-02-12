import urllib.request

raw=urllib.request.urlopen('https://google.com') #GET

response_code=raw.status# при выводе даст код http(200,300 и тд)
raw_data=raw.read()#чтение построчно

print(f'status={response_code}')
print('-'*20)
print(raw_data)