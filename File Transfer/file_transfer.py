import shutil
import os
import time
from tkinter import *
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master = master
        self.master.title("File Transfer")

        self.lbl_src = Label(self.master, text='Source Directory:')
        self.lbl_src.grid(row=0,column=1, padx=(0,10),pady=(10,2), sticky=W)
        self.lbl_dest = Label(self.master, text='Destination Directory:')
        self.lbl_dest.grid(row=2,column=1, padx=(0,10),pady=(10,2), sticky=W)

        self.btn_browsesrc = Button(self.master, text='Browse...', command=lambda: browseSrcDir(self))
        self.btn_browsesrc.grid(row=1,column=0, padx=10,pady=(0,10))
        self.btn_browsedest = Button(self.master, text='Browse...', command=lambda: browseDestDir(self))
        self.btn_browsedest.grid(row=3,column=0, padx=10,pady=(0,10))
        self.btn_filecheck = Button(self.master, text='Move Files', command=lambda: moveFiles(self))
        self.btn_filecheck.grid(row=4,column=1, padx=10,pady=(0,10), sticky=E)

        self.txtbox_src = Entry(self.master, text='',width=50)
        self.txtbox_src.grid(row=1,column=1, padx=(0,10),pady=(0,10))
        self.txtbox_dest = Entry(self.master, text='',width=50)
        self.txtbox_dest.grid(row=3,column=1, padx=(0,10),pady=(0,10))

        # Prompts the user to select a directory that will be inserted into the text box
        # adding a foward slash at the end so that the moveFiles function joins the path and the file properly
        def browseSrcDir(self):
            source = tk.filedialog.askdirectory() + '/'
            self.txtbox_src.delete(0,END)
            self.txtbox_src.insert(0,source)
        
        def browseDestDir(self):
            destination = tk.filedialog.askdirectory() + '/'
            self.txtbox_dest.delete(0,END)
            self.txtbox_dest.insert(0,destination)

        # Checks if a file has been modified in the last 24 hours by getting both modified time and local time
        # in seconds, subtracting 86400 seconds (24 hours) from local time, and making a comparison
        def moveFiles(self):                     
            source = self.txtbox_src.get()
            destination = self.txtbox_dest.get()
            confirm = tk.messagebox.askokcancel("Confirmation", 'Files modified in the last 24 hours from\n"{}"\nwill be copied to\n"{}"\nProceed?'.format(source,destination))
            if confirm:
                try:
                    files = os.listdir(source)
                    for i in files:
                        filepath = os.path.join(source,i)
                        filemtime = os.path.getmtime(filepath)
                        localtime = time.time()
                        if filemtime > localtime - 86400:
                            try:
                                shutil.copy(source+i, destination)
                            except:
                                tk.messagebox.showerror('Destination Directory Not Found!','Your destination directory, {}, does not exist!'.format(destination))
                    tk.messagebox.showinfo('Done!','Files were moved successfully from\n "{}"\n to\n "{}"'.format(source,destination))
                except FileNotFoundError:
                    tk.messagebox.showerror('Source Directory Not Found!',"Your source directory, {}, does not exist!".format(source))

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
    

    
