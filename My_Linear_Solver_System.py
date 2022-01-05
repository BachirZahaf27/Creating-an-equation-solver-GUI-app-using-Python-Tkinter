#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.0
#  in conjunction with Tcl version 8.6
#    Jan 05, 2022 05:08:53 PM CET  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import My_Linear_Solver_System_support

class solver:
    def doRefresh(self):
         self.Entry1.delete(0, END)
         self.Entry2.delete(0, END)
         self.Entry3.delete(0, END)
         self.Entry4.delete(0, END)
         self.Entry5.delete(0, END)
         self.Entry6.delete(0, END)
         self.Entry7.delete(0, END)
         self.Entry8.delete(0, END)
         self.Entry9.delete(0, END)
         self.Entry10.delete(0, END)
         self.Entry11.delete(0, END)
         self.Entry12.delete(0, END)
         self.Entry13.delete(0, END)
         self.Entry14.delete(0, END)
         self.Entry15.delete(0, END)
         return
             
    def solveMatrix(self):
        condition1 = ((self.Entry1.get() is "") or (self.Entry2.get() is "") or (self.Entry3.get() is "") or
		      (self.Entry4.get() is "") or (self.Entry5.get() is "") or (self.Entry6.get() is "") or
		      (self.Entry7.get() is "") or (self.Entry8.get() is "") or (self.Entry9.get() is "") or
		      (self.Entry10.get() is "") or (self.Entry11.get() is "") or (self.Entry12.get() is ""))
        if (condition1 is True):
                fmsgbox.showinfo("Solver", "Empty user input. Please check!")
                return
        matrix1 = np.array([[float(self.Entry1.get()),float(self.Entry2.get()),float(self.Entry3.get())],
                    	    [float(self.Entry5.get()),float(self.Entry6.get()),float(self.Entry7.get())],
                            [float(self.Entry9.get()),float(self.Entry10.get()),float(self.Entry11.get())]])
        
	
	
	matrix2 = np.linalg.inv(matrixl)
        matrix3 = np.array([float(self.Entry4.get()), float(self.Entry8.get()), float(self.Entry12.get())])
        results = np.round(matrix2.dot(matrix3),decimals=10)
        self.Entry13.insert(0,results[0])
        self.Entry14.insert(0,results[1])
        self.Entry15.insert(0,results[2])
        return
    
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("651x490+349+124")
        top.minsize(120, 1)
        top.maxsize(1444, 881)
        top.resizable(1,  1)
        top.title("solver")
        top.configure(background="#80ffff")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.077, rely=0.612, height=34, width=67)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Solve''')#, command=self.solveMatrix()

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.215, rely=0.612, height=34, width=67)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Clear''')#, command=self.doRefresh()

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(relx=0.078, rely=0.078, height=20, width=63)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Equation 1''')
        self.TLabel1.configure(compound='left')

        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(relx=0.078, rely=0.249, height=18, width=66)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Equation 2''')
        self.TLabel2.configure(compound='left')

        self.TLabel3 = ttk.Label(self.top)
        self.TLabel3.place(relx=0.077, rely=0.429, height=17, width=66)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Equation 3''')
        self.TLabel3.configure(compound='left')

        self.Entry1 = ttk.Entry(self.top)
        self.Entry1.place(relx=0.108, rely=0.151, relheight=0.057
                , relwidth=0.112)
        self.Entry1.configure(takefocus="")
        self.Entry1.configure(cursor="ibeam")

        self.Entry2 = ttk.Entry(self.top)
        self.Entry2.place(relx=0.292, rely=0.151, relheight=0.057
                , relwidth=0.112)
        self.Entry2.configure(takefocus="")
        self.Entry2.configure(cursor="ibeam")

        self.Entry3 = ttk.Entry(self.top)
        self.Entry3.place(relx=0.476, rely=0.151, relheight=0.057
                , relwidth=0.112)
        self.Entry3.configure(takefocus="")
        self.Entry3.configure(cursor="ibeam")

        self.Entry4 = ttk.Entry(self.top)
        self.Entry4.place(relx=0.661, rely=0.151, relheight=0.057
                , relwidth=0.112)
        self.Entry4.configure(takefocus="")
        self.Entry4.configure(cursor="ibeam")

        self.TLabel4_1 = ttk.Label(self.top)
        self.TLabel4_1.place(relx=0.23, rely=0.151, height=27, width=30)
        self.TLabel4_1.configure(background="#d9d9d9")
        self.TLabel4_1.configure(foreground="#000000")
        self.TLabel4_1.configure(font="TkDefaultFont")
        self.TLabel4_1.configure(relief="flat")
        self.TLabel4_1.configure(anchor='w')
        self.TLabel4_1.configure(justify='left')
        self.TLabel4_1.configure(text='''X +''')
        self.TLabel4_1.configure(compound='left')

        self.TLabel4_2 = ttk.Label(self.top)
        self.TLabel4_2.place(relx=0.415, rely=0.151, height=27, width=30)
        self.TLabel4_2.configure(background="#d9d9d9")
        self.TLabel4_2.configure(foreground="#000000")
        self.TLabel4_2.configure(font="TkDefaultFont")
        self.TLabel4_2.configure(relief="flat")
        self.TLabel4_2.configure(anchor='w')
        self.TLabel4_2.configure(justify='left')
        self.TLabel4_2.configure(text='''Y +''')
        self.TLabel4_2.configure(compound='left')

        self.TLabel4_3 = ttk.Label(self.top)
        self.TLabel4_3.place(relx=0.599, rely=0.151, height=27, width=30)
        self.TLabel4_3.configure(background="#d9d9d9")
        self.TLabel4_3.configure(foreground="#000000")
        self.TLabel4_3.configure(font="TkDefaultFont")
        self.TLabel4_3.configure(relief="flat")
        self.TLabel4_3.configure(anchor='w')
        self.TLabel4_3.configure(justify='left')
        self.TLabel4_3.configure(text='''Z  =''')
        self.TLabel4_3.configure(compound='left')

        self.Entry5 = ttk.Entry(self.top)
        self.Entry5.place(relx=0.092, rely=0.327, relheight=0.057
                , relwidth=0.112)
        self.Entry5.configure(takefocus="")
        self.Entry5.configure(cursor="ibeam")

        self.TLabel4_1_1 = ttk.Label(self.top)
        self.TLabel4_1_1.place(relx=0.23, rely=0.327, height=27, width=30)
        self.TLabel4_1_1.configure(background="#d9d9d9")
        self.TLabel4_1_1.configure(foreground="#000000")
        self.TLabel4_1_1.configure(font="TkDefaultFont")
        self.TLabel4_1_1.configure(relief="flat")
        self.TLabel4_1_1.configure(anchor='w')
        self.TLabel4_1_1.configure(justify='left')
        self.TLabel4_1_1.configure(text='''X +''')
        self.TLabel4_1_1.configure(compound='left')

        self.Entry6 = ttk.Entry(self.top)
        self.Entry6.place(relx=0.292, rely=0.327, relheight=0.059
                , relwidth=0.112)
        self.Entry6.configure(takefocus="")
        self.Entry6.configure(cursor="ibeam")

        self.TLabel4_2_1 = ttk.Label(self.top)
        self.TLabel4_2_1.place(relx=0.415, rely=0.327, height=27, width=30)
        self.TLabel4_2_1.configure(background="#d9d9d9")
        self.TLabel4_2_1.configure(foreground="#000000")
        self.TLabel4_2_1.configure(font="TkDefaultFont")
        self.TLabel4_2_1.configure(relief="flat")
        self.TLabel4_2_1.configure(anchor='w')
        self.TLabel4_2_1.configure(justify='left')
        self.TLabel4_2_1.configure(text='''Y +''')
        self.TLabel4_2_1.configure(compound='left')

        self.Entry7 = ttk.Entry(self.top)
        self.Entry7.place(relx=0.476, rely=0.327, relheight=0.059
                , relwidth=0.112)
        self.Entry7.configure(takefocus="")
        self.Entry7.configure(cursor="ibeam")

        self.TLabel4_3_1 = ttk.Label(self.top)
        self.TLabel4_3_1.place(relx=0.599, rely=0.327, height=27, width=30)
        self.TLabel4_3_1.configure(background="#d9d9d9")
        self.TLabel4_3_1.configure(foreground="#000000")
        self.TLabel4_3_1.configure(font="TkDefaultFont")
        self.TLabel4_3_1.configure(relief="flat")
        self.TLabel4_3_1.configure(anchor='w')
        self.TLabel4_3_1.configure(justify='left')
        self.TLabel4_3_1.configure(text='''Z  =''')
        self.TLabel4_3_1.configure(compound='left')

        self.Entry8 = ttk.Entry(self.top)
        self.Entry8.place(relx=0.661, rely=0.327, relheight=0.057
                , relwidth=0.112)
        self.Entry8.configure(takefocus="")
        self.Entry8.configure(cursor="ibeam")

        self.Entry9 = ttk.Entry(self.top)
        self.Entry9.place(relx=0.092, rely=0.49, relheight=0.057, relwidth=0.112)

        self.Entry9.configure(takefocus="")
        self.Entry9.configure(cursor="ibeam")

        self.TLabel4_1_1_1 = ttk.Label(self.top)
        self.TLabel4_1_1_1.place(relx=0.23, rely=0.49, height=27, width=30)
        self.TLabel4_1_1_1.configure(background="#d9d9d9")
        self.TLabel4_1_1_1.configure(foreground="#000000")
        self.TLabel4_1_1_1.configure(font="TkDefaultFont")
        self.TLabel4_1_1_1.configure(relief="flat")
        self.TLabel4_1_1_1.configure(anchor='w')
        self.TLabel4_1_1_1.configure(justify='left')
        self.TLabel4_1_1_1.configure(text='''X +''')
        self.TLabel4_1_1_1.configure(compound='left')

        self.Entry10 = ttk.Entry(self.top)
        self.Entry10.place(relx=0.292, rely=0.49, relheight=0.057
                , relwidth=0.112)
        self.Entry10.configure(takefocus="")
        self.Entry10.configure(cursor="ibeam")

        self.TLabel4_2_1_1 = ttk.Label(self.top)
        self.TLabel4_2_1_1.place(relx=0.415, rely=0.49, height=27, width=30)
        self.TLabel4_2_1_1.configure(background="#d9d9d9")
        self.TLabel4_2_1_1.configure(foreground="#000000")
        self.TLabel4_2_1_1.configure(font="TkDefaultFont")
        self.TLabel4_2_1_1.configure(relief="flat")
        self.TLabel4_2_1_1.configure(anchor='w')
        self.TLabel4_2_1_1.configure(justify='left')
        self.TLabel4_2_1_1.configure(text='''Y +''')
        self.TLabel4_2_1_1.configure(compound='left')

        self.Entry11 = ttk.Entry(self.top)
        self.Entry11.place(relx=0.476, rely=0.49, relheight=0.059
                , relwidth=0.112)
        self.Entry11.configure(takefocus="")
        self.Entry11.configure(cursor="ibeam")

        self.TLabel4_3_1_1 = ttk.Label(self.top)
        self.TLabel4_3_1_1.place(relx=0.599, rely=0.49, height=27, width=30)
        self.TLabel4_3_1_1.configure(background="#d9d9d9")
        self.TLabel4_3_1_1.configure(foreground="#000000")
        self.TLabel4_3_1_1.configure(font="TkDefaultFont")
        self.TLabel4_3_1_1.configure(relief="flat")
        self.TLabel4_3_1_1.configure(anchor='w')
        self.TLabel4_3_1_1.configure(justify='left')
        self.TLabel4_3_1_1.configure(text='''Z  =''')
        self.TLabel4_3_1_1.configure(compound='left')

        self.Entry12 = ttk.Entry(self.top)
        self.Entry12.place(relx=0.661, rely=0.49, relheight=0.057
                , relwidth=0.112)
        self.Entry12.configure(takefocus="")
        self.Entry12.configure(cursor="ibeam")

        self.TLabel4_1_1_1_1 = ttk.Label(self.top)
        self.TLabel4_1_1_1_1.place(relx=0.23, rely=0.755, height=27, width=30)
        self.TLabel4_1_1_1_1.configure(background="#d9d9d9")
        self.TLabel4_1_1_1_1.configure(foreground="#000000")
        self.TLabel4_1_1_1_1.configure(font="TkDefaultFont")
        self.TLabel4_1_1_1_1.configure(relief="flat")
        self.TLabel4_1_1_1_1.configure(anchor='w')
        self.TLabel4_1_1_1_1.configure(justify='left')
        self.TLabel4_1_1_1_1.configure(text='''X =''')
        self.TLabel4_1_1_1_1.configure(compound='left')

        self.TLabel4_2_1_1_1 = ttk.Label(self.top)
        self.TLabel4_2_1_1_1.place(relx=0.415, rely=0.755, height=27, width=30)
        self.TLabel4_2_1_1_1.configure(background="#d9d9d9")
        self.TLabel4_2_1_1_1.configure(foreground="#000000")
        self.TLabel4_2_1_1_1.configure(font="TkDefaultFont")
        self.TLabel4_2_1_1_1.configure(relief="flat")
        self.TLabel4_2_1_1_1.configure(anchor='w')
        self.TLabel4_2_1_1_1.configure(justify='left')
        self.TLabel4_2_1_1_1.configure(text='''Y =''')
        self.TLabel4_2_1_1_1.configure(compound='left')

        self.TLabel4_3_1_1_1 = ttk.Label(self.top)
        self.TLabel4_3_1_1_1.place(relx=0.599, rely=0.755, height=27, width=30)
        self.TLabel4_3_1_1_1.configure(background="#d9d9d9")
        self.TLabel4_3_1_1_1.configure(foreground="#000000")
        self.TLabel4_3_1_1_1.configure(font="TkDefaultFont")
        self.TLabel4_3_1_1_1.configure(relief="flat")
        self.TLabel4_3_1_1_1.configure(anchor='w')
        self.TLabel4_3_1_1_1.configure(justify='left')
        self.TLabel4_3_1_1_1.configure(text='''Z  =''')
        self.TLabel4_3_1_1_1.configure(compound='left')

        self.Entry15 = ttk.Entry(self.top)
        self.Entry15.place(relx=0.661, rely=0.755, relheight=0.059
                , relwidth=0.114)
        self.Entry15.configure(takefocus="")
        self.Entry15.configure(cursor="ibeam")

        self.Entry14 = ttk.Entry(self.top)
        self.Entry14.place(relx=0.476, rely=0.755, relheight=0.059
                , relwidth=0.114)
        self.Entry14.configure(takefocus="")
        self.Entry14.configure(cursor="ibeam")

        self.Entry13 = ttk.Entry(self.top)
        self.Entry13.place(relx=0.292, rely=0.755, relheight=0.059
                , relwidth=0.114)
        self.Entry13.configure(takefocus="")
        self.Entry13.configure(cursor="fleur")

        self.TLabel4 = ttk.Label(self.top)
        self.TLabel4.place(relx=0.092, rely=0.755, height=27, width=48)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Results''')
        self.TLabel4.configure(compound='left')

        self.TLabel5 = ttk.Label(self.top)
        self.TLabel5.place(relx=0.86, rely=0.918, height=19, width=35)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="TkDefaultFont")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='w')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''ZMB''')
        self.TLabel5.configure(compound='left')

def start_up():
    My_Linear_Solver_System_support.main()

if __name__ == '__main__':
    My_Linear_Solver_System_support.main()




