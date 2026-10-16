########################################################
# HACKATHON 2026 - Virginia Western Community College
# CTRL-ALT-ELITE Edition
# VWCC CAE Phishing Detector v1.0
# (c) Noah W, Noah T, Arkadiy, Lashman, 16 October 2026
########################################################

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
    securityLabel = ttk.Label(frm2, text="")
    securityLabel.grid(column=0, row=2, columnspan=2, pady=5)
    reasoningLabel = ttk.Label(frm2, text="")
    reasoningLabel.grid(column=0, row=4, columnspan=2, pady=5)
    # suspicionLabel = ttk.Label(frm2, text="")
    # suspicionLabel.grid(column=0, row=3, columnspan=2, pady=5)

    def back_to_frm():
        #back to normal window size
        statusLabel.config(text="")
        resultLabel.config(text="")
        securityLabel.config(text="")
        reasoningLabel.config(text="")
        frm2.grid_forget()  # Hide the second frame
        frm.grid()  # Show the first frame
        url.set("") # Clear the URL entry field for the next input
        root.bind("<Return>", lambda event: phishing_detector(url.get()))

    
    firstLine = ttk.Label(frm, text="Welcome to the Phishing Detector!",font=(16))
    firstLine.grid(column=0, row=0, columnspan=2, pady=(0,10))

    secondLine = ttk.Label(frm, text="Virginia Western Community College 2026")
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
        # important for the information section
        specialCharactersInformer = 0
        numbersInformer = 0  
        lettersInformer = 1
        keywordsInformer = 0
        
        urlLength, specialCharactersCount, digitsCount, lettersCount, is_dangerous = typesOfCharactersInUrl(url)
        if ".xyz" in url or ".click" in url or ".biz" in url or ".scam" in url:
            phishing_confidence += 90  # 90% likely a scam based on keywords
            keywordsInformer = 1
        if "secure" in url or "update" in url or "verify" in url:
            phishing_confidence += 25  # 25% likely a scam based on keywords
            keywordsInformer = 2
        if "free" in url or "offer" in url or "click" in url:
            phishing_confidence += 35  # 35% likely a scam based on keywords
            keywordsInformer = 3
        if "bank" in url or "paypal" in url or "amazon" in url:
            phishing_confidence += 20  # 20% likely a scam based on keywords
            keywordsInformer = 4
        if "login" in url:
            phishing_confidence += 15  # 15% likely a scam based on keywords
            keywordsInformer = 5
        else:
            phishing_confidence = 1  # 99% likely safe based on keywords

        # Adds onto phishing confidence the lower the percentage of letters is in the URL
        lettersPercent = lettersCount / urlLength
        if (lettersPercent < 0.3):
            phishing_confidence += 50
        elif (lettersPercent < 0.5):
            phishing_confidence += 35
        elif (lettersPercent < 0.7):
            phishing_confidence += 15
        elif (lettersPercent < 0.8):
            phishing_confidence += 10

        if (lettersPercent < 0.8):
            lettersInformer = lettersPercent

        # Adds onto phishing confidence the higher the percentage of special characters is in the URL
        specialCharactersPercent = specialCharactersCount / urlLength
        if (specialCharactersPercent > .50):
            phishing_confidence += 99
        elif (specialCharactersPercent > .30):
            phishing_confidence += 50
        elif (specialCharactersPercent > .20):
            phishing_confidence += 25
        elif (specialCharactersPercent > .15):
            phishing_confidence += 15

        if (specialCharactersPercent > .15):
            specialCharactersInformer = specialCharactersPercent

        # Adds onto phishing confidence the higher the percentage of numbers is in the URL
        numbersPercent = digitsCount / urlLength
        if (numbersPercent > .30):
            phishing_confidence += 50
        elif (numbersPercent > .15):
            phishing_confidence += 30
        elif (numbersPercent > .10):
            phishing_confidence += 15
        elif (numbersPercent > .05):
            phishing_confidence += 10

        if (numbersPercent > .05):
            numbersInformer = numbersPercent


        # If the confidence is over 99 sets it to 99
        if (phishing_confidence > 99):
            phishing_confidence = 99

        # If the confidence is over 50 label it as phishing
        if (phishing_confidence > 50):
            is_phishing = True
        else:
            is_phishing = False

        phishing_announcer(is_phishing, phishing_confidence, is_dangerous, lettersInformer, specialCharactersInformer, numbersInformer, keywordsInformer)

    # Checks the length of and how many digits, special characters and letters there are in the URL
    def typesOfCharactersInUrl(url):
        specialCharactersCount = 0
        digitsCount = 0
        is_dangerous = False

        # If the url starts with http:// it should be flagged as not secure
        if "http://" in url:
            is_dangerous = True


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


        return (urlLength,specialCharactersCount,digitsCount,lettersCount, is_dangerous)

            

    # Will show the user the results of the phishing detection.
    def phishing_announcer(is_phishing, phishing_confidence, is_dangerous, lettersInformer, specialCharactersInformer, numbersInformer, keywordsInformer):
        frm.grid_forget()  # Hide the first frame
        frm2.grid()  # Show the second frame
        root.bind("<Return>", lambda event: back_to_frm())
        reasoning = ""
        
        if is_phishing:
            statusLabel.config(text="WARNING!!", foreground="dark red",font=(16))
            statusLabel.config(padding=(20,20)) #Add Padding
            #statusLabel.grid(column=0, row=0, columnspan=2, pady=5)
            resultLabel.config(text=f"{url.get()[:50]} is likely phishing with confidence: {phishing_confidence}%") #format string to show the confidence score
            resultLabel.config(font=(14)) #Change Font Size
            #print("This URL is likely phishing with confidence:", str(phishing_confidence) + "%")
            #resultLabel.grid(column=0, row=1, columnspan=2, pady=10)        
        else:
            statusLabel.config(text="SAFE", foreground="dark green",font=(16))
            statusLabel.config(padding=(20,20)) #Add Padding
            #statusLabel.grid(column=0, row=0, columnspan=2, pady=5)
            resultLabel.config(text=f"{url.get()[:50]} is likely safe with confidence: {100 - phishing_confidence}%") #format string to show the confidence score
            resultLabel.config(font=(14)) #Change Font Size
            #print("This URL is likely safe with confidence:", str(phishing_confidence) + "%")
            resultLabel.grid(column=0, row=1, columnspan=2, pady=10)

        
        if is_dangerous:
            securityLabel.config(text="WARNING!! This URL is not secure it contains http://! Be careful!", foreground="orange")
            securityLabel.config(font=(14),padding=(20,20))

        if lettersInformer < 0.8:
            reasoning += f"WARNING!! {lettersInformer*100:.2f}% of this URL is made up of letters! Use caution!\n"
        if specialCharactersInformer > 0.15:
            reasoning += f"WARNING!! {specialCharactersInformer*100:.2f}% of this URL is made up of special characters! Use caution!\n"
        if numbersInformer > 0.05:
            reasoning += f"WARNING!! {numbersInformer*100:.2f}% of this URL is made up of numbers! Use caution!\n"
        if keywordsInformer == 1:
            reasoning += "WARNING!! This URL contains keywords that are commonly used in phishing attacks, which includes: .xyz, .click, .biz, .scam \n"
        if keywordsInformer == 2:
            reasoning += "WARNING!! This URL contains keywords that are commonly used in phishing attacks, which includes: secure, update, verify \n"
        if keywordsInformer == 3:
            reasoning += "WARNING!! This URL contains keywords that are commonly used in phishing attacks, which includes: free, offer, click \n"
        if keywordsInformer == 4:
            reasoning += "WARNING!! This URL contains keywords that are commonly used in phishing attacks, which includes: bank, paypal, amazon \n"
        if keywordsInformer == 5:
            reasoning += "WARNING!! This URL contains a keyword that is commonly used in phishing attacks, which includes: login \n"
        
        # if reasoning != "":
        #     suspicionLabel.config(text="These are the reasons for suspicion:", foreground="dark orange", font=(14))

        reasoningLabel.config(text=reasoning, foreground="dark orange")
        reasoningLabel.config(font=(14),padding=(20,20))

    root.mainloop()

if __name__ == "__main__":
    main()