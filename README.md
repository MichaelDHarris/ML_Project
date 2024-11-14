# ML_Project
Political Personality Sentiment Analysis

# Libraries
To install textblob, run the command "pip install -U textblob"

Tkinter is built into installations of Python.

To install openpyxl, run the command "pip install openpyxl"

# Format for Testing
Tweets are to be put into a .txt file

The format for input tweets can be found in the test.txt file provided.

The content of a single tweet is ordered as such:

Author 1

Date 1

Tweet 1

Author 2

Date 2

Tweet 2

It is best practice in this application to order tests based on author, for example, all Donald Trump Tweets followed by all Kamala Harris tweets.

# Intended Behavior

Upon running, the program should open a file dialog window. Upon selecting your file and clicking open,

the file will be tested to see if the amount of newlines are divisible by 3 for formatting purposes.

After, the file will be sorted into a nested list, with each sublist grouping the information of an individual tweet.

Then, a Blob object is created from the tweet content and the polarity and subjectivity are found.

After, the program will attempt to append the data to an Excel worksheet.

The terminal will ask the user what they wish to name their worksheet. The worksheet will not save if the user does not name it.
