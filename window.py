import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime


def write(master,a,b,c):
	
	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()
	
	fpin=open(str(accnt_no)+"-pin.txt",'w')
	fpin.write(c)
	fpin.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(b+"\n")
	fdet.write(a+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                   \tCredit\t Debit\tBalance\n")
	frec.write(str(strftime("%y-%m-%d %h:%m:%s",gmtime()))+"\t"+b+"\t    \t"+b+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def check(master,a,b):
	fpin=open(a+"-pin.txt",'r')
	st=fpin.readline()
	fpin.close()
	if(st==b): 
		messagebox.showinfo("Abcd","1")
		master.destroy()
	else:return 



def Main_Menu():
	
	def Create():
		
		crwn=tk.Tk()
		crwn.geometry("600x300")
		l1=tk.Label(crwn,text="Enter Name:",relief="raised")
		l1.pack(side="top")
		e1=tk.Entry(crwn)
		e1.pack(side="top")
		l2=tk.Label(crwn,text="Enter opening credit:",relief="raised")
		l2.pack(side="top")
		e2=tk.Entry(crwn)
		e2.pack(side="top")
		l3=tk.Label(crwn,text="Enter desired PIN:",relief="raised")
		l3.pack(side="top")
		e3=tk.Entry(crwn,show="*")
		e3.pack(side="top")
		b=tk.Button(crwn,text="Submit",command=lambda: write(crwn,e1.get(),e2.get(),e3.get()))
		b.pack(side="top")
		return
	def Credit():

		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		l1=tk.Label(crdtwn,text="Enter Name: ",relief="raised")
		l2=tk.Label(crdtwn,text="Enter Account Number: ",relief="raised")
		l3=tk.Label(crdtwn,text="Enter PIN: ",relief="raised")
		e1=tk.Entry(crdtwn)
		e2=tk.Entry(crdtwn)
		e3=tk.Entry(crdtwn,show="*")
		l1.pack(side="top")
		e1.pack(side="top")
		l2.pack(side="top")
		e2.pack(side="top")
		l3.pack(side="top")
		e3.pack(side="top")
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check(crdtwn,e2.get(),e3.get()))
		b.pack(side="right")



	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	l_title=tk.Message(text="Welcome to Apna Bank!!\nWe are pleased to serve you!!\nPlease choose from among the following:",relief="raised",width=2000,padx=500,pady=20,fg="red",bg="blue",justify="center",anchor="center")
	l_title.pack(side="top")
	b1=tk.Button(text="1] Create a new account.",command=Create)
	b2=tk.Button(text="Credit amount in your account",command=Credit)
	b3=tk.Button(text="Debit amount from your account")
	b4=tk.Button(text="Check Balance in your account")
	b5=tk.Button(text="View Transaction History")
	b1.pack(side="left")
	b2.pack(side="left")
	b3.pack(side="left")
	b4.pack(side="left")
	b5.pack(side="left")
	rootwn.mainloop()



Main_Menu()