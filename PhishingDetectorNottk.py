from tkinter import *

def main():
    def scan():
        URL = GetURL.get()
        print(URL + " is a phishing site!")
        window.destroy()

    window = Tk()

    window.title("VWCC CAE Phishing Analyzer v1.0")

    label1 = Label(window, text="Welcome to the Phishing Detector!")
    label1.config(font=("Times New Roman", 16))
    label1.pack()

    label2 = Label(window, text="This is Awesome!")
    label2.config(font=("Times New Roman", 16))
    label2.pack()

    label3 = Label(window, text="CTRL-ALT-ELITE Edition")
    label3.config(font=("Times New Roman", 16))
    label3.pack()

    QuitButton = Button(window, text="Quit", command=window.destroy)
    QuitButton.config(font=("Times New Roman", 16))

    GetURL = Entry()
    GetURL.config(font=("Times New Roman", 16))

    ScanButton = Button(window, text = "SCAN", command = scan)
    ScanButton.config(font=("Times New Roman", 16))

    GetURL.pack()
    QuitButton.pack(side=RIGHT)
    ScanButton.pack(side=RIGHT)

    window.mainloop()

main()