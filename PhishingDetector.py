from tkinter import *
from tkinter import ttk


def main():
    root = Tk()

    # Create the application variable and give it an initial value.
    url = StringVar(value="")
    
    root.title("VWCC CAE Phishing Analyzer v1.0")
    frm = ttk.Frame(root, padding=50)
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
    entry = ttk.Entry(frm, textvariable=url, placeholder="Enter URL here")
    entry.grid(column=1, row=3, pady=(0,30))
    
    # Print the current value whenever the user presses Return.
    def print_contents(event):
        print("The current URL is:", url.get())
    # Using lambda allows entry.bind to call multiple functions, I believe (it works correctly).
    entry.bind("<Return>", lambda event: (print_contents(event), phishing_detector(url.get())))
    quitButton = ttk.Button(frm, text="Quit", command=root.destroy)
    quitButton.grid(column=1, row=100, sticky="e")

    # Placeholder for the actual phishing detection logic.
    def phishing_detector(url):
        is_phishing = False  # Replace with actual detection logic
        phishing_confidence = 100  # Replace with actual confidence score
        phishing_announcer(is_phishing, phishing_confidence)

    # Will show the user the results of the phishing detection.
    def phishing_announcer(is_phishing, phishing_confidence):
        if is_phishing:
            print("This URL is likely phishing with confidence:", str(phishing_confidence) + "%")
        else:
            print("This URL is likely safe with confidence:", str(phishing_confidence) + "%")

    


    root.mainloop()

if __name__ == "__main__":
    main()