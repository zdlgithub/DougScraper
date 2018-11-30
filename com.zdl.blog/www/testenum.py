from enum import Enum,unique


@unique
class Browser(Enum):
    CHROME = 1
    FIREFOX = 2

bn = Browser.CHROME

def abc():
    if bn == Browser.CHROME:
        print(bn)
    else:
        print(0)

abc()

class MyTest():
	def __init__(self):
		print('init')
		self.__one = 'one'
		self.__two = 'two'

	def __enter__(self):
		print('enter')
		return self

	def testone(self):
		print('testone')
		print(self.__one)
	def testtwo(self):
		print('testtwo')
		print(self.__two)

	def __del__(self):
		print('del')
		self.__one = None
		self.__two = None
	
	def __exit__(self, exc_type, exc_value, exc_tb):
		print('exit')
		self.__del__()

# with MyTest() as mt:
# 	print(mt.testone())
mta = MyTest()
mta.testone()
mta.testtwo()
mta = None

print('abc')
print('abc')
