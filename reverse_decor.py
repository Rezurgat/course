def reverse_decor(func):
	def wrapper(s):
		pre_res=func(s)
		res=sorted(pre_res,reverse=True)
		res_fin=''.join(res)
		print(f'Ответ - {res_fin}')
	return wrapper
	
@reverse_decor
def getting(s):
	return(s)
	
getting(input().split())