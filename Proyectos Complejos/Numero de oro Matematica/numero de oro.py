"""
Trabajo realizado por Josué Alejandro Bouchard
"""

import json
from decimal import *

nombreArchivoJson="datos.json"

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a


#Comeinza el codigo
try:
	archivo=json.load(open(nombreArchivoJson))

	getcontext().prec = archivo["presicion"]
	nums=set(archivo["serie de fibonacci"])
	num_actual=int(archivo["num_actual"])
except:
	open(nombreArchivoJson,"x").write(json.dumps({"presicion":getcontext().prec,"serie de fibonacci":[0,0],"num_actual":0,"numero de oro":"0"},indent=5))
	getcontext().prec = archivo["presicion"]
	nums=set(archivo["serie de fibonacci"])
	num_actual=int(archivo["num_actual"])

try:
	while(True):
		nums.add(fib(num_actual))
		final=sorted(list(nums))
		try:
			numeroOro=Decimal(final[-2])/Decimal(final[-1])
			open(nombreArchivoJson,"w").write(json.dumps({"presicion":getcontext().prec,"serie de fibonacci":[final[-2],final[-1]],"num_actual":num_actual,"numero de oro":str(numeroOro)},indent=5))
		except:
			pass
		num_actual=num_actual+1
except KeyboardInterrupt:
	print("Deteniendo programa...")