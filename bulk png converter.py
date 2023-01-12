from tkinter import*
import customtkinter
import cv2
import os
from glob import glob
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("650x320")
root.title("PNG Converter")
root.iconbitmap("E:\\ML_test\\app\\pics\\converter.ico")


#heading label


#intitalize the font
my_font = customtkinter.CTkFont(family="Times New Roman", size=12)
#Entry for select path 
select_entry = customtkinter.CTkEntry(root, width=400, font=my_font)
select_entry.place(relx=0.3, rely=0.2)

#entry for save path
save_entry = customtkinter.CTkEntry(root, width=400, font=my_font)
save_entry.place(relx=0.3, rely=0.4)

#button image
select_image = customtkinter.CTkImage(Image.open("E:\\ML_test\\app\\pics\\folder.png"))

#button for select path
select_button = customtkinter.CTkButton(master=root, text="", image=select_image, width=10)
select_button.place(relx=0.95, rely=0.243, anchor=CENTER)

#button for save path
save_button = customtkinter.CTkButton(master=root, text="", image=select_image, width=10)
save_button.place(relx=0.95, rely=0.44, anchor=CENTER)



root.mainloop()