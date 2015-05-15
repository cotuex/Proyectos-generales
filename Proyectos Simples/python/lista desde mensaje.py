def lista_desde_mensaje(mensaje):
	lista=[]
	for i in mensaje:
		lista.append(str(i))
	return (lista)

print(lista_desde_mensaje("abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"))