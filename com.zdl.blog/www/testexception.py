import traceback

print('########################################################')
print("1/0 Exception Info")
print( '---------------------------------------------------------')
try:
    1/0
except Exception as e:
    print( 'str(Exception):\t', str(Exception))
    print( 'str(e):\t\t', str(e))
    print( 'repr(e):\t', repr(e))
    # print( 'e.message:\t', e.with_traceback)
    print( 'traceback.print_exc():',traceback.print_exc())
    print( 'traceback.format_exc():\n%s' % traceback.format_exc())
print( '########################################################')
# print( '\n########################################################')  
# print( "i = int('a') Exception Info")
# print( '---------------------------------------------------------')
# try:
#     i = int('a')
# except Exception as e:
#     print( 'str(Exception):\t', str(Exception))
#     print( 'str(e):\t\t', str(e))
#     print( 'repr(e):\t', repr(e))
#     print( 'e.message:\t', e.message)
#     print( 'traceback.print_exc():',traceback.print_exc())
#     print( 'traceback.format_exc():\n%s' % traceback.format_exc())
# print( '########################################################')