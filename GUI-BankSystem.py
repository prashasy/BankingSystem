import tkinter as tk
from tkinter import messagebox
from time import gmtime, strftime


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0

def write(master,name,oc,pin):
	
	if( (is_number(name)) or (is_number(oc)==0) or (is_number(pin)==0)):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

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
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+oc+"              "+oc+"\n")
	frec.close()
	
	messagebox.showinfo("Details","Your Account Number is:"+str(accnt_no))
	master.destroy()
	return

def crdt_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 

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
	frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ",gmtime()))+"     "+str(amti)+"              "+str(cb)+"\n")
	frec.close()
	messagebox.showinfo("Operation Successfull!!","Amount Credited Successfully!!")
	master.destroy()
	return

def debit_write(master,amt,accnt,name):

	if(is_number(amt)==0):
		messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
		master.destroy()
		return 
			
	fdet=open(accnt+".txt",'r')
	pin=fdet.readline()
	camt=int(fdet.readline())
	fdet.close()
	if(int(amt)>camt):
		messagebox.showinfo("Error!!","You dont have that amount left in your account\nPlease try again.")
	else:
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
	creditwn.configure(bg="orange")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(crditwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")
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
	creditwn.configure(bg="orange")
	fr1=tk.Frame(creditwn,bg="blue")
	l_title=tk.Message(crditwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")	
	l1=tk.Label(creditwn,relief="raised",text="Enter Amount to be debited: ")
	e1=tk.Entry(creditwn,relief="raised")
	l1.pack(side="top")
	e1.pack(side="top")
	b=tk.Button(creditwn,text="Debit",relief="raised",command=lambda:debit_write(creditwn,e1.get(),a,name))
	b.pack(side="top")




def disp_bal(a):
	fdet=open(a+".txt",'r')
	fdet.readline()
	bal=fdet.readline()
	fdet.close()
	messagebox.showinfo("Balance",bal)




def disp_tr_hist(a):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	disp_wn.title("Transaction History")
	disp_wn.configure(bg="orange")
	fr1=tk.Frame(disp_wn,bg="blue")
	fr1=tk.Frame(disp_wn)
	fr1.pack(side="top")
	l_title=tk.Message(disp_wn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")


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
	try:
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
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")

def check_bal(master,a,b,c):
	try:
		fpin=open(a+".txt",'r')
		st=fpin.readline()
		fpin.readline()
		fpin.readline()
		name=fpin.readline()
		fpin.close()
		if(st==(b+"\n") and (c.lower()+"\n")==name.lower()): 
			master.destroy()
			disp_bal(a)
			
		else:
			messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
			master.destroy()
			return 
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")

def check_debit(master,a,b,c):
	try:
		fpin=open(a+".txt",'r')
		st=fpin.readline()
		fpin.readline()
		fpin.readline()
		name=fpin.readline()
		fpin.close()
		if((st==(b+"\n")) and ((c.lower()+"\n")==name.lower())): 
			master.destroy()
			De_Amt(a,c)
			
		else:
			messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
			master.destroy()
			return
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")		 

def check_credit(master,a,b,c):
	try:
		fpin=open(a+".txt",'r')
		st=fpin.readline()
		fpin.readline()
		fpin.readline()
		name=fpin.readline()
		fpin.close()
		if(st==(b+"\n") and (c.lower()+"\n")==name.lower()):  
			master.destroy()
			Cr_Amt(a,c)
			
		else:
			messagebox.showinfo("Error","Invalid Credentials\nPlease try again.")
			master.destroy()
			return 
	except FileNotFoundError:
		messagebox.showinfo("Error","Invalid Credentials!\nTry Again!")
def Main_Menu():
	
	def Create():
		
		crwn=tk.Tk()
		crwn.geometry("600x300")
		crwn.title("Create Account")
		crwn.configure(bg="orange")
		fr1=tk.Frame(crwn,bg="blue")

		l_title=tk.Message(crwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier","50","bold"))
		l_title.pack(side="top")

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
		b=tk.Button(crwn,text="Submit",command=lambda: write(crwn,e1.get().strip(),e2.get().strip(),e3.get().strip()))
		b.pack(side="top")
		return
	def Credit():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Credit")
		crdtwn.configure(bg="orange")
		fr1=tk.Frame(crdtwn,bg="blue")
		l_title=tk.Message(crdtwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier","50","bold"))
		l_title.pack(side="top")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check_credit(crdtwn,e2.get().strip(),e3.get().strip(),e1.get().strip()))
		b.pack(side="top")
	def Debit():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Debit")
		crdtwn.configure(bg="orange")
		fr1=tk.Frame(crdtwn,bg="blue")
		l_title=tk.Message(crdtwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier","50","bold"))
		l_title.pack(side="top")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check_debit(crdtwn,e2.get().strip(),e3.get().strip(),e1.get().strip()))
		b.pack(side="top")
	def check_balance():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Balance Check")
		crdtwn.configure(bg="orange")
		fr1=tk.Frame(crdtwn,bg="blue")
		l_title=tk.Message(crdtwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier","50","bold"))
		l_title.pack(side="top")
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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: check_bal(crdtwn,e2.get().strip(),e3.get().strip(),e1.get().strip()))
		b.pack(side="top")


	def transac_hist():
		crdtwn=tk.Tk()
		crdtwn.geometry("600x300")
		crdtwn.title("Transaction History")
		crdtwn.configure(bg="orange")
		fr1=tk.Frame(crdtwn,bg="blue")
		l_title=tk.Message(crdtwn,text="JUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
		l_title.config(font=("Courier","50","bold"))
		l_title.pack(side="top")

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
		b=tk.Button(crdtwn,text="Submit:",relief="raised",command=lambda: tr_hist(crdtwn,e2.get().strip(),e3.get().strip(),e1.get().strip()))
		b.pack(side="top")	

	rootwn=tk.Tk()
	rootwn.geometry("1600x500")
	rootwn.title("Apna Bank")
	rootwn.configure(background='orange')
	fr1=tk.Frame(rootwn)
	fr1.pack(side="top")
	bg_image = tk.PhotoImage(file ="pile1.gif")
	x = tk.Label (image = bg_image)
	x.place(y=-400)

	l_title=tk.Message(text="WELCOME TO\nJUIT BANK",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
	l_title.config(font=("Courier","50","bold"))
	l_title.pack(side="top")


	img1=tk.PhotoImage(file="new.gif")
	myimg1=img1.subsample(2,2)
	img2=tk.PhotoImage(file="credit.gif")
	myimg2=img2.subsample(2,2)
	img3=tk.PhotoImage(file="debit.gif")
	myimg3=img3.subsample(2,2)
	img4=tk.PhotoImage(file="balance1.gif")
	myimg4=img4.subsample(2,2)
	img5=tk.PhotoImage(file="transaction.gif")
	myimg5=img5.subsample(2,2)

	b1=tk.Button(image=myimg1,command=Create)
	b1.image=myimg1
	b2=tk.Button(image=myimg2,command=Credit)
	b2.image=myimg2
	b3=tk.Button(image=myimg3,command=Debit)
	b3.image=myimg3
	b4=tk.Button(image=myimg4,command=check_balance)
	b4.image=myimg4
	b5=tk.Button(image=myimg5,command=transac_hist)
	b5.image=myimg5
	
	img6=tk.PhotoImage(file="quit.gif")
	myimg6=img6.subsample(2,2)

	b6=tk.Button(image=myimg6,relief="raised",command=rootwn.destroy)

	b1.place(x=10,y=200)
	b2.place(x=10,y=270)
	b3.place(x=900,y=200)
	b4.place(x=900,y=270)
	b5.place(x=900,y=340)
	b6.place(x=500,y=400)

	rootwn.mainloop()



Main_Menu()