from tkinter import*
from tkinter import ttk,messagebox
import os
import time
class File_App:
    def __init__(self,root):
        self.root=root
        self.root.title("File Base Record System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="File Base Record System",bd=10,relief=GROOVE,pady=10,font=("times new roman",35,"bold")).pack(fill=X)
        Student_Frame=Frame(self.root,bd=10,relief=GROOVE)
        Student_Frame.place(x=20,y=100,height=455) 

        stitle=Label(Student_Frame,text="Customera Details",font=("times new roman",30,"bold")).grid(row=0,columnspan=4,pady=20)

        self.s_id=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()

        lblsid=Label(Student_Frame,text="Customer Id",font=("times new roman",20,"bold")).grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txtsid=Entry(Student_Frame,bd=7,textvariable=self.s_id,relief=GROOVE,width=21,font="arial 15 bold").grid(row=1,column=1,padx=10,pady=10)

        lblcontact=Label(Student_Frame,text="Contact",font=("times new roman",20,"bold")).grid(row=1,column=2,pady=10,padx=20,sticky="w")
        txtcontact=Entry(Student_Frame,bd=7,textvariable=self.contact,relief=GROOVE,width=21,font="arial 15 bold").grid(row=1,column=3,padx=10,pady=10)

        lblname=Label(Student_Frame,text="Name",font=("times new roman",20,"bold")).grid(row=2,column=0,pady=10,padx=20,sticky="w")
        txtname=Entry(Student_Frame,bd=7,textvariable=self.name,relief=GROOVE,width=21,font="arial 15 bold").grid(row=2,column=1,padx=10,pady=10)

        lbldate=Label(Student_Frame,text="Date(dd/mm/yyyy)",font=("times new roman",20,"bold")).grid(row=2,column=2,pady=10,padx=20,sticky="w")
        txtdate=Entry(Student_Frame,bd=7,textvariable=self.date,relief=GROOVE,width=21,font="arial 15 bold").grid(row=2,column=3,padx=10,pady=10)

        lblcourse=Label(Student_Frame,text="Course",font=("times new roman",20,"bold")).grid(row=3,column=0,pady=10,padx=20,sticky="w")
        txtcourse=Entry(Student_Frame,bd=7,textvariable=self.course,relief=GROOVE,width=21,font="arial 15 bold").grid(row=3,column=1,padx=10,pady=10)

        lbladdress=Label(Student_Frame,text="Address",font=("times new roman",20,"bold")).grid(row=4,column=0,pady=10,padx=20,sticky="w")
        txtaddress=Entry(Student_Frame,bd=7,textvariable=self.address,relief=GROOVE,width=21,font="arial 15 bold").grid(row=4,column=1,padx=10,pady=10)

        lblcity=Label(Student_Frame,text="City",font=("times new roman",20,"bold")).grid(row=5,column=0,pady=10,padx=20,sticky="w")
        txtcity=Entry(Student_Frame,bd=7,textvariable=self.city,relief=GROOVE,width=21,font="arial 15 bold").grid(row=5,column=1,padx=10,pady=10)

        lbldegree=Label(Student_Frame,text="Select Degree",font=("times new roman",20,"bold")).grid(row=3,column=2,padx=10,sticky="w",pady=10)
        lblproof=Label(Student_Frame,text="Id Proof",font=("times new roman",20,"bold")).grid(row=4,column=2,padx=10,sticky="w",pady=10)
        lbldegree=Label(Student_Frame,text="Payment Mode",font=("times new roman",20,"bold")).grid(row=5,column=2,padx=10,sticky="w",pady=10)

        degreecombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.degree,state="readonly",font="arial 15 bold")
        degreecombo['values']=("BA","BCA","MA","MBA","B.TEch","M.Tech","BBA","MCA","M.com")
        degreecombo.grid(row=3,column=3,pady=10)

        idcombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.proof,state="readonly",font="arial 15 bold")
        idcombo['values']=("Adhaar","Pan Card","Voter Id","Driving License","PassPort","Residancle Proof","Local Id","Collage Id")
        idcombo.grid(row=4,column=3,pady=10)

        paymentcombo=ttk.Combobox(Student_Frame,width=20,textvariable=self.payment,state="readonly",font="arial 15 bold")
        paymentcombo['values']=("Visa","Master Card","UPI","Bank Transactition","RTGS","Online Payment","Cash","Check")
        paymentcombo.grid(row=5,column=3,pady=10)

        btnFrame=Frame(self.root,bd=10,relief=GROOVE)
        btnFrame.place(x=10,y=580)

        btnsave=Button(btnFrame,text="Save",font="arial 15 bold",bd=7,width=18,command=self.save_data).grid(row=0,column=0,padx=12,pady=10)
        btndelete=Button(btnFrame,text="Delete",font="arial 15 bold",bd=7,width=18,command=self.delete).grid(row=0,column=1,padx=12,pady=10)
        btnclear=Button(btnFrame,text="Clear",command=self.clear,font="arial 15 bold",bd=7,width=18).grid(row=0,column=2,padx=12,pady=10)
        btnlog=Button(btnFrame,text="Log Out",font="arial 15 bold",bd=7,width=18,command=self.logout).grid(row=0,column=3,padx=12,pady=10)
        btnexit=Button(btnFrame,text="Exit",font="arial 15 bold",bd=7,width=18,command=self.exit_fun).grid(row=0,column=4,padx=12,pady=10)


        File_Frame=Frame(self.root,bd=10,relief=GROOVE)
        File_Frame.place(x=1038,y=100,width=300,height=450)

        ftitle=Label(File_Frame,text="All Files",font="arial 20 bold",bd=5,relief=GROOVE).pack(side=TOP,fill=X)

        scroll_y=Scrollbar(File_Frame,orient=VERTICAL)
        self.file_list=Listbox(File_Frame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.pack(fill=BOTH,expand=1)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.show_files()
        self.root.mainloop()

    def save_data(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Customer ID must be Requrid")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"

                if present=="yes":
                    ask=messagebox.askyesno("Update","File Already Present /nDo you want to update it")
                    if ask>0:
                        self.save_file()
                        messagebox.showinfo("Update","Record Updated")
                        self.show_files()
                else:
                    self.save_file()
                    messagebox.showinfo("Update","Record Updated")  
                    self.show_files()
            else:
                self.save_file()
                messagebox.showinfo("Update","Record Updated")  
                self.show_files()
                    

       
    def save_file(self):

        f=open("files/"+str(self.s_id.get())+".txt","w")
        f.write(
                str(self.s_id.get())+","+
                str(self.name.get())+","+
                str(self.course.get())+","+
                str(self.address.get())+","+
                str(self.city.get())+","+
                str(self.contact.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())
                )
        f.close()
        

    def show_files(self):
        files=os.listdir("files/")
        self.file_list.delete(0,END)
        if len(files)>0:
            
            for i in files:
                self.file_list.insert(END,i)

    def get_data(self,ev):
        get_cursor=self.file_list.curselection()
        #print(self.file_list.get(get_cursor))
        f1=open("files/"+self.file_list.get(get_cursor))
        value=[]
        for f in f1:
            value=f.split(",")


        self.s_id.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])

    def clear(self):
        self.s_id.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")

    def delete(self):
        present="no"
        if self.s_id.get()=="":
            messagebox.showerror("Error","Customer ID must be Requrid")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    if i.split(".")[0] == self.s_id.get():
                        present="yes"
                if present=="yes":
                    ask=messagebox.askyesno("Delete","Do you want to Delete")
                    if ask>0:
                        os.remove("files/"+self.s_id.get()+".txt")
                        messagebox.showinfo("Succesfully","Deleted")
                        self.show_files()
                else:
                    messagebox.showerror("Error","File not Found")

    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Do you want to Exit")
        if ask>0:
            self.root.destroy()
    def logout(self):
        self.root.destroy()
        import login

root=Tk()
ob=File_App(root)
root=mainloop()









    