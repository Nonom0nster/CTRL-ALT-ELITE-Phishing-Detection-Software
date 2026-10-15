##################################################
#
#
#
# HEADER AND COMMENT BLOCK maybe with credits and sources too?
#
#
#
##################################################

from tkinter import *
from tkinter import ttk


def main():
    root = Tk()

    # Create the application variable and give it an initial value.
    url = StringVar(value="")
    
    root.title("VWCC CAE Phishing Analyzer v1.0")
    frm = ttk.Frame(root, padding=50) #Window page 1
    frm.grid()

    frm2 = ttk.Frame(root, padding=50) #Window page 2
    statusLabel = ttk.Label(frm2, text="")
    statusLabel.grid(column=0, row=0, columnspan=2, pady=5)
    resultLabel = ttk.Label(frm2, text="")
    resultLabel.grid(column=0, row=1, columnspan=2, pady=10)  

    def back_to_frm():
        frm2.grid_forget()  # Hide the second frame
        frm.grid()  # Show the first frame
        url.set("") # Clear the URL entry field for the next input
        root.bind("<Return>", lambda event: phishing_detector(url.get()))

    
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
    
    
    # Using lambda allows entry.bind to call multiple functions, I believe (it works correctly).
    root.bind("<Return>", lambda event: phishing_detector(url.get()))
    quitButton = ttk.Button(frm, text="Quit", command=root.destroy)
    quitButton.grid(column=0, row=100, sticky="w")
    scanButton = ttk.Button(frm, text="Scan URL", command=lambda: phishing_detector(url.get()))
    scanButton.grid(column=1, row=100, sticky="e")

    quitButton = ttk.Button(frm2, text="Quit", command=root.destroy)
    quitButton.grid(column=0, row=100, sticky="w")
    backButton = ttk.Button(frm2, text="Check Another URL", command=back_to_frm)
    backButton.grid(column=1, row=100, sticky="e")




    # Placeholder for the actual phishing detection logic.
    def phishing_detector(url):
        # If the url is empty or the default placeholder text, show a warning message and return
        if url == "" or url == "Enter URL here":
            statusLabel.config(text="Please enter a URL to scan.", foreground="orange")
            resultLabel.config(text="")
            return
        is_phishing = False  # Replace with actual detection logic
        phishing_confidence = 0  # Replace with actual confidence score
        urlLength, specialCharactersCount, digitsCount, lettersCount = typesOfCharactersInUrl(url)
        if ".xyz" in url or ".click" in url or ".biz" in url or ".scam" in url:
            phishing_confidence = 90  # 90% likely a scam based on keywords
        elif "login" in url or "secure" in url or "update" in url or "verify" in url:
            phishing_confidence = 85  # 85% likely a scam based on keywords
        elif "free" in url or "offer" in url or "click" in url:
            phishing_confidence = 75  # 75% likely a scam based on keywords
        elif "bank" in url or "paypal" in url or "amazon" in url:
            phishing_confidence = 65  # 65% likely a scam based on keywords
        else:
            phishing_confidence = 1  # 99% likely safe based on keywords

        # Adds onto phishing confidence the lower the percentage of letters is in the URL
        lettersPercent = lettersCount / urlLength
        if (lettersPercent < 0.8):
            phishing_confidence += 10
        elif (lettersPercent < 0.7):
            phishing_confidence += 20
        elif (lettersPercent < 0.5):
            phishing_confidence += 50
        elif (lettersPercent < 0.3):
            phishing_confidence += 99

        # Adds onto phishing confidence the higher the percentage of special characters is in the URL
        specialCharactersPercent = specialCharactersCount / urlLength
        if (specialCharactersPercent > .15):
            phishing_confidence += 10
        elif (specialCharactersPercent > .20):
            phishing_confidence += 20
        elif (specialCharactersPercent > .30):
            phishing_confidence +=50
        elif (specialCharactersPercent > .50):
            phishing_confidence += 99

        # Adds onto phishing confidence the higher the percentage of numbers is in the URL
        numbersPercent = digitsCount / urlLength
        if (numbersPercent > .5):
            phishing_confidence += 10
        elif (numbersPercent > .10):
            phishing_confidence += 20
        elif (numbersPercent > .15):
            phishing_confidence +=50
        elif (numbersPercent > .30):
            phishing_confidence += 99


        # If the confidence is over 99 sets it to 99
        if (phishing_confidence > 99):
            phishing_confidence = 99

        # If the confidence is over 50 label it as phishing
        if (phishing_confidence > 50):
            is_phishing = True
        else:
            is_phishing = False
        phishing_announcer(is_phishing, phishing_confidence)

    # Checks the length of and how many digits, special characters and letters there are in the URL
    def typesOfCharactersInUrl(url):
        specialCharactersCount = 0
        digitsCount = 0
        # Removes https:// or http:// from the string before checking special characters
        if "https://" in url or "http://" in url:
            url = url.split("//", 1)[1]

        # Gets lenght of URL
        urlLength = len(url)

        # Checks if each character is a special character or digit
        for characters in url:
            if (not characters.isalnum()):
                specialCharactersCount += 1
            if (characters.isdigit()):
                digitsCount += 1

        lettersCount = urlLength - (digitsCount + specialCharactersCount)

        return (urlLength,specialCharactersCount,digitsCount,lettersCount) 



            

    # Will show the user the results of the phishing detection.
    def phishing_announcer(is_phishing, phishing_confidence):
        frm.grid_forget()  # Hide the first frame
        frm2.grid()  # Show the second frame
        root.bind("<Return>", lambda event: back_to_frm())
        
        if is_phishing:
            statusLabel.config(text="WARNING!!", foreground="dark red")
            #statusLabel.grid(column=0, row=0, columnspan=2, pady=5)
            resultLabel.config(text=f"{url.get()[:50]} is likely phishing with confidence: {phishing_confidence}%") #format string to show the confidence score
            #print("This URL is likely phishing with confidence:", str(phishing_confidence) + "%")
            #resultLabel.grid(column=0, row=1, columnspan=2, pady=10)        
        else:
            statusLabel.config(text="SAFE", foreground="dark green")
            #statusLabel.grid(column=0, row=0, columnspan=2, pady=5)
            resultLabel.config(text=f"{url.get()[:50]} is likely safe with confidence: {100 - phishing_confidence}%") #format string to show the confidence score
            #print("This URL is likely safe with confidence:", str(phishing_confidence) + "%")
            resultLabel.grid(column=0, row=1, columnspan=2, pady=10)


    


    root.mainloop()

if __name__ == "__main__":
    main()