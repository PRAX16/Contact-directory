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
spinbox_cl = 0
e_tb  = 0
ig_tb = 0
fb_tb = 0
select = 0
name_label_display = 0
phone_display = 0 
address_display = 0 
dob_display = 0
relation_display = 0
closeness_display = 0 
zodiac_display = 0
country_display = 0
email_display = 0
insta_display = 0
facebook_display = 0




def showall_window2():
    global select
    showall = Toplevel()
    showall.title('Display All contacts')

    showall.geometry("500x500")
    showall['bg'] = "white"

    #frame 1 for 3rd window
    frame1_3 = Frame(showall)
    frame1_3.pack()

    #Sort by label
    sort_label = Label(frame1_3, text="Sort by")
    sort_label.grid(row=0,column=0)
    
    #Sort dropdown
    list_of_sorting = ["Last added","Alphabetically","Closeness level"]
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
    frame3_3 = Frame(showall, bg = "black")
    frame3_3.pack()

    Button(frame3_3,text="EDIT").grid(row = 1, column = 0,padx= 10, pady=10)
    Button(frame3_3,text="DELETE", command = delete).grid(row = 1, column = 1,padx= 10, pady=10)
    Button(frame3_3,text="VIEW", command = view).grid(row = 1, column = 2,padx= 10, pady=10)

def save():
    name = name_tb.get()
    phone = phone_number_tb.get()
    address = address_tb.get("1.0",END)
    dob_date = spinbox_date.get()
    dob_month = spinbox_month.get()
    dob_year = spinbox_year.get()
    dob = datetime.date(int(dob_year), int(dob_month), int(dob_date))
    relation = temp.get()
    closeness = spinbox_cl.get()
    gmail = e_tb.get()
    insta = ig_tb.get()
    facebook = fb_tb.get()
        
    '''
    if name == "" or phone == "":
        messagebox.showerror('Error','Please fill in the Name or Phone no.!')
        return
    '''

        
    data_dict = {'name':name,'phone':phone,'address':address,'dob':dob,'relation':relation,'closeness level':closeness,'Gmail':gmail,'Insta':insta,'Facebook':facebook}

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
    global select, name_tb, phone_number_tb, address_tb, spinbox_date, spinbox_month, spinbox_year, temp, spinbox_cl, e_tb, ig_tb, fb_tb
    create = Toplevel()
    create.title('Create new contact')

    create.geometry("550x800")
    create['bg'] = "black"
    # frame 1
    frame_1 = Frame(create)
    frame_1.pack()

    #name label
    name_label = Label(frame_1)
    name_label['text'] = "Name"
    name_label.grid(row=0,column=0,padx=35,pady=10)

    #name textbox
    name_tb = Entry(frame_1)
    name_tb['width'] = 23
    name_tb.grid(row=0,column=1,pady=2,columnspan=3,padx=20)

    #phone number label
    phone_number_label = Label(frame_1)
    phone_number_label['text'] = "Phone Number"
    phone_number_label.grid(row=1,column=0,padx=35,pady=10)

    #phone number textbox 
    phone_number_tb = Entry(frame_1)
    phone_number_tb['width'] = 20
    phone_number_tb.grid(row=1,column=1,columnspan=3,pady=1,padx=130)

    #country code dropdown
    list_of_ccodes = ["+91","+1"]
    temp2 = StringVar()

    #Dropdown / Option menu - select relation
    relation_optionmenu = OptionMenu(frame_1, temp2, *list_of_ccodes)
    temp2.set("+")
    relation_optionmenu.grid(row=1,column=1,columnspan=1,padx=35,pady=10)


    #address label
    address_label= Label(frame_1)
    address_label['text'] = "Address"
    address_label.grid(row=3,column=0,padx=35,pady=10)

    #address textbox
    address_tb = Text(frame_1)
    address_tb['width'] = 25
    address_tb['height'] = 3
    address_tb.grid(row=3,column=1,columnspan=3,pady=2,padx=20)

    #dob label
    dob_label= Label(frame_1)
    dob_label['text'] = "DOB"
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

    #relation label
    relation_label = Label(frame_1)
    relation_label['text'] = "Relation"
    relation_label.grid(row=5,column=0,padx=35,pady=10)

    #relation dropdown
    list_of_relation = ["Family","Friends","Co-workers"]
    temp = StringVar()

    #Dropdown / Option menu - select relation
    relation_optionmenu = OptionMenu(frame_1, temp, *list_of_relation)
    temp.set("Select your relation")
    relation_optionmenu.grid(row=5,column=1,columnspan=3,padx=35,pady=10)


    #closeness level label
    closeness_level_label = Label(frame_1)
    closeness_level_label['text'] = "Closeness level"
    closeness_level_label.grid(row=7,column=0,padx=35,pady=10)

    #closeness level spinbox
    spinbox_cl = Spinbox(frame_1,from_=1,to=10)
    spinbox_cl['width'] = 5
    spinbox_cl.grid(row=7,column=1)

    #Social media Frame 2

    frame2 = Frame(create)
    frame2.pack(padx=10,pady=10)
   

    #gmail 

    image2 = Image.open("C:\\Users\\Admin\\Downloads\\gmail.jpeg")
 
    #Resize the image
    resize_image2 = image2.resize((50,50))
 
    img2 = ImageTk.PhotoImage(resize_image2)
 
    label2 = Label(frame2, image=img2)
    label2.image = img2
    label2.grid(row=1,column=0)

    e_tb = Entry(frame2)
    e_tb['width'] = 23
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
    ig_tb.grid(row=2,column=1,pady=2,padx=20)

    #fb textbox

    image4 = Image.open("C:\\Users\\Admin\\Downloads\\fb.jpeg")
 
    #Resize the image
    resize_image4 = image4.resize((50,50))
 
    img4 = ImageTk.PhotoImage(resize_image4)
 
    label4 = Label(frame2, image=img4)
    label4.image = img4
    label4.grid(row=3,column=0)


    fb_tb = Entry(frame2)
    fb_tb['width'] = 23
    fb_tb.grid(row=3,column=1,pady=2,padx=20)
    

    #Save button
    button_save = Button(frame2, command = save)
    button_save['text'] = "Save"
    button_save['bg'] = "light blue"
    button_save['fg'] = "black"
    button_save['width'] = button_width
    button_save['height'] = 1
    button_save.grid(row=5, column=1, padx=padx_distance, pady=pady_distance) 
    
    
    #Cancel button

    button_cancel = Button(frame2, command=create.destroy)
    button_cancel['text'] = "Cancel"
    button_cancel['bg'] = "light blue"
    button_cancel['fg'] = "black"
    button_cancel['width'] = 10
    button_cancel['height'] = 1
    button_cancel.grid(row=6, column=1, padx=10, pady=10)


    '''
    #Define a callback function
    def callback(url):
        webbrowser.open_new_tab(url)

        #Create a Label to display the link
        link = Label(showall, text="INSTAGRAM",font=('Helveticabold', 15), fg="red", cursor="hand2")
        link.bind("<Button-1>", lambda e: callback("http://www.instagram.com/{insta}/"))
        link.grid(row=1,column=0)   
    '''
def delete():

    deleting_option = select.curselection()
    print(deleting_option)

    text = select.get(deleting_option)
    select.delete(deleting_option)
    file_data = open('contact_list.txt','r')
    lines = file_data.readlines()
    # updated_lines = lines[:]
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
'''
def reset():

    .set("")
    .set("")
    .delete("1.0","end")
'''
def view():
    global name_label_display,phone_display, address_display, dob_display, relation_display, closeness_display, facebook_display, insta_display, email_display, zodiac_display, country_display, select, name_tb, phone_number_tb, address_tb, spinbox_date, spinbox_month, spinbox_year, temp, spinbox_cl, e_tb, ig_tb, fb_tb
    vieww = Toplevel()
    vieww.title('Contact details')

    vieww.geometry("500x500")
    vieww['bg'] = "black"


    #reset()
    view_option = select.curselection()
    text = select.get(view_option)

    file_data = open('contact_list.txt', 'r')
    lines = file_data.readlines()

    for i in lines:
        dict_lol = eval(i.strip())

        if dict_lol.get('name') == text:

            name_label_display.set(text)
            phone_display.set(dict_lol.get('phone'))
            address_display.insert(END,dict_lol.get('address'))


    # frame 1
    frame1_4 = Frame(vieww)
    frame1_4.pack()

    #Name display label
    name_label_display = Entry(frame1_4)
    name_label_display.grid(row = 0, column = 0)
    #Phone no. display
    phone_display = Entry(frame1_4)
    phone_display.grid(row = 1, column = 0, padx = 10, pady= 10)
    #Adddress display
    address_display = Text(frame1_4)
    address_display.grid(row= 2, column= 0, padx= 10, pady= 10)
    #DOB display
    dob_display = Entry(frame1_4)
    dob_display.grid(row= 3, column= 0, padx= 10, pady= 10)
    #Relation display
    relation_display = Entry(frame1_4)
    relation_display.grid(row= 4, column= 0, padx= 10, pady= 10)
    #Closeness level display
    closeness_display = Entry(frame1_4)
    closeness_display.grid(row= 5, column= 0, padx= 10, pady= 10)
    #Zodiac sign display
    zodiac_display = Entry(frame1_4)
    zodiac_display.grid(row= 6, column= 0, padx= 10, pady= 10)
    #Country display
    country_display = Entry(frame1_4)
    country_display.grid(row= 7, column= 0, padx= 10, pady= 10)
    #Socials display
    email_display = Entry(frame1_4)
    email_display.grid(row= 8, column= 0, padx= 10, pady= 10)

    insta_display = Entry(frame1_4)
    insta_display.grid(row= 9, column= 0, padx= 10, pady= 10)

    facebook_display = Entry(frame1_4)
    facebook_display.grid(row= 10, column= 0, padx= 10, pady= 10)
    #Send email







    
    
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
button_create['text'] = "Create New!"
button_create['bg'] = "white"
button_create['fg'] = "black"
button_create['width'] = button_width
button_create['height'] = 1
button_create.grid(row=1, column=1, padx=padx_distance, pady=pady_distance)

# button2 - Display all
button_display = Button(frame_2, command = showall_window2)
button_display['text'] = "Show All!"
button_display['bg'] = "white"
button_display['fg'] = "black"
button_display['width'] = button_width
button_display['height'] = 1
button_display.grid(row=2, column=1, padx=padx_distance, pady=pady_distance)

# button4 - Exit
button_exit = Button(frame_2, command = root.destroy)
button_exit['text'] = "Exit"
button_exit['bg'] = "white"
button_exit['fg'] = "black"
button_exit['width'] = button_width
button_exit['height'] = 1
button_exit.grid(row=4, column=1, padx=padx_distance, pady=pady_distance)

root.mainloop()