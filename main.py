from tkinter import *
from function import *
from tkinter import messagebox as mb


#"#7575a3" = light gray for labels
#"#3d3d5c" =  dark gray for buttons
#"#9494b8" = bg
#"#1f1f2e"=form

def main():
    root= Tk()

    root.title("Phone Book")
    root.geometry("1200x700")
    root.minsize(1200,700)
    root.iconbitmap("calltelephoneauricularincircularbutton_80086.ico")
    root.configure(bg="#9494b8")

    c_l=Label(text="copyright 2022",bg="#3d3d5c",
        fg="white",
        font=("Calibre", 10)
        ).pack(side=BOTTOM,fill=X,anchor=NW)

    Title_label= Label(
        text="PHONEBOOK",relief=GROOVE,bg="#3d3d5c",fg="white",font=("Calibre", 30," bold"),borderwidth=10
    ).pack(side=TOP,fill=X)


    welcome_label= Label(
        text="""Hello user, \n
    Welcome to the smartphone phonebook""", relief=SUNKEN,borderwidth=2,bg="#9494b8",fg="black",font=("Calibre", 10),pady=1,
    ).pack(anchor=N,side=TOP,fill=X)

    create_img=PhotoImage(file="D:\\phone.py\icons8-add-96.png")
    p = create_img.subsample(2,2)

    create_contact=Button(root,
        text="  Create Contact",
        image=p,
        font=("Times New Roman",14,"bold"),
        command=createContact,
        compound=LEFT,
        bg="#3d3d5c",
        fg="white"
        ).pack(fill=X,pady=5)

    all_img=PhotoImage(file="D:\\phone.py\icons8-contacts-80.png")
    p1 = all_img.subsample(2,2)

    all_contacts=Button(
        root,
        text="  All Contacts",
        font=("Times New Roman",14,"bold"),
        command=allContacts,
        bg="#3d3d5c",
        fg="white",
        image=p1,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    search_img=PhotoImage(file="D:\\phone.py\icons8-search-128.png")
    p2 = search_img.subsample(3,3)

    search_contact=Button(
        root,
        text="  Search Contact",
        font=("Times New Roman",14,"bold"),
        command=searchContact,
        bg="#3d3d5c",
        fg="white",
        image=p2,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    group_img=PhotoImage(file="D:\\phone.py\icons8-group-96.png")
    p3 = group_img.subsample(2,2)

    see_groups=Button(
        root,
        text="  Groups",
        font=("Times New Roman",14,"bold"),
        command=manageGroups,
        bg="#3d3d5c",
        fg="white",
        image=p3,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    dummy_img=PhotoImage(file="D:\\phone.py\icons8-data-sheet-80.png")
    p4 = dummy_img.subsample(2,2)

    data_dummy=Button(
        root,
        text="  Add Sample Data  ",
        font=("Times New Roman",14,"bold"),
        command=dummyData,
        bg="#3d3d5c",
        fg="white",
        image=p4,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    #
    delete_img=PhotoImage(file="D:\\phone.py\icons8-delete-300.png")
    p5 = delete_img.subsample(6,6)

    delete_contact=Button(
        root,
        text="  Delete All Contacts",
        command=deleteallContact,
        font=("Times New Roman",14,"bold"),
        bg="#3d3d5c",
        fg="white",
        image=p5,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    #icons8-exit-256.png

    exit_img=PhotoImage(file="D:\\phone.py\icons8-exit-256.png")
    p6 = exit_img.subsample(6,6)

    exit_prg=Button(
        root,
        text="  Exit",
        font=("Times New Roman",14,"bold"),
        command=exit,
        bg="#3d3d5c",
        fg="white",
        image=p6,
        compound=LEFT,
        ).pack(fill=X,pady=5)

    mode_prg=Button(
        root,
        text="  Convert to Light Mode",
        font=("Times New Roman",14,"bold"),
        command=lambda:[root.destroy(),light_mode()],
        bg="#3d3d5c",
        fg="white",
        ).pack(pady=5,fill=X)

    root.mainloop()

if (__name__== "__main__"):
    main()
else:
    def call():
        main();


