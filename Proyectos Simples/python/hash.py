from tkinter.filedialog import *
import hashlib

class programa:

	#------------------------------------------

	def parte1(self):
		self.frame1=Frame(self.ventana)
		self.frame1.pack()
		self.listbox=Listbox(self.frame1)
		self.listbox.pack()
		self.listbox.insert(END,"md5")		#0
		self.listbox.insert(END,"sha1")		#1
		self.listbox.insert(END,"sha224")	#2
		self.listbox.insert(END,"sha256")	#3
		self.listbox.insert(END,"sha384")	#4
		self.listbox.insert(END,"sha512")	#5
		Button(self.frame1,text="Siguiente",command=self.parte2).pack()
		self.ventana.mainloop()

	def parte2(self):
		if (self.listbox.curselection()[0]==0):
			self.hash=hashlib.md5()

		elif (self.listbox.curselection()[0]==1):
			self.hash=hashlib.sha1()

		elif (self.listbox.curselection()[0]==2):
			self.hash=hashlib.sha224()

		elif (self.listbox.curselection()[0]==3):
			self.hash=hashlib.sha256()

		elif (self.listbox.curselection()[0]==4):
			self.hash=hashlib.sha384()

		elif (self.listbox.curselection()[0]==5):
			self.hash=hashlib.sha512()

		else:
			pass
		
		self.frame1.pack_forget()
		self.parte3()

	def parte3(self):
		self.frame2=Frame(self.ventana)
		self.frame2.pack()
		Button(self.frame2,text="Archivo",command=self.parte4_archivo).grid(row=0,column=0)
		Button(self.frame2,text="Mensaje",command=self.parte4_mensaje).grid(row=0,column=1)

	def parte4_archivo(self):
		self.frame2.pack_forget()
		Arch_to_HASH=askopenfilename()
		Arch_to_HASH=open(Arch_to_HASH,"rb")
		while True:
			data=Arch_to_HASH.read(2**20)
			if not data:
				break
			self.hash.update(data)
		self.final()


	def parte4_mensaje(self):
		self.frame2.pack_forget()
		self.frame3=Frame(self.ventana)
		self.frame3.pack()
		Entry(self.frame3,textvariable=self.Men_to_HASH).pack()
		Button(self.frame3,text="Siguiente",command=self.parte5).pack()

	def parte5(self):
		self.frame3.pack_forget()	
		self.obj=self.Men_to_HASH.get()
		self.obj=self.obj.encode()
		self.hash.update(self.obj)
		self.final()

	def final(self):
		frame4=Frame(self.ventana)
		frame4.pack()
		text=Text(frame4,wrap=WORD)
		text.pack()
		text.insert(0.0,self.hash.hexdigest())





#----------------------------------------------------------------------------------
	def __init__(self):
		self.ventana=Tk()
		self.Men_to_HASH=StringVar()
		self.parte1()






programa()