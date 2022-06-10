from tkinter import *
from function2 import *
from tkinter import messagebox as mb

#"#CBF7F3" = heading labels
#"#9ccefa" = buttons
#"#CED9F7" = bg
#"#c3e8e2"=form
#"#b8cde0"= Ask Skanda(I know where I have used and explaining it is way too hard)

def main1():
    root= Tk()

    root.title("Phone Book")
    root.geometry("1200x700")
    root.minsize(1200,700)
    root.iconbitmap("calltelephoneauricularincircularbutton_80086.ico")
    root.configure(bg="#CED9F7")

    c_l=Label(text="Copyright 2022",bg="#b8cde0",
        fg="black",
        font=("Times New Roman", 10)
        ).pack(side=BOTTOM,fill=X,anchor=NW)

    Title_label= Label(
        text="Phonebook", relief=GROOVE,bg="#CBF7F3",fg="black",font=("Times New Roman", 30," bold"),borderwidth=10
    ).pack(side=TOP,fill=X)


    welcome_label= Label(
        text="""Hello user, \n
    Welcome to the Smartphone Phonebook""", relief=SUNKEN,borderwidth=2,bg="#CED9F7",fg="black",font=("Times New Roman", 10),pady=1,
    ).pack(anchor=N,side=TOP,fill=X)

    create_img=PhotoImage(file="D:\phone.py\icons8-add-96.png")
    p = create_img.subsample(2,2)

    create_contact=Button(root,
        text="   Create Contact",
        image=p,
        font=("Times New Roman",14,"bold"),
        command=createContact,
        compound=LEFT,
        bg="#9ccefa",
        fg="black"
        ).pack(fill=X,pady=5)

    all_img=PhotoImage(file="D:\phone.py\icons8-contacts-80.png")
    p1 = all_img.subsample(2,2)

    all_contacts=Button(
        root,
        text="        All Contacts",
        font=("Times New Roman",14,"bold"),
        command=allContacts,
        bg="#9ccefa",
        fg="black",
        image=p1,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    search_img=PhotoImage(file="D:\phone.py\icons8-search-128.png")
    p2 = search_img.subsample(3,3)

    search_contact=Button(
        root,
        text="   Search Contact",
        font=("Times New Roman",14,"bold"),
        command=searchContact,
        bg="#9ccefa",
        fg="black",
        image=p2,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    group_img=PhotoImage(file="D:\phone.py\icons8-group-96.png")
    p3 = group_img.subsample(2,2)

    see_groups=Button(
        root,
        text="                 Groups",
        font=("Times New Roman",14,"bold"),
        command=manageGroups,
        bg="#9ccefa",
        fg="black",
        image=p3,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    dummy_img=PhotoImage(file="D:\phone.py\icons8-data-sheet-80.png")
    p4 = dummy_img.subsample(2,2)

    data_dummy=Button(
        root,
        text="  Add Sample Data  ",
        font=("Times New Roman",14,"bold"),
        command=dummyData,
        bg="#9ccefa",
        fg="black",
        image=p4,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    #
    delete_img=PhotoImage(file="D:\phone.py\icons8-delete-300.png")
    p5 = delete_img.subsample(6,6)

    delete_contact=Button(
        root,
        text="       Delete All Contacts",
        command=deleteallContact,
        font=("Times New Roman",14,"bold"),
        bg="#9ccefa",
        fg="black",
        image=p5,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    #icons8-exit-256.png

    exit_img=PhotoImage(file="D:\phone.py\icons8-exit-256.png")
    p6 = exit_img.subsample(6,6)

    exit_prg=Button(
        root,
        text="             Exit",
        font=("Times New Roman",14,"bold"),
        command=exit,
        bg="#9ccefa",
        fg="black",
        image=p6,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    mode_prg=Button(
        root,
        text="  Convert to Dark Mode",
        font=("Times New Roman",14,"bold"),
        command=lambda:[root.destroy(),dark_mode()],
        bg="#9ccefa",
        fg="black",
        ).pack(fill=X,pady=5)

    root.mainloop()



if (__name__== "__main__"):
    main1()
else:
    def call():
        main1()
