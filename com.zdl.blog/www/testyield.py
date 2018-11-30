def jumping_rang(upto):	
	index=0
	while index<upto:
		jump = yield index
		print(jump)
		if jump==None :
			jump=1
		index+=jump
if __name__ == '__main__':
	iteror = jumping_rang(10)
	print(next(iteror))
	print(iteror.send(2))
	# print(iteror.send(-1))
	print(next(iteror))
	print(iteror.send(None))

def fib(n):
	index = 0
	a = 0
	b = 1
	while index < n:
		yield b
		a, b = b, a + b
		index += 1

print('-'*10 + 'test yield fib' + '-'*10)
for fib_res in fib(20):
	print(fib_res)



def copy_fib(n):
	print('I am copy from fib')
	yield from fib(n)
	print('Copy end')
print('-'*10 + 'test yield from' + '-'*10)
for fib_res in copy_fib(20):
	print(fib_res)