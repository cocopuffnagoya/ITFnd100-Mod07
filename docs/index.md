Name: Coco Jones<br>
Date: February 26, 2023<br>
Class: ITFDN110A<br>
Module: 07<br>
GitHub: https://github.com/cocopuffnagoya/ITFnd100-Mod07<br>

# **Pickling and Try-Except in Python**

## **Introduction**
In module 07, I researched how to handle errors using Try-Except and class and how to pickle data in Python. To complete this assignment, I watched a couple of YouTubes and read some articles on the web. I have pasted the URLs of the resources at the References section and written why I selected those resources for my assignment there. I decided to combine the two requirements (pickling and try-except) into one script. 

## **What are the benefits of putting built-in Python command into functions?**
Below is an example in which I put multiple Python commands into my open_file() function. This function has 8 commands. Once a function is defined, you can use this as many times as you want throughout the script. The 8 commands are in one block and this one function can be called multiple times later in the script. Benefits of putting built-in commands to functions are organizing our script and improving readability and reusability. (Fig 1)

```
def open_file():    # Create a open_file function to read binary file
    with open('studentData.pkl','rb') as readFile:
        a = pickle.load(readFile)   # Load first line and put the data into a
        b = pickle.load(readFile)   # Load second line and put the data into b
        c = pickle.load(readFile)   # Load third line and put the data into a
        print("The file shows:")
        print("Number of your Students: "+str(a))   # Show loaded data
        print("Your Students and Grades:")
        for i in range(0,numStudents):  # Show loaded data
            print(b[i],c[i],sep=' = ')  # Show loaded data
```
**Fig 1 - Multiple commands into one Function**

## **What are the benefits of using structured error handling?** ##
There are multiple benefits of structured error handling. One benefit is that you can use your custom error message instead of showing python built-in error message. Python’s built-in error messages are not easy to understand for end users. Also, python’s error message stops the whole program and does not allow the user to correct the mistake that she/he made. By using structured error handling, the user will know when there is an error, how he can correct and proceed. Fig 2 below shows an Try-Except Error handling example in my script. Fig 3 shows what happens if the error handling is not used.
 
**Fig 2 - Try-Except error handling example**
 
**Fig 3 - If no error handling is used, python error message is displayed and the program stops**

## **What are the differences between a text file and a binary file?**
One of the differences between a text file and a binary file is that a binary file is not for humans to read. The data on a binary file is obscure. Below is a binary file example that was created by the assignment script. A text file is readable and understandable to humans. Another difference is that a text file uses the .txt extension. But binary files can have .pkl or .pickle or .bat extensions. You can make up an extension for your binary file. In my assignment script, I gave the .pkl extension to my binary file. (Fig 4)
 
	**Fig 4 – What is in a binary file and a binary file can have an .pkl extension**

## **How is the Exception class used?**
The exception class is used to handle errors in Python. In Fig 2 above, I showed the Try-Except block that is designed to catch an error. In the example, the user is expected to enter an integer to the program. If a non-integer value is entered, the Exception message “That is not a valid number. Try again!” is shown.
 
## **How do you “derive” a new class from the Exception class?**
You can derive a new class by typing class, your desired class name and (Exception). In my assignment script, I derived a new class from the Exception class. See Fig 5. I created a new class called InvalidGrade to raise an exception when the value the user inputs is smaller than 0 or larger than 100. 
 
**Fig 5 – Deriving a new class from Exception**
## When might you create a class derived from the Exception class?
When you cannot use any of the built-in exceptions in Python to handle an expected error, you can create a custom exception. In my script, I created a custom Exception to handle an error. My program asks the user to enter students’ names and grades. Grades are between 0 and 100. No negative values or values over 100 are invalid values. In my script, I created a class InvalidGrade(Exception) to raise an Exception when a value over 100 or below 0 are entered and have the user enter the. In the example below, the user enters 120 for Jim’s grade, the custom exception catches it and tells the user to enter the value between 0 and 100. (Fig 6)
 
**Fig 6 – Create a custom Exception to catch an unwanted value.**

## **What is the Markdown language?**
The Markdown language is used to format technical documents in plain text and is used on collaborative platforms like GitHub. This language is used to publish a copy of my Module 07 Assignment. The language is easily converted to HTML or PDF. That is one of the benefits of the Markdown language.  
To make a header, you use #. To make your font bolder, you wrap the words with **. And to post your coding in a coding block, you wrap your coding with ```. <br> is used as carriage return. (Fig 7)
  
**Fig 7 – Markdown language to publish my homework**

## **How do you use Markdown on a GitHub webpage?**
First you need to create a webpage. Create a repository and go to Settings and Pages. Select Deploy from a branch, main and /docs and save the settings. (Fig 8) Your page will be available within 20 minutes.<br>
 
Then go to the <> Code tab. You can paste your plain text there and start editing using #, ##, <br>, ** as explained above in Fig 7 above. You need to go back and forth between Edit file and Preview. Once you are finished, click on Commit changes to save.

## **Summary**
In module 07, I created one script that has pickling and Try-Except blocks. I used online resources listed below at the References. I will add comments why I used those resources and why I though they were relevant. 

## **References**
https://www.youtube.com/watch?v=LjtIKL17Bpw  Python Tutorial 15: Solution to Python Pickle Homework Example Problems (Last accessed: 2/26/2023)<br>
I found this material very useful to understand how to pickle.dump and pickle.load data and how pickling works in Python. I tweaked and used his script as part of my assignment script. Added Try-Except exceptions to it and put his commands into functions and added the menu options to complete my script.<br>
https://www.youtube.com/watch?v=b0q9vVgAMq8 Try Catch with Loop (Python) (Last accessed: 2/26/2023) <br>
This material was useful for me to understand how to repeat the prompt until the user inputs a value in the correct format. With use of while True shown in this video, I was able to loop the step until the user inputs a value in an expected format.<br>
https://www.programiz.com/python-programming/user-defined-exception  Python Custom Exceptions (Last accessed: 2/25/2023)<br>
I read this article when I was looking for how to define my own Exception to use in my script. This article explains how to create a custom Exception very well.<br>

Python Programming, Third Edition, Course Technology, Michael Dawson 2019  ISBN-13 978-1-4354-5500-9
