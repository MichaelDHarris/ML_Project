'''
To install textblob, run the command "pip install -U textblob"
Tkinter is built into installations of Python.
To install openpyxl, run the command "pip install openpyxl"
The format for input tweets can be found in the test.txt file provided.
The content of a single tweet is ordered as such:

Author
Date
Tweet
'''
from textblob import * #nlp toolkit
from tkinter import * #filedialog window
from tkinter import filedialog
from openpyxl import Workbook #excel workbook export
from openpyxl.styles import Font

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
    print(filename)
    with open(filename, 'r') as f:
        text = "".join(line for line in f) #getting text document to readable format
    wb = Workbook()
    ws = wb.active
    Data = [["Author", "Date", "Polarity", "Subjectivity", "Tweet"]] #category names of the spreadsheet
    line_list = text.splitlines()
    tweet_list = []
    if len(line_list) % 3 != 0: #line_list lines should be divisible by 3 to follow format
        raise Exception("Line_list lines are not divisible by 3. Each tweet is grouped into 3 lines.")
    for i in range(len(line_list)//3):
        tweet_list.append([line_list.pop(0),line_list.pop(0),line_list.pop(0)])
    print(tweet_list)
    i = 1 #count each entry
    for tweet in tweet_list:
        blob = TextBlob(tweet[2])
        Data.append([tweet[0],tweet[1],blob.polarity, blob.subjectivity, tweet[2]]) #go sentence by sentence and append relevant information to spreadsheet
        print(f"\nTweet {i}: \n")
        i += 1
        for item in tweet:
            print(item)
        print(blob.sentiment)
    for row in Data: #
        ws.append(row)
    ft = Font(bold=True)
    for row in ws["A1:E1"]: #bold headers
        for cell in row:
            cell.font = ft
    print('─' * 30)
    print('Saving to Excel Workbook')
    name = str(input('Please enter what you would like you workbook to be named (do not add the extension, I will do that for you.): '))+ '.xlsx'
    wb.save(name)
    print('You can find the workbook in the same folder that this program is in once this program exits! Now exiting program...')
    window.destroy() #workbook doesn't show up until program exits, so we force exit the window to end the program
#create the root window
window = Tk()
#set window title
window.title('File Explorer')
#set window size
window.geometry("350x200")
#set window background color
window.config(background="white")
#create a File Explorer label
label_file_explorer = Label(window,
                            text="Machine Learning Project",
                            width=50, height=4,
                            fg="blue")
button_explore = Button(window,
                        text="Browse Files",
                        command=browseFiles)
button_exit = Button(window,
                     text="Exit",
                     command=exit)
#grid method is chosen for placing
#the widgets at respective positions
#in a table like structure by
#specifying rows and columns
label_file_explorer.grid(column=0, row=1)
button_explore.grid(column=0, row=2)
button_exit.grid(column=0, row=3)
#let the window wait for any events
window.mainloop()


