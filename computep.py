# creamos la funcion
def computepay(h,r):
	if h <= 40:
		total = h * r
	else:
		total = 40 * r + (h-40) * 1.5 * r
	return("{0:.2f}".format(total))
#-------------------------------------------------------------

# aqui introducimos los parametros

while True:
	try:
		h = float(input("Horas trabajadas: "))
		if h < 1:
			print("Error. Tienes que poner como minimo una hora")
			continue
		elif h >=1:
			break
	except:
		print('Error.Tienes que introducir el numero de horas trabajadas')
		continue
while True:
	try:
		r = float(input("Sueldo a la hora: "))
		if r < 0:
			print("Error. El sueldo no puede ser negativo")
			continue
		else:
			break
	except:
		print("Error. Tienes que introducir el sueldo en numeros")
		continue
#-------------------------------------------------------------

# invocamos nuestra funcion
p = computepay(h,r)
print(p,"€")
