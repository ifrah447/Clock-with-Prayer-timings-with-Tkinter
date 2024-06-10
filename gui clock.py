import time
import tkinter as tk
from tkinter import *
background_color=input("enter a color (ALL CAPS) for background: ")
color=input("enter text color: ")
def tick(time1= ' '):
    time2=time.strftime('%I :%M :%S')
    if time2 != time1:
        time1= time2
        clock_frame.config(text=time2)
        clock_frame.after(200,tick)

def fajar_namaz():
    fajar.config(text="05:57          فجر")
def zuhar_namaz():
    zuhar.config(text="12:41          ظہر")
def asr_namaz():
    asr.config(text="03:46          عصر")
def maghrib_namaz():
    maghrib.config(text="06:07          مغرب")
def isha_namaz():
    isha.config(text="07:21          عشاء")
def jummah_namaz():
    jummah.config(text="01:30          جمعہ")

root=tk.Tk()
clock_frame=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
clock_frame.pack(fill='both',expand=1)
fajar=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
fajar.pack(fill=X)
zuhar=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
zuhar.pack(fill=X)
asr=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
asr.pack(fill=X)
maghrib=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
maghrib.pack(fill=X)
isha=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
isha.pack(fill=X)
jummah=tk.Label(root,font=('arial 50 bold'),bg=background_color,fg=color)
jummah.pack(fill=X)

root.attributes('-fullscreen',True)
root.configure(background="lightgreen")
tick()
fajar_namaz()
zuhar_namaz()
asr_namaz()
maghrib_namaz()
isha_namaz()
jummah_namaz()
root.mainloop()
