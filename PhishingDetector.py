from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Welcome to the Phishing Detector!").grid(column=0, row=0)
    ttk.Label(frm, text="This is Awesome!").grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=2)
    root.mainloop()
    
if __name__ == "__main__":
    main()