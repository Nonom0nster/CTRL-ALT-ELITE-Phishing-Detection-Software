from tkinter import *
from tkinter import ttk


def main():
    root = Tk()
    frm = ttk.Frame(root, padding=100)
    frm.grid()
    ttk.Label(frm, text="Welcome to the Phishing Detector!").grid(column=0, row=0, pady=(0, 10))
    ttk.Label(frm, text="This is Awesome!").grid(column=0, row=1, pady=(0, 10))
    ttk.Label(frm, text="CTRL-ALT-ELITE Edition").grid(column=0, row=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3, pady=(30, 30))
    ttk.Button(frm, text="Quit Again", command=root.destroy).grid(column=1, row=3)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()