#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 可写函数说明
def printinfo( arg1, *vartuple ):
	"打印任何传入的参数"
	print("输出arg1:")
	print(arg1)
	print("输出vartuple: ")
	for var in vartuple:
		print(var)
	return;
# 调用printinfo 函数
printinfo( 10 );
printinfo( 70, 60, 50 );