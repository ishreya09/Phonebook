from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from types import NoneType
import datetime
import sys

#from tkinter.ttk import *

phonebook=[]



def object(t,g,min,bg):
    r=Tk()
    a,b=min
    r.title(t)
    r.geometry(g)
    r.iconbitmap("calltelephoneauricularincircularbutton_80086.ico")
    r.minsize(a,b)
    r.configure(bg=bg)
    return r

def createContact():
    r= object("Create Contact", "1100x600",(1100,600),"#7575a3")
    Title= Label(r,
    text="Create Contact", relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibri",30,"bold"),borderwidth=10
    ).pack(side=TOP,fill=X)

    name_var=StringVar(master=r)
    phone_var=StringVar(master=r)
    phone2_var=StringVar(master=r)
    phone3_var=StringVar(r)
    email_var=StringVar(r)
    dob_var=StringVar(r)
    group_var=StringVar(r)
    profession_var=StringVar(r)
    address_var=StringVar(r)

    def submit():
        c=0
        unique_id = str(datetime.datetime.now())
        name=name_var.get()
        phone=phone_var.get()
        
        
        if phone2_var!=NoneType:
            phone2=phone2_var.get()
            
            phone2_var.set("")
        else:
            phone2=""
        if phone3_var!=NoneType:
            phone3=phone3_var.get()
            
            phone3_var.set("")
        else:
            phone3=""
        email=email_var.get()
        dob=dob_var.get()
        group=group_var.get()
        address =address_var.get()
        profession= profession_var.get()
        #validating
        if phone!="":
            if not(phone.isdigit()):
                mb.showerror("Number can contain only digits","Number can contain only digits")
                r.destroy()
                c=1
        if email!="":
            if not('@' in email):
                mb.showerror("Invalid Email","Invalid Email")
                r.destroy()
                c=1
        
        if phone2 !="":
            if not(phone2.isdigit()):
                mb.showerror("Number can contain only digits","Number can contain only digits")
                r.destroy()
                c=1
        
        if phone3 !="":
            if not(phone3.isdigit()):
                mb.showerror("Number can contain only digits","Number can contain only digits")
                r.destroy()
                c=1

        if dob!="":
            if len(dob)!=10 and not("/" in dob):
                mb.showerror("Invalid Date of Birth Format","Invalid Date of Birth Format")
                r.destroy()
                c=1
        if profession!="":
            if not profession.isalpha():
                mb.showerror("Profession Can't contain digits or special characters","Profession Can't contain digits or special characters")
                r.destroy()
                c=1
        if c==0:
            phonebook.append([name,phone,phone2,phone3,email,dob,group,address,profession,unique_id])
            mb.showinfo("Contact Created", "The Contact is Successfully Created")
            r.destroy()

        name_var.set("")
        phone_var.set("")
        email_var.set("")
        dob_var.set("")
        group_var.set("")
        address_var.set("")
        profession_var.set("")
        
        print(phonebook)
        
        

        """r1=object("Contact Created","300x100",(300,100),"gray")
        r1.maxsize(300,100)
        Label(r1,text="Contact Created ",padx=10,pady=10,bg="white",relief=GROOVE).pack(side=TOP,anchor=CENTER,fill=X)
        Button(r1,
        text="OK",
        command=r1.destroy).pack(side=BOTTOM,anchor=S,fill=X,padx=10,pady=10)"""

        

    def add2ndnum():
        nonlocal phone2_var
        
        phone2_label=Label(r,
        text="Number 2:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)  
        phone2_entry=Entry(r,width=60,textvariable=phone2_var,).pack(side=TOP,anchor=N,padx=100)

        add=Button(r,
        text="ADD THIRD NUMBER",
        command=add3rdnum,
        font=("Times New Roman",15,"bold"),
        bg="#3d3d5c",
        fg="white",).pack(side=TOP,anchor=N,fill=X,padx=200)


    def add3rdnum():
        nonlocal phone3_var
        
        phone3_label=Label(r,
        text="Number 3:",
        font =("Times New Roman", 15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)  
        phone3_entry=Entry(r,width=60,textvariable=phone3_var,).pack(side=TOP,anchor=N,padx=100)
    
    

    

    
    sub=Button(r,
        text="Submit",
        command=submit,
        bg="#3d3d5c",
        font=("Times New Roman",15,"bold"),
        pady=8, 
        fg="white",
        relief=GROOVE,
        )

    sub.pack(side=TOP,anchor=N, fill=X,padx=200,pady=9)

    phone2_var.set("")
    phone3_var.set("")
        
    name_label=Label(r,
    text="Name:",
    font =("Times New Roman",15),
    bg="#1f1f2e",
    fg="white",
    ).pack(side=TOP,anchor=N,fill=X,padx=100)
    name_entry=Entry(r,width=100,textvariable=name_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    phone_label=Label(r,
    text="Number 1:",
    font =("Times New Roman",15),
    bg="#1f1f2e",
    fg="white",
    ).pack(side=TOP,anchor=N,fill=X,padx=100)  
    phone_entry=Entry(r,width=60,textvariable=phone_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    add=Button(r,
        text="ADD SECOND NUMBER",
        command=add2ndnum,
        font=("Times New Roman",15,"bold"),
        bg="#3d3d5c",
        fg="white",).pack(side=TOP,anchor=N,fill=X,padx=200)

    email_label=Label(r,text="Email:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    email_entry=Entry(r,width=100,textvariable=email_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    
    dob_label=Label(r,text="Date of birth(DD/MM/YYYY):",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    dob_entry=Entry(r,width=50,textvariable=dob_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    
    category_label=Label(r,text="Category(Family/Friends/Work/Favorite/Emergency/Important/Others):",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    category_entry=Entry(r,width=60,textvariable=group_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    
    address_label=Label(r,text="Address:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    address_entry=Entry(r,width=60,textvariable=address_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    profession_label=Label(r,text="Designation :",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    profession_entry=Entry(r,width=60,textvariable=profession_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    
    r.mainloop()

def editContact(i,t,t1):
    r= object("Edit Contact", "1100x600",(1100,600),"#7575a3")
    Title= Label(r,
    text="Edit Contact", relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibri",30,"bold"),borderwidth=10
    ).pack(side=TOP,fill=X)
    i[1]=str(i[1])
    i[2]=str(i[2])
    i[3]=str(i[3])
    name_var=StringVar(master=r)
    phone_var=StringVar(master=r)
    phone2_var=StringVar(master=r)
    phone3_var=StringVar(r)
    email_var=StringVar(r)
    dob_var=StringVar(r)
    group_var=StringVar(r)
    profession_var=StringVar(r)
    address_var=StringVar(r)

    def submit():
        c=0
        unique_id = i[9]
        name=name_var.get()
        phone=phone_var.get()
        
        if phone2_var!=NoneType:
            phone2=phone2_var.get()
            
            phone2_var.set("")
        else:
            phone2=""
        if phone3_var!=NoneType:
            phone3=phone3_var.get()
            
            phone3_var.set("")
        else:
            phone3=""
        email=email_var.get()
        dob=dob_var.get()
        group=group_var.get()
        address =address_var.get()
        profession= profession_var.get()
        d=phonebook.index(i)

        #validating
        if phone!="":
            if not(phone.isdigit()):
                mb.showerror("Number can contain only digits","Number can contain only digits")
                r.destroy()
                c=1
        if email!="":
            if not('@' in email):
                mb.showerror("Invalid Email","Invalid Email")
                r.destroy()
                c=1
        
        if phone2 !="":
            if not(phone2.isdigit()):
                mb.showerror("Number can contain only digits","Number can contain only digits")
                r.destroy()
                c=1
        
        if phone3 !="":
            if not(phone3.isdigit()):
                mb.showerror("Number can contain only digits","Number can contain only digits")
                r.destroy()
                c=1

        if dob!="":
            if len(dob)!=10 and not("/" in dob):
                mb.showerror("Invalid Date of Birth Format","Invalid Date of Birth Format")
                r.destroy()
                c=1
        if profession!="":
            if not profession.isalpha():
                mb.showerror("Profession Can't contain digits or special characters","Profession Can't contain digits or special characters")
                r.destroy()
                c=1

        if c==0:
            phonebook[d]=[name,phone,phone2,phone3,email,dob,group,address,profession,unique_id]

        
        
            print(phonebook)
        
            mb.showinfo("Contact Updated", "The Contact is Successfully Updated")
            r.destroy()
        t.destroy()
        t1.destroy()
    

    sub=Button(r,
        text="Update Contact",
        command=submit,
        bg="#3d3d5c",
        font=("Times New Roman",15,"bold"),
        pady=8, 
        fg="white",
        relief=GROOVE,).pack(side=TOP,anchor=N,padx=200,pady=9)
        
    name_var.set(i[0])
    phone_var.set(i[1])
    phone2_var.set(i[2])
    phone3_var.set(i[3])
    email_var.set(i[4])
    dob_var.set(i[5])
    group_var.set(i[6])
    address_var.set(i[7])
    profession_var.set(i[8])

    name_label=Label(r,
    text="Name:",
    font =("Times New Roman",15),
    bg="#1f1f2e",
    fg="white",
    ).pack(side=TOP,anchor=N,fill=X,padx=100)
    name_entry=Entry(r,width=100,textvariable=name_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    phone_label=Label(r,
    text="Number 1:",
    font =("Times New Roman",15),
    bg="#1f1f2e",
    fg="white",
    ).pack(side=TOP,anchor=N,fill=X,padx=100)  
    phone_entry=Entry(r,width=60,textvariable=phone_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    phone2_label=Label(r,
        text="Number 2:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)  
    phone2_entry=Entry(r,width=60,textvariable=phone2_var,).pack(side=TOP,anchor=N,padx=100)
    phone3_label=Label(r,
        text="Number 3:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)  
    phone3_entry=Entry(r,width=60,textvariable=phone3_var,).pack(side=TOP,anchor=N,padx=100)
    email_label=Label(r,text="Email:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    email_entry=Entry(r,width=100,textvariable=email_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    dob_label=Label(r,text="Date of birth(DD/MM/YYYY):",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    dob_entry=Entry(r,width=60,textvariable=dob_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    category_label=Label(r,text="Category(Family/Friends/Work/Favorite/Emergency/Important/Others):",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    category_entry=Entry(r,width=60,textvariable=group_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    address_label=Label(r,text="Address:",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    address_entry=Entry(r,width=100,textvariable=address_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)
    profession_label=Label(r,text="Designation :",
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,padx=100)
    profession_entry=Entry(r,width=60,textvariable=profession_var,font = ('Times New Roman',10,'normal')).pack(side=TOP,anchor=N,padx=100)

    r.mainloop()


def delete(r1,r,i):
        #i=phonebook.index(i)
        r2=object( "{} Contact Deleted".format(i[0]), "300x100",(300,100),"#7575a3")
        r2.maxsize(300,100)
        i[1]=str(i[1])
        i[2]=str(i[2])
        i[3]=str(i[3])
        
        phonebook.remove(i)

        Label(r2,text="Contact Deleted",padx=10,pady=10,bg="#1f1f2e",
        font=("Times New Roman",15),
        fg="white",relief=GROOVE).pack(side=TOP,anchor=CENTER,fill=X)

        r1.destroy()  
        r.destroy()

        Button(
            r2,
            text="OK",
            font=("Times New Roman",15,"bold"),
            bg="#1f1f2e",
            fg="white",
            command=r2.destroy
            ).pack(side=BOTTOM,anchor=S,fill=X,padx=10,pady=10)

                 
            
        r2.mainloop()

def open(i,r):
    r1=object( "{} Contact Info".format(i[0]), "500x500",(500,500),"#7575a3")
    Title= Label(r1,
    text="Contact Details", relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibri",30,"bold"),borderwidth=10
        ).pack(side=TOP,fill=X)

    Label(master=r1,
        text="Name :  "+ i[0],
        font =("Times New Roman",15),
        bg="#1f1f2e",
        fg="white",
        relief=SUNKEN,
        borderwidth=2,
        padx=10,
            pady=3).pack(fill=X,side=TOP)

    Label(r1,
            text="Number :  " +str(i[1]),
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)

    if str(i[2])!="":
        Label(r1,
                text="Number 2 :  " +str(i[2]),
                font =("Times New Roman",15),
                bg="#1f1f2e",
                fg="white",
                relief=SUNKEN,
                borderwidth=2,
                padx=10,
                pady=3,
                ).pack(fill=X,side=TOP)
            
    if str(i[3])!="":
        Label(r1,
                text="Number 3 :  " +str(i[3]),
                font =("Times New Roman",15),
                bg="#1f1f2e",
                fg="white",
                relief=SUNKEN,
                borderwidth=2,
                padx=10,
                pady=3,
                ).pack(fill=X,side=TOP)

    Label(r1,
            text="Email :  " +str(i[4]),
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)

    Label(r1,
            text="Date of Birth :  " +str(i[5]),
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)


    Label(r1,
            text="Group :  " +i[6],
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)

    Label(r1,
            text="Address :  " +str(i[7]),
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)

    Label(r1,
            text="Designation :  " +str(i[8]),
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)
            
    Label(r1,
            text="Timestamp :  " +str(i[9]),
            font =("Times New Roman",15),
            bg="#1f1f2e",
            fg="white",
            relief=SUNKEN,
            borderwidth=2,
            padx=10,
            pady=3,
            ).pack(fill=X,side=TOP)

    
    """
    edit_img=PhotoImage(r1,file="D:\phone.py\icons8-edit-40.png")
    p6 = edit_img.subsample(1,1)
    
    delete1_img=PhotoImage(r1,file="D:\phone.py\icons8-delete-300.png")
    p7 = delete1_img.subsample(6,6)
    """
    g_img=PhotoImage(master=r1,file="D:\phone.py\icons8-delete-300.png")
    i1 = g_img.subsample(6,6)
    
    g1_img=PhotoImage(master=r1,file="D:\phone.py\icons8-edit-80.png")
    i2 = g1_img.subsample(2,2)
    
    Button(r1,
            text="  Edit Contact",
            command=lambda:[editContact(i,r,r1)],
            font=("Times New Roman",15),
            fg="white",
            bg="#3d3d5c",
            pady=5,
            image=i2,
            compound=LEFT,
            ).pack(side=BOTTOM,fill=X)
    

    Button(r1,text= "  Delete Contact",
            #way to send parameters 
            #command=lambda:delete(r1),
            command=lambda:[delete(r1,r,i)],
            font=("Times New Roman",15),
            fg="white",
            bg="#3d3d5c",
            pady=5,
            #image=p7,
            #compound=LEFT,
            image=i1,
            compound=LEFT,
            ).pack(side=BOTTOM,fill=X)


    r1.mainloop()

def openList(l):
    r=object("Contacts","1100x600",(1100,600),"#7575a3")

    Title= Label(r,
    text="Contacts", relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibri",30,"bold"),borderwidth=10
    ).pack(side=TOP,fill=X)

    create_img=PhotoImage(master=r,file="D:\phone.py\icons8-add-96.png")
    p = create_img.subsample(2,2)

    create_contact=Button(r,
    text="  Create Contact",
    image=p,
    font=("Times New Roman",14,"bold"),
    command=createContact,
    compound=LEFT,
    bg="#3d3d5c",
    fg="white"
    ).pack(padx=200,fill=X,pady=2)

    search_var=StringVar(r)

    def submit():
        global phonebook
        q=search_var.get()
        print(q,type(q))
        l=[]
        c=0
        for i in phonebook:
            #phonebook.append([name,phone,phone2,phone3,email,dob,group,address,profession,unique_id])
            print(i)
            
            if i[0].startswith(q) or i[0].endswith(q) or i[1]==q or i[2]==q or i[3]==q or i[4]==q or i[6]==q or i[7].startswith(q) or i[7].endswith(q) or i[8]==q:
                    l.append(i)
                    c=1

            print("c=",c)
        if c==0:
            mb.showinfo("No Contact Found","No results found")
        elif c==1:
            r.destroy()
            openList(l)
            


    search_label=Label(r,text="Search :",
        font =("Times New Roman",15,"bold"),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,pady=4)
    search_entry=Entry(r,textvariable=search_var,font = ('Times New Roman',10,'normal'),width=100).pack(side=TOP,anchor=N)

    g1_img=PhotoImage(master=r,file="D:\phone.py\icons8-search-96.png")
    i2 = g1_img.subsample(3,3)

    Button(r,
        text="  Search",
        command=submit,
        bg="#3d3d5c",
        fg="white",
        font=("Times New Roman",15,"bold"),
        padx=10,
        pady=5,
        image=i2,
        compound=LEFT
        ).pack(side=TOP,anchor=N,padx=200,fill=X,pady=2)



    scroll_bar = Scrollbar(r)
  
    scroll_bar.pack( side = RIGHT,
                fill = Y )

    columns = ('name', 'phone_number_1',"phone_number_2","phone_number_3", 'email',"date_of_birth","group","address","profession","unique_id")
    tree = ttk.Treeview(r, columns=columns, show='headings',yscrollcommand = scroll_bar.set)
    tree.heading("name",text="Name")
    tree.heading("phone_number_1",text="Phone Number 1")
    tree.heading("phone_number_2",text="Phone Number 2")
    tree.heading("phone_number_3",text="Phone Number 3")
    tree.heading("email",text="Email")
    tree.heading("date_of_birth",text="Date of Birth")
    tree.heading("group",text="Group")
    tree.heading("address",text="Address")
    tree.heading("profession",text="Profession")
    tree.heading("unique_id",text="Time Stamp")

    tree.column('name', width=60, anchor=W)
    tree.column('phone_number_1', width=15,)
    tree.column('phone_number_2', width=15,)
    tree.column('phone_number_3', width=15, )
    tree.column('email', width=60, )
    tree.column('date_of_birth',width=8,)
    tree.column('group', width=20, )
    tree.column('address', width=50, )
    tree.column('profession', width=10,)
    tree.column('unique_id', width=10,)
    
    l.sort(key=lambda x:x[0])

    for i in l:
        tree.insert('', END, values=i)
    
    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']
            print(record)
            open(record,r)
    
    tree.bind('<Double-1>', item_selected)

    tree.pack(fill=BOTH,expand=True)
    
    #scrollbar = ttk.Scrollbar(r, orient=VERTICAL, command=tree.yview)
    #tree.configure(yscroll=scrollbar.set)
    #scrollbar.pack(side=LEFT,fill=Y)

    r.mainloop()

def dummyData():
    #phonebook.append([name,phone,phone2,phone3,email,dob,group,address,profession,unique_id])
    #Dummy data is to add entries quickly so that testing can be done quickly
    phonebook.append(["Police","100","","","gov@gmail.com","","emergency","Ranchi Jharkhand","police",str(datetime.datetime.now())])
    phonebook.append(["Hospital","112","","","hospital@gmail.com","","emergency","Ranchi Jharkhand","hospital",str(datetime.datetime.now())])
    phonebook.append(["Shreya Mishra","9193939999","9343387733","9876543210","shreya@gmail.com","22/02/2002","friend","Ranchi Jharkhand","student",str(datetime.datetime.now())])
    phonebook.append(["Apoorva Raj","9193933499","9343387732","9126543210","apoorva@gmail.com","25/12/2002","important","Mysore Karnataka","student",str(datetime.datetime.now())])
    phonebook.append(["Adrija Pes","9419393559","9343456733","9876733210","adrija@gmail.com","05/05/2004","favourite","Bangalore Karnataka","student",str(datetime.datetime.now())])
    phonebook.append(["Abhijeet Mishra","9193456999","9999387733","9873293210","abhijeet@gmail.com","09/11/1978","work","Hyderabad Telangana","teacher",str(datetime.datetime.now())])
    phonebook.append(["Isham Sinha","9567456999","9934587733","9878943210","isham@gmail.com","09/01/2007","friend","Bangalore Karnataka","student",str(datetime.datetime.now())])
    phonebook.append(["B. S. Grewal","9193456999","9999387733","9873293210","grewal@gmail.com","07/08/2002","classmate","Hyderabad Telangana","teacher",str(datetime.datetime.now())])
    phonebook.append(["Skanda Sreesha Prashad","9193402399","9991234733","9870912210","skanda@gmail.com","04/02/2005","friend","Bangalore Karnataka","student",str(datetime.datetime.now())])
    phonebook.append(["Chandan Kumar Jha","9155402399","9991111133","9222912210","chandan@gmail.com","04/12/1985","family","Bangalore Karnataka","student",str(datetime.datetime.now())])
    phonebook.append(["Rashmi Jha","9155433399","9333111133","9233312210","rashmi@gmail.com","02/07/1985","family","Bangalore Karnataka","student",str(datetime.datetime.now())])
    mb.showinfo("Data added", "Dummy Data Entries is added to the phone directory")

def searchContact():
    global phonebook
    
    r= object("Search Contact", "600x600",(600,600),"#7575a3")
    Title= Label(r,
    text="Search Contact", relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibri",30,"bold"),borderwidth=10
    ).pack(side=TOP,fill=X)

    search_var=StringVar(r)

    def submit():
        global phonebook
        q=search_var.get()
        print(q,type(q))
        l=[]
        c=0
        for i in phonebook:
            #print(i)
            
            if i[0].startswith(q) or i[0].endswith(q) or i[1]==q or i[2]==q or i[3]==q or i[4]==q or i[6]==q or i[7].startswith(q) or i[7].endswith(q) or i[8]==q:
                    l.append(i)
                    c=1

            print("c=",c)
        if c==0:
            mb.showinfo("No Contact Found","No results found")
        elif c==1:
            openList(l)


    search_label=Label(r,text="Search :",
        font =("Times New Roman",15,"bold"),
        bg="#1f1f2e",
        fg="white",
        ).pack(side=TOP,anchor=N,fill=X,pady=4)
    search_entry=Entry(r,textvariable=search_var,font = ('Times New Roman',10,'normal'),width=100).pack(side=TOP,anchor=N)

    g1_img=PhotoImage(master=r,file="D:\phone.py\icons8-search-96.png")
    i2 = g1_img.subsample(3,3)

    Button(r,
        text="Search",
        command=submit,
        bg="#3d3d5c",
        fg="white",
        font=("Times New Roman",15,"bold"),
        padx=10,
        pady=5,
        image=i2,
        compound=LEFT
        ).pack(side=TOP,anchor=N,padx=200,fill=X,pady=10)


    r.mainloop()
    


def allContacts():
    openList(phonebook)

    #phonebook.append([name,phone,phone2,phone3,email,dob,group,address,profession,id])

def manageGroups():
    r=object("Groups","600x600",(600,600),"#7575a3")
    Title= Label(r,
    text="Groups", relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibri",30,"bold"),borderwidth=10
    ).pack(side=TOP,fill=X)
    def exist():
        t=["work","friends","friend","family","emergency","favourite","important"]
        l=[]
        for i in phonebook:
            if i[6].lower() not in t:
                l.append(i[6])
        
        return l

    def work():
        l=[]
        for i in phonebook:
            if i[6]=="Work" or i[6]=="WORK" or i[6]=="work":
                l.append(i)
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")
    
    def friend():
        l=[]
        for i in phonebook:
            if i[6]=="Friends" or i[6]=="FRIENDS" or i[6]=="friends" or i[6]=="friend" or i[6]=="Friend" or i[6]=="FRIEND":
                l.append(i)
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")
    
    def family():
        l=[]
        for i in phonebook:
            if i[6]=="Family" or i[6]=="FAMILY" or i[6]=="family":
                l.append(i)
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")

    def favourite():
        l=[]
        for i in phonebook:
            if i[6]=="favourite" or i[6]=="Favourite" or i[6]=="favourite".upper():
                l.append(i)
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")

    def important():
        l=[]
        for i in phonebook:
            if i[6]=="important" or i[6]=="Important" or i[6]=="important".upper():
                l.append(i)
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")

    def emergency():
        l=[]
        for i in phonebook:
            if i[6]=="emergency" or i[6]=="Emergency" or i[6]=="EMERGENCY":
                l.append(i)
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")
    
    def others():
        l=[]
        a=exist()
        for i in phonebook:
            if i[6] in a:
                l.append(i)
        
        if l!=[]:
            openList(l)
        else:
            mb.showinfo("Empty Group","Noone present in the group")

    g_img=PhotoImage(master=r,file="D:\phone.py\icons8-emergency-64.png")
    i = g_img.subsample(2,2)

    g1_img=PhotoImage(master=r,file="D:\phone.py\icons8-work-64.png")
    i1 = g1_img.subsample(2,2)

    g2_img=PhotoImage(master=r,file="D:\phone.py\icons8-friends-96.png")
    i2 = g2_img.subsample(2,2)

    g3_img=PhotoImage(master=r,file="D:\phone.py\icons8-family-120.png")
    i3 = g3_img.subsample(3,3)

    g4_img=PhotoImage(master=r,file="D:\phone.py\icons8-group-96 (1).png")
    i4 = g4_img.subsample(2,2)
    
    g5_img=PhotoImage(master=r,file="D:\phone.py\icons8-favourite-64.png")
    i5 = g5_img.subsample(2,2)

    g6_img=PhotoImage(master=r,file="D:\phone.py\icons8-important-64.png")
    i6 = g6_img.subsample(2,2)



    Button(
        r,
        text="  Emergency Contacts",
        command=emergency,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i

        ).pack(fill=X,pady=5)

    Button(
        r,
        text="  Important Contacts",
        command=important,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i6

        ).pack(fill=X,pady=5)
    
    Button(
        r,
        text="  Favourite Contacts",
        command=favourite,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i5

        ).pack(fill=X,pady=5)

    Button(
        r,
        text="  Work",
        command=work,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i1

        ).pack(fill=X,pady=5)

    Button(
        r,
        text="  Friends",
        command=friend,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i2
        ).pack(fill=X,pady=5)
    Button(
        r,
        text="  Family",
        command=family,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i3
        ).pack(fill=X,pady=5)
    Button(
        r,
        text="  Others",
        command=others,
        bg="#3d3d5c",
        fg="white",
        font =("Times New Roman",15),
        compound=LEFT,
        image=i4
        ).pack(fill=X,pady=5)

    r.mainloop()

def deleteallContact():
    global phonebook
    phonebook=[]      
    print(phonebook)
    mb.showinfo("All contacts Deleted","All Contacts Deleted")

def exit_prg():
    sys.exit(0)


def setPhonebook(pb):
    global phonebook
    phonebook =pb

import function2
import main2

def light_mode():
    function2.setPhonebook(phonebook)
    main2.call()
