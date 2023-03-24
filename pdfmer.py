from tkinter import *
from tkinter import messagebox
from PyPDF2 import PdfWriter
import tkinter.font as tkFont
import os

win=Tk()
win.title("Pdfmerger")
win.geometry('629x500')
win.iconbitmap('pdffavicon.ico')
win.configure(bg='#a2c892')
fnt=tkFont.Font(size=28)


def merge():
    if(pdf1.get()!='' and pdf2.get()!=''):
        lis=list()
        lis.append(pdf1.get())
        lis.append(pdf2.get())

        merger = PdfWriter()
        
        ot=output.get()
        z=ot+".pdf"
        
        for fil in lis:
            merger.append(fil)

        if(ot!=''):
            merger.write(z)
        else:
            merger.write("merged.pdf")
        merger.close()
        messagebox.showinfo("Merged!!","please check the same location as this python file.")
    else:
        messagebox.showinfo("Empty directory","please enter both the locations of the pdf.")



def openit():
    mer="mergedpdf.pdf"
    if(mer in os.listdir()):
        open("mergedpdf.pdf","rb")
    else:
        messagebox.showinfo("No pdf","Please merge pdf first")




name1=Label(win,text="Address of file 1",bg='#74a273')
name1.grid(row=1,column=0,padx=10,pady=10)
pdf1=Entry(win,width=50,bg='#5e9b6f')
pdf1.grid(row=1,column=1,padx=10,pady=10)

name2=Label(win,text="Address of file 2",bg='#74a273')
name2.grid(row=2,column=0,padx=10,pady=10)
pdf2=Entry(win,width=50,bg='#5e9b6f')
pdf2.grid(row=2,column=1,padx=10,pady=10)


output_label=Label(win,text="Name of the outputfile:",bg='#74a273')
output_label.grid(row=3,column=0,padx=10,pady=10)
output=Entry(win,width=50,bg='#5e9b6f')
output.grid(row=3,column=1,padx=10,pady=10)





mergebtn=Button(win,text="Merge",command=merge,bg='#86b985')
mergebtn.grid(row=4,column=0,padx=10,pady=10)

openbtn=Button(win,text="Open merged pdf",command=openit,bg='#86b985')
openbtn.grid(row=4,column=1,padx=10,pady=10)

lb=Label(win,text="If you want to merge new pdf's please rename the existing 'mergedpdf.pdf' into something else",wraplength=500,font=fnt,bg='#587f5a',fg='#5e9b6f')
lb.grid(row=5,column=1,padx=10)





win.mainloop()