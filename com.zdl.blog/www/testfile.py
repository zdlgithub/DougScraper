
with open('1.csv','a+') as fsp:
	fsp.write('test file;')
	fsp.write('test file1;')
	fsp.write('test file1;')
	fsp.write('test file1;')
	fsp.writelines('file4\nfile5')
	
with open('1.csv','r') as fr:
	print(fr.read())