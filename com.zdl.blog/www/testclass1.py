class Payment:
	def pay(self,amount):
		raise:NotImplementedError
		# pass

class Alipay(Payment):
	def zhifu(self,amount):
		print('apply alipay %d' % amount)

alipay = Alipay()
alipay.zhifu(100)
alipay.pay(200)