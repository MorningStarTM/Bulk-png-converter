from tkinter import*
import customtkinter
from tkinter import ttk
import cv2
import os
from glob import glob
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import time

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("650x320")
root.title("PNG Converter")
root.iconbitmap("E:\\ML_test\\app\\pics\\converter.ico")

#function for get path
def get_select_path_from_entry():
    path = select_entry.get()
    return path

#function to get save directory
def get_save_path_from_entry():
    path = save_entry.get()
    return path

#function for get path using button
def browse_select_folder():
    folder = filedialog.askdirectory()
    select_entry.insert(0,folder)

#function to get path of save directory
def browse_save_folder():
    folder = filedialog.askdirectory()
    save_entry.insert(0,folder)


#function for convert the image
def convert_image():
    #variable for check work done
    file_size = 0
    #get the path of select directory
    select_path = get_select_path_from_entry()
    #Get the path of save directory
    save_path = get_save_path_from_entry()
    #Show error message
    

    if select_path == "":
        messagebox.showerror("Empty", "Path is empty")
    
    #get the file path of imgages
    images = sorted(glob(os.path.join(select_path, "*.*")))
    #extract the name for image
    name = save_path.split("/")[-1]
    #show progress bar
    progress.place(relx=0.1, rely=0.85)

    for i in range(len(images)):
        #read image
        image = cv2.imread(images[i], cv2.IMREAD_COLOR)
        #resize image
        image = cv2.resize(image, (200, 200))
        #save image
        cv2.imwrite(f"{save_path}/{name}_{i}.png", image)
        file_size += 1
        #increment value in progress bar
        progress['value'] += int(100/(len(images)-1))
        root.update_idletasks()
        time.sleep(1)

        #show message when process completed
        if progress['value'] > 100:
            messagebox.showinfo("Done", "Successfully converted")
            #hide the progress bar
            progress.place(relx=-0.9, rely=-0.9)
        
        


#intitalize the font for label
my_font_1 = customtkinter.CTkFont(family="Arial", size=15)
#intitalize the font for entry
my_font_2 = customtkinter.CTkFont(family="Arial", size=16)
#initalize the font for button
my_font_3 = customtkinter.CTkFont(family="Arial Rounded MT", size=26)

#heading label
select_path = customtkinter.CTkLabel(root, text="Select Path", font=my_font_1)
select_path.place(relx=0.1, rely=0.2)

save_path = customtkinter.CTkLabel(root, text="Save Path", font=my_font_1)
save_path.place(relx=0.1, rely=0.4)



#Entry for select path 
select_entry = customtkinter.CTkEntry(root, width=400, font=my_font_2)
select_entry.place(relx=0.25, rely=0.2)

#entry for save path
save_entry = customtkinter.CTkEntry(root, width=400, font=my_font_2)
save_entry.place(relx=0.25, rely=0.4)

#button image
select_image = customtkinter.CTkImage(Image.open("E:\\ML_test\\app\\pics\\folder.png"))

#button for select path
select_button = customtkinter.CTkButton(master=root, text="", image=select_image, width=10, command=browse_select_folder)
select_button.place(relx=0.90, rely=0.243, anchor=CENTER)

#button for save path
save_button = customtkinter.CTkButton(master=root, text="", image=select_image, width=10, command=browse_save_folder)
save_button.place(relx=0.90, rely=0.44, anchor=CENTER)

#convert Button
convert_button = customtkinter.CTkButton(root, text="Convert", font=my_font_3, width=540, height=50, command=convert_image)
convert_button.place(relx=0.1, rely=0.6)

#progress bar
progress = ttk.Progressbar(root,orient=HORIZONTAL, mode="determinate", length=670)
progress.place(relx=-0.9, rely=0.85)

root.mainloop()