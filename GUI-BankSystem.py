import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime
#from PIL import ImageTk,Image


def write(master,name,oc,pin):
	
	f1=open("Accnt_Record.txt",'r')
	accnt_no=int(f1.readline())
	accnt_no+=1
	f1.close()

	f1=open("Accnt_Record.txt",'w')
	f1.write(str(accnt_no))
	f1.close()

	fdet=open(str(accnt_no)+".txt","w")
	fdet.write(pin+"\n")
	fdet.write(oc+"\n")
	fdet.write(str(accnt_no)+"\n")
	fdet.write(name+"\n")
	fdet.close()

	frec=open(str(accnt_no)+"-rec.txt",'w')
	frec.write("Date                             Credit      Debit     Balance\n")
	frec.write(str(strftime("%Y-%m-%d %H:%M:%S",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=amti+camt
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("%Y-%m-%d %H:%M:%S",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	amti=int(amt)
	cb=camt-amti
	fdet=open(accnt+".txt",'w')
	fdet.write(pin)
	fdet.write(str(cb)+"\n")
	fdet.write(accnt+"\n")
	fdet.write(name+"\n")
	fdet.close()
	frec=open(str(accnt)+"-rec.txt",'a+')
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+"              "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Debited Successfully!!")
	master.destroy()
	return

def Cr_Amt(a,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300")
	creditwn.title("Credit Amount")
	l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be credited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Credit",relief="raised",command=lambda:crdt_write(creditwn,e1.get(),a,name))
	b.pack(side="top")


def De_Amt(a,name):
	creditwn=tk.Tk()
	creditwn.geometry("600x300")
	creditwn.title("Debit Amount")
	l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be debited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Debit",relief="raised",command=lambda:debit_write(creditwn,e1.get(),a,name))
	b.pack(side="top")


def check_debit(master,a,b,c):
	fpin=open(a+".txt",'r')
	st=fpin.readline()
	fpin.readline()
	fpin.readline()
	name=fpin.readline()
	fpin.close()
	if((st==(b+"\n")) and ((c+"\n")==name)): 
		master.destroy()
		De_Amt(a,c)
		
	else:
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

def disp_bal(a):
	fdet=open(a+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)


def check_bal(master,a,b,c):
	fpin=open(a+".txt",'r')
	st=fpin.readline()
	fpin.readline()
	fpin.readline()
	name=fpin.readline()
	fpin.close()
	if(st==(b+"\n") and (c+"\n")==name): 
		master.destroy()
		disp_bal(a)
		
	else:
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

def disp_tr_hist(a):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
	l1.pack(side="top")
	fr2=tk.Frame(disp_wn)
	fr2.pack(side="top")
	frec=open(a+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()

def tr_hist(master,a,b,c):
	fpin=open(a+".txt",'r')
	st=fpin.readline()
	fpin.readline()
	fpin.readline()
	name=fpin.readline()
	fpin.close()
	if(st==(b+"\n") and (c+"\n")==name):  
		master.destroy()
		disp_tr_hist(a)
		
	else:
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

def check_credit(master,a,b,c):
	fpin=open(a+".txt",'r')
	st=fpin.readline()
	fpin.readline()
	fpin.readline()
	name=fpin.readline()
	fpin.close()
	if(st==(b+"\n") and (c+"\n")==name):  
		master.destroy()
		Cr_Amt(a,c)
		
	else:
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

def Main_Menu():
	
	def Create():
		
		crwn=tk.Tk()
		crwn.geometry("600x300")
		crwn.title("Create Account")
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
		crdtwn.title("Credit")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check_credit(crdtwn,e2.get(),e3.get(),e1.get()))
		b.pack(side="right")
	def Debit():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Debit")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check_debit(crdtwn,e2.get(),e3.get(),e1.get()))
		b.pack(side="right")
	def check_balance():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Balance Check")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check_bal(crdtwn,e2.get(),e3.get(),e1.get()))
		b.pack(side="right")


	def transac_hist():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Transaction History")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: tr_hist(crdtwn,e2.get(),e3.get(),e1.get()))
		b.pack(side="right")	

	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Apna Bank")
	rootwn.configure(background='orange')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	#bimage=tk.PhotoImage('~/Documents/BankingSystem/12345.jpg')
	#label1=tk.Label(image=bimage)
	#label1.place(x=0,y=0,relwidth=1,relheight=1)
	l_title=tk.Message(text="Welcome to Apna Bank!!\nWe are pleased to serve you!!\nPlease choose from among the following:",relief="raised",width=2000,padx=520,pady=20,fg="red",bg="blue",justify="center",anchor="center")
	l_title.pack(side="top")
	b1=tk.Button(text="1] Create a new account.",command=Create)
	b2=tk.Button(text="Credit amount in your account",command=Credit)
	b3=tk.Button(text="Debit amount from your account",command=Debit)
	b4=tk.Button(text="Check Balance in your account",command=check_balance)
	b5=tk.Button(text="View Transaction History",command=transac_hist)
	b1.pack(side="left")
	b2.pack(side="left")
	b3.pack(side="left")
	b4.pack(side="left")
	b5.pack(side="left")

	rootwn.mainloop()



Main_Menu()