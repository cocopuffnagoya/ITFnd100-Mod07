Name: Coco Jones<br>
Date: February 26, 2023<br>
Class: ITFDN110A<br>
Module: 07<br>
GitHub: 

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
