import tkinter as tk

def disp_tr_hist(a):
	disp_wn=tk.Tk()
	disp_wn.geometry("900x600")
	#fr1=tk.Frame(disp_wn)
	#fr1.pack(side="top")
	l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
	l1.pack(side="top")
	#fr2=tk.Frame(disp_wn)
	#fr2.pack(side="top")
	frec=open(a+"-rec.txt",'r')
	for line in frec:
		l=tk.Message(disp_wn,text=line,relief="raised",width=2000)
		l.pack(side="top")
	b=tk.Button(disp_wn,text="Close Window",relief="raised",command=disp_wn.destroy)
	b.pack(side="top")
	frec.close()
	disp_wn.mainloop()


disp_tr_hist("63710015015")