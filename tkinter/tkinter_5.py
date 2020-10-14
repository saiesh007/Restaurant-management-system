from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image  # pip install Pillow

root = tk.Tk()
root.title("my GUI")
root.geometry("300x300")
img = ImageTk.PhotoImage(Image.open(r'D:\code\Restaurant management system\cafe.ico'))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()