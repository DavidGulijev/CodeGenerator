#importing libraries
import random
import string
import tkinter as tk
import sys
import time
from tkinter import *
from PIL import Image, ImageTk

#the configuration of the window
root = tk.Tk()
root.title("CodeGen")
root.configure(background='gray14')

#background settings
canvas = tk.Canvas(root, width=600, height=500, bg ="gray14", borderwidth =0, highlightthickness=0)
canvas.grid(columnspan=8, rowspan=7)

#logo bit
logo = Image.open('logo.png') # < This part of the code should work on the users end. But if it doesnt, then its probably because it cant find the directory
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg="gray14")
logo_label.image = logo
logo_label.grid(column=2, row=0)


#generation for the number code
def get_pass(length):
  chars = string.digits
  return "".join(random.choice(chars) for char in range(length))
  
#this is where some of the error handling comes in for the input box
#box_number.get().isspace()==3: wont work, I think this is a bug with tkinter
def box():
    if len(box_number.get())==11:
      answer.config(text="Successful")
      run.config(text=box_number.get())
  
    else: 
      answer.config(text="Please use 8 digits & spaced out by 2")

#this is where the numbers is combined. pdw is just used as an abreviation to save some time.
def total ():
  pdw1 = get_pass(2)
  pdw2 = get_pass(2)
  pdw3 = get_pass(2)
  pdw4 = get_pass(2)
  add_total = pdw1 +" " + pdw2+" "+  pdw3+" "  + pdw4
  print (add_total)
  run.config(text=add_total)

#this is where the session data is saved
def clipper():
  copy_all = ("Saved: "+ "'"+run['text']+"'" +"'"+" Date & Time: "+day + ", " + date)
  root.clipboard_clear()
  root.clipboard_append(copy_all)
  answer.config(text="Copied to clipboard")

#this is the clock used to put the date and times up // they are set to global so i can call on them
def clock():
  hour = time.strftime("%H:")
  minute = time.strftime("%M:")
  second = time.strftime("%S")
  global day
  day = (hour + minute +second)
  global date
  date = time.strftime("%b %d %Y")
  time_label.config(text=day, fg="goldenrod1", bg="gray14")
  time_label.after(1000, clock)
  time_label2.config(text=date)

#running the generator
run = Label(root, font=("Helvetica", 30), fg="goldenrod1", bg="gray14")
run.grid(column=2, row=1)

#clock labels
time_label = Label(root, text="", font=("Helvetica", 28), fg="goldenrod1", bg="gray14")
time_label.grid(column=3, row=0,)
  
time_label2 = Label(root, text="", font=("Helvetica", 15), fg="goldenrod1", bg="gray14")
time_label2.grid(column=3, row=1)

#just some text to prompt the user what to do
box_label = Label(root, font=("Helvetica", 12),text="Enter your own data", fg="goldenrod1", bg="gray14")
box_label.grid(column=2, row=6)

#the input box
box_number = Entry(root,font=("Helvetica", 14),fg="goldenrod1", bg="dim gray")
box_number.grid(column=2, row=5)

#the enter button for input box
box_button = Button(root,font=("Helvetica", 14), text="Enter", fg="gray14", bg="goldenrod1", command=box)
box_button.grid(column=3, row=5)

#the error handling text
answer = Label(root, text='',fg="goldenrod1", bg="gray14")
answer.grid(column=2, row=7)

#the button to generate
generate = Button(width=15, height=3, font=("Helvetica", 14, "bold"), fg="gray14", bg="goldenrod1",text="Generate", command=total)
generate.grid(column=3, row=4)

#the button to save
clipper = Button(width=15, height=3, font=("Helvetica", 14, "bold"),text="Save", fg="gray14", bg="goldenrod1", command=clipper)
clipper.grid(column=2, row=4)

#instructions on the screen
instructions = tk.Label(root, text="Select 'generate' to create a unique code", font="calibri", fg="goldenrod1", bg="gray14")
instructions.grid(column=2, row=2)

#this is where all of the functions are called to run them
clock()
total()
root.mainloop()