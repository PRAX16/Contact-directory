from os import name
from tkinter import *
from PIL import Image, ImageTk
import csv 
from time import strftime
import datetime
import webbrowser
from tkinter import messagebox

 
# creating the root window 
root = Tk()
 
# root config
root.geometry("417x350")
root.title("Contacts Directory")

dict_list = []
name_tb = 0 
phone_number_tb = 0
address_tb = 0
spinbox_date = 0  
spinbox_month = 0
spinbox_year = 0 
temp = 0
temp2=0 
spinbox_cl = 0
e_tb  = 0
ig_tb = 0
fb_tb = 0
select = 0
name_label_display = ""
attachments = []



def showall_window2():
    global select
    showall = Toplevel()
    showall.title('Display All contacts')

    showall.geometry("300x300")
    showall['bg'] = "grey"

    #frame 1 for 3rd window
    frame1_3 = Frame(showall)
    frame1_3['bg'] = "grey"
    frame1_3.pack()

    #Sort by label
    sort_label = Label(frame1_3, text="Sort by")
    sort_label.grid(row=0,column=0, padx = 5)
    
    #Sort dropdown
    list_of_sorting = ["Last added"]
    temp3 = StringVar()

    #Dropdown / Option menu - sort by
    sortby_optionmenu = OptionMenu(frame1_3, temp3, *list_of_sorting)
    temp3.set("Select")
    sortby_optionmenu.grid(row=0,column=1)

    #frame 2
    frame2_3 = Frame(showall, bg="red",)
    frame2_3.pack()
    
    #Listbox configuration
    scroll = Scrollbar(frame2_3, orient=VERTICAL)
    select = Listbox(frame2_3, yscrollcommand=scroll.set, height=12)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    

    #frame 3 for the buttons
    frame3_3 = Frame(showall, bg = "grey")
    frame3_3.pack()

    Button(frame3_3,text="DELETE", command = delete, font= "Calibri", bd=5).grid(row = 1, column = 0,padx= 10, pady=10)
    Button(frame3_3,text="VIEW", command = view, font= "Calibri",bd = 5).grid(row = 1, column = 1,padx= 10, pady=10)

def save():
    name = name_tb.get()
    phone = phone_number_tb.get()
    address = address_tb.get("1.0",END)
    dob_date = spinbox_date.get()
    dob_month = spinbox_month.get()
    dob_year = spinbox_year.get()
    dob = datetime.date(int(dob_year), int(dob_month), int(dob_date))
    gmail = e_tb.get()
    insta = ig_tb.get()
    facebook = fb_tb.get()

    if name == "" or phone == "" or insta =="" or facebook == "":
        messagebox.showerror("ERROR" , "Please fill the necessary details!!")
        return

        
    data_dict = {'name':name,'phone':phone, 'address':address,'dob':dob,'Gmail':gmail,'Insta':insta,'Facebook':facebook}

    print(data_dict) 

    file = open("contact_list.txt", "a")
    file.write(str(data_dict))
    file.write("\n")
    file.close()

    update_list_box()
        

    messagebox.showinfo("SUCCESS", "CONTACT SAVED!")

def update_list_box():
    global dict_list, select   
    file_display = open("contact_list.txt","r")
    
    select.delete(0,END)
    dict_list.clear()
    for i in file_display:
        dict_list.append(eval(i.strip()))
        print(i.strip())

    # print(dict_list)
    file_display.close()

    for i in range(0,len(dict_list)):
        name = dict_list[i].get('name')
        select.insert(i+1,name)


def create_window1():
    global temp2, select, name_tb, phone_number_tb, address_tb, spinbox_date, spinbox_month, spinbox_year, temp, spinbox_cl, e_tb, ig_tb, fb_tb
    create = Toplevel()
    create.title('Create new contact')

    create.geometry("650x500")
    create['bg'] = "grey"

    # frame 1
    frame_1 = Frame(create)
    frame_1['bg'] = 'grey'
    frame_1.pack()

    #name label
    name_label = Label(frame_1)
    name_label['text'] = "Name"
    name_label.configure(font=("calibri",14,'bold'), bg = "grey")
    name_label.grid(row=0,column=0,padx=35,pady=10)

    #name textbox
    name_tb = Entry(frame_1)
    name_tb['width'] = 23
    name_tb.configure(bg='#CBCBCB',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,justify='center')
    name_tb.grid(row=0,column=1,pady=2,columnspan=3,padx=20)

    #phone number label
    phone_number_label = Label(frame_1)
    phone_number_label['text'] = "Phone Number"
    phone_number_label.configure(font=("calibri",14,'bold'), bg = "grey")
    phone_number_label.grid(row=1,column=0,padx=35,pady=10)

    #phone number textbox 
    phone_number_tb = Entry(frame_1)
    phone_number_tb['width'] = 20
    phone_number_tb.configure(bg='#CBCBCB',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,justify='center')
    phone_number_tb.grid(row=1,column=1,columnspan=3,pady=1,padx=130)

    #address label
    address_label= Label(frame_1)
    address_label['text'] = "Address"
    address_label.configure(font=("calibri",14,'bold'), bg = "grey")
    address_label.grid(row=3,column=0,padx=35,pady=10)

    #address textbox
    address_tb = Text(frame_1)
    address_tb['width'] = 25
    address_tb['height'] = 3
    address_tb.configure(bg='#CBCBCB',font=('Calibri (Body)',12,'bold'),bd=5)
    address_tb.grid(row=3,column=1,columnspan=3,pady=2,padx=20)

    #dob label
    dob_label= Label(frame_1)
    dob_label['text'] = "DOB"
    dob_label.configure(font=("calibri",14,'bold'), bg = "grey")
    dob_label.grid(row=4,column=0,padx=35,pady=10)

    #dob dropdown
    #spinbox - date 
    spinbox_date = Spinbox(frame_1,from_=1,to=31)
    spinbox_date['width'] = 5
    spinbox_date.grid(row=4,column=1)

    # spinbox - month
    spinbox_month = Spinbox(frame_1,from_=1,to=12)
    spinbox_month['width'] = 5
    spinbox_month.grid(row=4,column=2)

    # spinbox - year
    spinbox_year = Spinbox(frame_1,from_=1990,to=2021)
    spinbox_year['width'] = 5
    spinbox_year.grid(row=4,column=3)

    #Social media Frame 2
    frame2 = Frame(create)
    frame2['bg'] = "grey"
    frame2.pack(padx=10,pady=10)
   

    #gmail 
    #E33434
    image2 = Image.open("C:\\Users\\Admin\\Downloads\\gmail.jpeg")
    #Resize the image
    resize_image2 = image2.resize((50,50))
    img2 = ImageTk.PhotoImage(resize_image2)
    label2 = Label(frame2, image=img2)
    label2.image = img2
    label2.grid(row=1,column=0)

    e_tb = Entry(frame2)
    e_tb['width'] = 23
    e_tb['fg'] = "white"
    e_tb.configure(bg='#E33434',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,justify='center')
    e_tb.grid(row=1,column=1,pady=2,padx=20)

    #instagram textbox 
    image3 = Image.open("C:\\Users\\Admin\\Downloads\\insta.jpeg")
    #Resize the image
    resize_image3 = image3.resize((50,50))
    img3 = ImageTk.PhotoImage(resize_image3)
    label3 = Label(frame2, image=img3)
    label3.image = img3
    label3.grid(row=2,column=0)


    ig_tb = Entry(frame2)
    ig_tb['width'] = 23
    ig_tb['fg'] = "white"
    ig_tb.configure(bg='#D153BE',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,justify='center')
    ig_tb.grid(row=2,column=1,pady=2,padx=20)

    #fb textbox
    #1B50D5

    image4 = Image.open("C:\\Users\\Admin\\Downloads\\fb.jpeg")
 
    #Resize the image
    resize_image4 = image4.resize((50,50))
 
    img4 = ImageTk.PhotoImage(resize_image4)
    
    label4 = Label(frame2, image=img4)
    label4.image = img4
    label4.grid(row=3,column=0)


    fb_tb = Entry(frame2)
    fb_tb['width'] = 23
    fb_tb['fg'] = "white"
    fb_tb.configure(bg='#1B50D5',font=('Calibri (Body)',12,'bold'),bd=5,relief=GROOVE,justify='center')
    fb_tb.grid(row=3,column=1,pady=2,padx=20)


    #Save button
    button_save = Button(frame2, command = save)
    button_save['text'] = "SAVE"
    button_save['width'] = button_width
    button_save['height'] = 1
    button_save['font'] = "Calibri"
    button_save['bg'] = "#CBD2D5"
    button_save['fg'] = "black"
    button_save.grid(row=5, column=1, padx=padx_distance, pady=pady_distance) 
    
    
    #Cancel button

    button_cancel = Button(frame2, command=create.destroy)
    button_cancel['text'] = "CANCEL"
    button_cancel['font'] = "Calibri"
    button_cancel['bg'] = "#CBD2D5"
    button_cancel['fg'] = "black"
    button_cancel['width'] = 10
    button_cancel['height'] = 1
    button_cancel.grid(row=6, column=1, padx=10, pady=10)


def delete():

    deleting_option = select.curselection()
    print(deleting_option)

    text = select.get(deleting_option)
    select.delete(deleting_option)
    file_data = open('contact_list.txt','r')
    lines = file_data.readlines()
    file_data.close()
    file_data = open('contact_list.txt','w')
    for i in lines:

        dict_lol = eval(i.strip())
        print(dict_lol)
        if dict_lol.get('name') == text:
            continue
        file_data.write(i)

    file_data.close()

    update_list_box()
    messagebox.showinfo("SUCCESS", "CONTACT DELETED!")

def openinsta():
    global dict_list,ig_tb
    file_data = open("contact_list.txt", "r")
    lines = file_data.readlines()
    for i in range(0,len(dict_list)):
        username_insta = dict_list[i].get('Insta')

    instagramm = ("https://www.instagram.com/"+username_insta+"/")
    webbrowser.open(instagramm)


def openfb():
    global fb_tb, dict_list
    file_data = open("contact_list.txt", "r")
    lines = file_data.readlines()
    for i in range(0,len(dict_list)):
        fbb = dict_list[i].get('Facebook')

    fb = ("https://www.facebook.com/"+fbb+"/")
    webbrowser.open(fb)

    file_data.close()

def openwhatsapp():
    global phone_number_tb, dict_list
    file_data = open("contact_list.txt", "r")
    lines = file_data.readlines()
    for i in range(0,len(dict_list)):
        phonenoo = dict_list[i].get('phone')

    whatsapp_redirect = ("http://wa.me/+91"+phonenoo+"/")
    webbrowser.open(whatsapp_redirect)

    file_data.close()

def opengmail():
    gmail_redirect = ("https://mail.google.com/mail/u/0/#inbox?compose=new")
    webbrowser.open(gmail_redirect)   

def view():
    global temp2, name_label_display,phone_display, address_display, dob_display, facebook_display, insta_display, email_display, zodiac_display, country_display, select, name_tb, phone_number_tb, address_tb, spinbox_date, spinbox_month, spinbox_year, temp, spinbox_cl, e_tb, ig_tb, fb_tb
    vieww = Toplevel()
    vieww.title('Contact details')
    vieww['bg'] = "#121212"
    vieww.geometry("400x400")
    

    view_option = select.curselection()
    text = select.get(view_option)

    # frame 1
    frame1_4 = Frame(vieww)
    frame1_4['bg'] = "#121212"
    frame1_4.pack()

    #Name display label
    name_label_display = Label(frame1_4)
    
    #Phone no. display
    phone_display = Label(frame1_4)
    
    #Adddress display
    address_display = Label(frame1_4)
    
    #DOB display
    dob_display = Label(frame1_4)
    
    #Socials display
    gmail_display = Label(frame1_4)
    
    #labels
    Name_label = Label(frame1_4, text=("Name"), font=('Cambria',12,'bold'),bg='#121212', fg = "white").grid(row=1,column=0,sticky=W, padx=20, pady=5)
    Phone_Number_label = Label(frame1_4, text="Phone Number", font=('Cambria',12,'bold'),bg='#121212',fg = "white").grid(row=2,column=0,sticky=W, padx=20, pady=5)
    Address_label = Label(frame1_4, text="Address", font=('Cambria',12,'bold'),bg='#121212',fg = "white").grid(row=3,column=0,sticky=W, padx=20, pady=5)
    dob_label = Label(frame1_4, text="Date of Birth", font=('Cambria',12,'bold'),bg='#121212',fg = "white").grid(row=4,column=0,sticky=W, padx=20, pady=5)
    gmail_label = Label(frame1_4, text="Email address", font=('Cambria',12,'bold'),bg='#121212',fg = "white").grid(row=5,column=0,sticky=W, padx=20, pady=5)

    
    file_data = open('contact_list.txt', 'r')
    lines = file_data.readlines()

    for i in lines:
        dict_lol = eval(i.strip())

        if dict_lol.get('name') == text:

            name_label_display['text'] = text
            name_label_display.configure(bg= "#121212", fg = "white", font= "Cambria, 12")
            name_label_display.grid(row= 1, column =1, padx = 5, pady = 5 )
            phone_display['text']= dict_lol.get('phone')
            phone_display.configure(bg= "#121212",fg = "white", font= "Cambria, 12")
            phone_display.grid(row= 2, column =1, padx = 5, pady = 5 )
            address_display['text'] = dict_lol.get('address')
            address_display.configure(bg= "#121212",fg = "white", font= "Cambria, 12")
            address_display.grid(row= 3, column =1, padx = 5, pady = 5 )
            dob_display['text'] = dict_lol.get('dob')
            dob_display.configure(bg= "#121212",fg = "white", font= "Cambria, 12")
            dob_display.grid(row= 4, column =1, padx = 5, pady = 5 )
            gmail_display['text'] = dict_lol.get('Gmail')
            gmail_display.configure(bg= "#121212",fg = "white", font= "Cambria, 12")
            gmail_display.grid(row= 5, column =1, padx = 5, pady = 5 )
            '''
            insta_display['label'] = dict_lol.get('insta')
            insta_display.configure(fg = "black", font= "Cambria, 12")
            insta_display.grid(row= 5, column =1, padx = 5, pady = 5 )
            '''
    #frame2_4
    frame2_4 = Frame(vieww)
    frame2_4['bg'] = "#121212"
    frame2_4.pack()
   

    #Instagram button image
    image11 = Image.open("C:\\Users\\Admin\\Downloads\\insta.jpeg")
 
    #Resize the image
    resize_image11 = image11.resize((70,70))
 
    img11 = ImageTk.PhotoImage(resize_image11)
    
    label111 = Label(frame2_4, image=img11)
    label111.image = img11
    label111.grid(row=5,column=0)
    
    #Gmail button image
    image12 = Image.open("C:\\Users\\Admin\\Downloads\\gmail.jpeg")
 
    #Resize the image
    resize_image12 = image12.resize((70,70))
 
    img12 = ImageTk.PhotoImage(resize_image12)
    
    label112 = Label(frame2_4, image=img12)
    label112.image = img12
    label112.grid(row=5,column=1)
    
    #Whatsapp button image
    image13 = Image.open("C:\\Users\\Admin\\Downloads\\whatsappp.jpeg")
 
    #Resize the image
    resize_image13 = image13.resize((70,70))
 
    img13 = ImageTk.PhotoImage(resize_image13)
    
    label113 = Label(frame2_4, image=img13)
    label113.image = img13
    label113.grid(row=5,column=2)

    #Facebook button image
    image14 = Image.open("C:\\Users\\Admin\\Downloads\\fb.jpeg")
 
    #Resize the image
    resize_image14 = image14.resize((70,70))
 
    img14 = ImageTk.PhotoImage(resize_image14)
    
    label114 = Label(frame2_4, image=img14)
    label114.image = img14
    label114.grid(row=5,column=3)
    
    
    #INSTAGRAM BUTTON
    button_insta = Button(frame2_4, command= openinsta)
    button_insta.grid(row=5, column=0)

    #GMAIL BUTTON
    button_gmail = Button(frame2_4, command= opengmail)
    button_gmail.grid(row=5, column=1)      

    #WHATSAPP BUTTON
    button_insta = Button(frame2_4, command= openwhatsapp)
    button_insta.grid(row=5, column=2)

    #FACEBOOK BUTTON
    button_gmail = Button(frame2_4, command= openfb)
    button_gmail.grid(row=5, column=3)        
               
    
    file_data.close()

def edit():
    editt = Toplevel()
    editt.title('Edit contact')

    editt.geometry("500x500")
    

    view_option = select.curselection()
    text = select.get(view_option)
        # frame 1
    frame1_5 = Frame(editt)
    frame1_5['bg'] = "white"
    frame1_5.pack()

    #Name display label
    name_entry = Entry(frame1_5)
    name_entry.grid(row = 0, column = 0)
    #Phone no. display
    phone_entry = Entry(frame1_5)
    phone_entry.grid(row = 1, column = 0, padx = 10, pady= 10)
    #Adddress display
    address_text = Text(frame1_5)
    address_text.grid(row= 2, column= 0, padx= 10, pady= 10)
    #DOB display
    dob_entry = Entry(frame1_5)
    dob_entry.grid(row= 3, column= 0, padx= 10, pady= 10)
  
    #Socials display
    email_entry= Entry(frame1_5)
    email_entry.grid(row= 8, column= 0, padx= 10, pady= 10)

    insta_entry = Entry(frame1_5)
    insta_entry.grid(row= 9, column= 0, padx= 10, pady= 10)

    facebook_entry = Entry(frame1_5)
    facebook_entry.grid(row= 10, column= 0, padx= 10, pady= 10)




    file_data = open('contact_list.txt', 'r')
    lines = file_data.readlines()



    
    
# frame 1
frame1 = Frame(root)
frame1.pack()



BG = PhotoImage(file="bgimage.png")
bg_label= Label(root,image=BG)
bg_label.place(x=0,y=0)
# label - GEN-Z CONTACTS DIRECTORY
labeltitle = Label(frame1)
labeltitle['text'] = "GEN-Z CONTACTS DIRECTORY"
labeltitle['font'] = ("Arial", 15)
labeltitle['fg'] = "black"
labeltitle.grid(row=0, column=0)



padx_distance = 20
pady_distance = 7
button_width = 10

# frame 2
frame_2 = Frame(root)
frame_2.pack(pady = 25)
frame_2['bg']="#121212"



# button1 - Create
button_create = Button(frame_2, command= create_window1)
button_create['text'] = "CREATE NEW"
button_create['font'] = "Calibri"
button_create['bg'] = "#CBD2D5"
button_create['fg'] = "black"
button_create['width'] = button_width
button_create.grid(row=1, column=1, padx=padx_distance, pady=pady_distance)


# button2 - Display all
button_display = Button(frame_2, command = showall_window2)
button_display['text'] = "SHOW ALL"
button_display['font'] = "Calibri"
button_display['bg'] = "#CBD2D5"
button_display['fg'] = "black"
button_display['width'] = button_width
button_display.grid(row=2, column=1, padx=padx_distance, pady=pady_distance)

# button4 - Exit
button_exit = Button(frame_2, command = root.destroy)
button_exit['text'] = "EXIT"
button_exit['font'] = "Calibri"
button_exit['bg'] = "#CBD2D5"
button_exit['fg'] = "black"
button_exit['width'] = button_width
button_exit.grid(row=4, column=1, padx=padx_distance, pady=pady_distance)

root.mainloop()