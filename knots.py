# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
import re

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.dowker = tk.Entry()
        

        # default Dowker encoding is the trefoil [4, 6, 2]
        self.dft = tk.StringVar()
        self.dft.set("[4, 6, 2]")
        self.dowker["textvariable"] = self.dft
        self.dowker.pack()
        
        # to submit Dowker encoding for parsing and . Drawing.
        self.smt = tk.Button(text="Submit", command=self.parseDowker)
        self.smt.pack()
        # Define a binding for when the user hits return because I'm
        # stupid and hit the return key instead of hitting buttons
        
        self.dowker.bind('<Key-Return>', self.parseDowker)
        
        

    def parseDowker(self, event=None):
        """ 
        Splits the input into a list of integers a la typical
        Dowker encoding notation
        """
        enc = list(int(a.split()[0]) for a in 
                   re.split(",|\[|\]",self.dowker.get()) if a!="")
        
        # Dowker encodings only have unique crossing labels
        if list(dict.fromkeys(enc)) != list(abs(e) for e in enc):
            raise Exception("Must not have duplicate values in Dowker code")
        mx = len(enc)
        for e in enc:
            en = abs(e)
        # Ensure only even integers used [odd integers implied in Dowker codes]
            if en%2:
                raise Exception("Dowker codes are comprised of even integers")
            if en < 1 or en > mx*2:
                raise Exception("Encoding values out of range of " +
                                "number of crossings in knot")
        
        print(enc)
        

root = tk.Tk()
root.geometry("400x400")
root.minsize(400, 400)
root.maxsize(400, 400)
 
myapp = App(root)
myapp.mainloop()