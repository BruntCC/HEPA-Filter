f = open("demofile.conf", "r")



print(f.read())

if f.isnumeric():
   print('Integer')
else:
   print('Not an integer')



f.close()