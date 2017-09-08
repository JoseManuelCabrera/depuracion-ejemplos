#la retribucion de las horas extra, sobre 40 horas, se incrementan en 1.5 veces
hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
	h = float(hrs)
	r = float(rate)
except:
	print("Error, introduce solo numeros.")
if h <= 40:
	print(r * h)
else:
	print(r * 40 + r * 1.5 * (h - 40))
