name = input ('Enter file:')
handle = open (name, 'r')
print (name)
for linea in handle.readlines():
    print (linea)
