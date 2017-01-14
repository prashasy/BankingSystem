import sys
from time import gmtime, strftime
class Bank:
	f1=open("Accnt_Record.txt",'r+')
	a=int(f1.readline())+1
	f1.close()

#def __init__(self):

	def BankSystem(self):
		print("Enter your choice\n")
		print("1] Create an account in our bank\n")
		print("2] Credit amount in your acount\n")
		print("3] Debit amount from your account\n")
		print("4] Check Balance\n")
		print("5] Transaction Summary")
		choice=int(input("Enter your choice:"))
        
		if (choice==1):
				name=input("Enter name:")
				amt=input("\nEnter opening balance:") 
				self.create(name,amt) 
		elif (choice==2 or choice==3 or choice==4 or choice==5):
			name=input("Enter name: ")
			accnt_no=input("\nEnter Account Number:")
        	
			f=open(str(accnt_no)+"-pin.txt",'r')
			p=int(f.readline())
			f.close()
			for i in range(0,3):
				pin=input("Enter pin:")
				if( not (pin == p)): 
	        			print ("PIN incorret.Try Again")
				if(i==2): return
				else: break

				if(choice==2 or choice==3):
					amt=input("\nEnter amount:")
				if(choice==2):self.credit(accnt_no,name,amt)
				if(choice==3):self.debit(accnt_no,name,amt)
			if(choice==4):self.check_bal(accnt_no)
				
			if(choice==5):self.transact_history(accnt_no)
			print("Thankyou for Banking with us!!")
			return
	def check_bal(self,accnt_no):
		f=open(str(accnt_no)+".txt",'r')
		cb=int(f.readline())
		print("\nCurrent Balance=(INR)",cb)
		f.close()
		return
def update(self,cb,name,accnt_no):
	f=open(str(accnt_no)+".txt","w")
	f.write(str(cb)+"\n")
	f.write(str(name)+"\n")
	f.write(str(accnt_no)+"\n")
	f.close()
	return
def debit(self,accnt_no,name,amt):
	f=open(str(accnt_no)+".txt",'r+')
	cb=int(f.readline())
	if(cb<amt):
		strin="Sorry!!\nyou dont have enough balance left in your account to perform this transaction\nCurrent Balance="+str(cb)
		raise ValueError(strin)
	cb=cb-amt
	f.close()
	ff=open(str(accnt_no)+"-rec.txt",'a+')
	ff.write(str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+"\t    \t"+str(amt)+"\t"+str(cb)+"\n")
	ff.close()
	self.update(cb,name,accnt_no)
	return
def credit(self,accnt_no,name,amt):
	f=open(str(accnt_no)+".txt","r+")
	cb=int(f.readline())
	cb=cb+amt
	ff=open(str(accnt_no)+"-rec.txt",'a+')
	ff.write(str(strftime("%y-%m-%d %h:%m:%s",gmtime()))+"\t"+str(amt)+"\t    \t"+str(cb)+"\n")
	ff.close()
	self.update(cb,name,accnt_no)
	return
def transact_history(self,accnt_no):
	f=open(str(accnt_no)+"-rec.txt",'r')
	for line in f:
		print (line)
	f.close()
	return 
def create(self,name,amt=0):
     accnt_no=(Bank.a)
     pin=0
     for i in range(0,2):
     	print ("Enter an ATM pin (of 4 dgits)")
     	pin=int(input())
     	if((pin/1000)>=1 and (pin/100000)==0):
     		break
     	if(i==1):
     		print ("You have exhausted your two attempts.Try again later!!")
     		return
     	print("Enter pin of exaclty 4 digits!!")

     fpin=open(str(accnt_no)+"-pin.txt",'w')
     fpin.write(str(pin))
     fpin.close()

     f1=open("Accnt_Record.txt",'w')
     f1.write(str(Bank.a))
     f1.close()
     Bank.a+=1
     f=open(str(accnt_no)+".txt","w")
     f.write(str(amt)+"\n")
     f.write(str(name)+"\n")
     f.write(str(accnt_no)+"\n")
     f.close()
     ff=open(str(accnt_no)+"-rec.txt",'w')
     ff.write("Date                   \tCredit\t Debit\tBalance\n")
     ff.write(str(strftime("%y-%m-%d %h:%m:%s",gmtime()))+"\t"+str(amt)+"\t    \t"+str(amt)+"\n")
     ff.close()
     print ("""Congratulations!!
     Account created successfully!!
     Your Account No. is - """,accnt_no)
     return
print ("Welcome to Apna bank!!")
while True:
	ch=int(input("Enter 1 to continue 0 to quit: "))
	if ch==0:
		sys.exit(0)
	b=Bank()
	Bank.BankSystem(b)
	
    





    

