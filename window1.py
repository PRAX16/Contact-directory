from tkinter import *

# creating the root window
root = Tk()

# root config
root.geometry("417x350")
root.title("Contacts Directory")



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
button_create = Button(frame_2)
button_create['text'] = "Create New!"
button_create['bg'] = "white"
button_create['fg'] = "black"
button_create['width'] = button_width
button_create['height'] = 1
button_create.grid(row=1, column=1, padx=padx_distance, pady=pady_distance)

# button2 - Display all
button_display = Button(frame_2)
button_display['text'] = "Show All!"
button_display['bg'] = "white"
button_display['fg'] = "black"
button_display['width'] = button_width
button_display['height'] = 1
button_display.grid(row=2, column=1, padx=padx_distance, pady=pady_distance)



# button3 - Delete
button_delete = Button(frame_2)
button_delete['text'] = "Delete!"
button_delete['bg'] = "white"
button_delete['fg'] = "black"
button_delete['width'] = button_width
button_delete['height'] = 1
button_delete.grid(row=3, column=1, padx=padx_distance, pady=pady_distance)



# button4 - Exit
button_exit = Button(frame_2)
button_exit['text'] = "Exit"
button_exit['bg'] = "white"
button_exit['fg'] = "black"
button_exit['width'] = button_width
button_exit['height'] = 1
button_exit.grid(row=4, column=1, padx=padx_distance, pady=pady_distance)



root.mainloop()