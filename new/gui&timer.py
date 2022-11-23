from doctest import master
import threading
from time import strftime, time
from time import sleep
import tkinter as tk
from tkinter import StringVar
import customtkinter as ctk 
from tkinter import *
#import timer1 
#from timer1 import counter






ctk.set_appearance_mode('system') #dark and light mode from windows
ctk.set_default_color_theme('green')




class App(ctk.CTk):
    WIDTH = 780
    HEIGHT = 520
    

   

        
        
        #self.e1_str=ctk.StringVar()
        #self.e1_str.set(self.ste)

    def __init__ (self):
        super(App,self).__init__()



        self.title("Buttons")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self._alarm_id = None

        
  # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    
        self.frame_right = ctk.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
     


    
        

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = ctk.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        self.ste=strftime('%H:%M:%S')
       # self.e_1=StringVar()
       # self.tt=strftime('%H:%M:%S')
       # self.e_1.get
       # self.e_1.set(self.tt)
        

        self.label_info_1 = ctk.CTkLabel(master=self.frame_info,
                                            text=self.ste,
                                            height=100,
                                            corner_radius=6,  # <- custom corner radius
                                            fg_color=("white", "gray"),  # <- custom tuple-color
                                            justify=tk.LEFT)                                    
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)    
        #self.label_info_1.after(1000, self.ste)
        #self.label_info_1.config()
        #self.label_info_1.after(1000, self.e_1)

        #self.progressbar = ctk.CTkProgressBar(master=self.frame_info)
        #self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        self.button_1 = ctk.CTkButton(master=self.frame_info,
                                                text="Start",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.toggle
                                                )
        self.button_1.grid(row=2, column=0, columnspan=1, rowspan=2, pady=20, padx=20, sticky="w")
        
        self.button_2 = ctk.CTkButton(master=self.frame_info,
                                                text="Button2",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=None
                                                )
        self.button_2.grid(row=2, column=2, columnspan=1, pady=20, padx=20, sticky="e")


        self.paused = True

    def toggle(self):
        if self.paused:
            self.paused = False
            self.button_1.configure(text='Stop')
            self.oldtime = time()
            self.run_timer()
        else:
            self.paused = True
            self.oldtime = time()
            self.button_1.configure(text='Start')

    def run_timer(self):
        if self.paused:
            return
        delta = int(time() - self.oldtime)
        timestr = '{:02}:{:02}'.format(*divmod(delta, 60))
        self.label_info_1.configure(text=timestr)
        self.label_info_1.after(1000, self.run_timer) 

    
  
    
   
            
    

    def change_appearance_mode(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()



def countdown(t):
    
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            sleep(1)
            t -= 1
        
        print('Fire in the hole!!')


        t = input("Enter the time in seconds: ")
#countdown(int(t))


if __name__=="__main__":
    app=App()
    app.mainloop()
    thread1=threading.Thread(target=countdown()).start()
    countdown(int())
    
