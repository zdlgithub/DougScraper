from functools import reduce

def add(aa,bb):
	cc = []	
	for a in aa:
		
		for b in bb:
			ctemp = []
			tmp0 = a[0]+','+b[0]
			tmp1 = ''
			if len(a)>1 and len(b)>1 :
				tmp1 = a[1]+','+b[1]
			elif len(a)>1:
				tmp1 = a[1]
			elif len(b)>1:
				tmp1=b[1]
			ctemp.append(tmp0)
			ctemp.append(tmp1)

			cc.append(ctemp)
			
	return cc


my_array = [[['Official Standard'], ['Glass n TPU Case'], ['Glass n Nillkin Case'], ['Glass n NillkinCover'], ['Glass n Mi Earphones']], [['Black', '7', 'https://ae01.alicdn.com/kf/HTB1NcilXOnrK1RjSsziq6xptpXa7/Global-version-Xiaomi-Redmi-Note-6-Pro-4GB-64GB-Snapdragon-636-Octa-Core-4000mAh-6-26.jpg'], ['Blue', '8', 'https://ae01.alicdn.com/kf/HTB13e5nXOzxK1RjSspjq6AS.pXaI/Global-version-Xiaomi-Redmi-Note-6-Pro-4GB-64GB-Snapdragon-636-Octa-Core-4000mAh-6-26.jpg'], ['Rose gold', '9', 'https://ae01.alicdn.com/kf/HTB1kcSjXUjrK1RkHFNRq6ySvpXam/Global-version-Xiaomi-Redmi-Note-6-Pro-4GB-64GB-Snapdragon-636-Octa-Core-4000mAh-6-26.jpg']]]

rr = reduce(add,my_array)
print(rr)