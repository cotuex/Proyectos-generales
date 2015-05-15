from tkinter import *
import subprocess

def ventana_inicio():
	
	def hibernar():
		subprocess.call(["shutdown","-h"])
		ventana.destroy()
	
	def apagar():
		ventana.destroy()
		ventana_apagado()

	def cancelar_apagado():
		subprocess.call(["shutdown","-a"])
		ventana.destroy()

	ventana=Tk()
	ventana.title("Apagar o hibernar PC")
	boton_a=Button(ventana,text="Apagar",command=apagar)
	boton_c=Button(ventana,text="Cancelar Apagado",command=cancelar_apagado)
	boton_h=Button(ventana,text="Hibernar",command=hibernar)

	boton_a.grid(row=0, column=0)
	boton_c.grid(row=0, column=1)
	boton_h.grid(row=1, column=0)
	ventana.mainloop()

def ventana_apagado():
	def procesar():
		if t_h.get()!="":
			h=t_h.get()
		else:
			h="0"
		
		if t_m.get()!="":
			m=t_m.get()
		else:
			m="0"

		if t_s.get()!="":
			s=t_s.get()
		else:
			s="0"
		tiempo=eval(s+"+"+m+"*60"+"+"+h+"*3600")
		apagar(tiempo)

	def apagar(tiempo):
		subprocess.call(["shutdown","-s","-t",str(tiempo)])
		ventana.destroy()


	ventana=Tk()
	ventana.title("Apagar PC")
	t_h=StringVar()
	t_m=StringVar()
	t_s=StringVar()
	label=Label(ventana,text="Especifique el tiempo")
	horas=Label(ventana,text="Horas")
	minutos=Label(ventana,text="Minutos")
	segundos=Label(ventana,text="Segundos")
	tth=Entry(ventana,textvariable=t_h)
	ttm=Entry(ventana,textvariable=t_m)
	tts=Entry(ventana,textvariable=t_s)
	boton=Button(ventana,text="Apagar",command=procesar)

	label.grid(column=0, row=0)
	horas.grid(column=0,row=1)
	minutos.grid(column=1,row=1)
	segundos.grid(column=2,row=1)
	tth.grid(row=2, column=0)
	ttm.grid(row=2, column=1)
	tts.grid(row=2, column=2)
	boton.grid(row=3, column=1)

ventana_inicio()