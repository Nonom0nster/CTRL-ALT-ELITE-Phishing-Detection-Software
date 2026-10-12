from tkinter import *
from tkinter import ttk


def main():
    root = Tk()

    # Create the application variable and give it an initial value.
    url = StringVar(value="URL goes here")
    
    root.title("VWCC CAE Phishing Analyzer v1.0")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    
    firstLine = ttk.Label(frm, text="Welcome to the Phishing Detector!")
    firstLine.grid(column=0, row=0, columnspan=2, pady=(0,10))

    secondLine = ttk.Label(frm, text="This is Awesome!")
    secondLine.grid(column=0, row=1, columnspan=2, pady=(0,10))

    thirdLine = ttk.Label(frm, text="CTRL-ALT-ELITE Edition")
    thirdLine.grid(column=0, row=2, columnspan=2, pady=(0,10))

    fourthLine = ttk.Label(frm, text="Enter URL to test: ")
    fourthLine.grid(column=0, row=3, pady=(0,30))
    
    # Tell the entry widget to track the variable.
    entry = ttk.Entry(frm, textvariable=url)
    entry.grid(column=1, row=3, pady=(0,30))
    
    # Print the current value whenever the user presses Return.
    def print_contents(event):
        print("The current URL is:", url.get())
    entry.bind("<Return>", print_contents)
    quitButton = ttk.Button(frm, text="Quit", command=root.destroy)
    quitButton.grid(column=1, row=100, sticky="e")
    

    
    root.mainloop()

if __name__ == "__main__":
    main()