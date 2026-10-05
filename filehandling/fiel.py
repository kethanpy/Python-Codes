
# 1. Write a Python program using a context manager (with) to 
# open a text file in read mode, read the entire content using 
# read(), and print the number of characters in the file. 
###########################
# with open("text.txt","r") as p:
#     s=p.read()
#     count=0
#     for i in s:
#         count+=1
        
# print(count)
##########################################3
# 2. Write a program that opens a file using a context manager, 
# reads all lines using readlines(), and prints only the lines that 
# contain more than 10 characters. 

# with open("text.txt","r")as s:
#     k=s.readlines()
#     for i in k:
#         if len(i)>10:
#             print(i)
###############################################33
# 3. Write a program that creates a file and writes 3 lines using 
# write(), reopens the same file in append mode, appends 2 
# more lines, and finally reads and prints the complete file 
# content.
########################3
# with open("text.txt","w")as k:
#     k.write("hello my name is kethan\n")
#     k.write("i am from manchiral\n")
#     k.write("my gradutation completede a ku\n")
# with open("text.txt","a") as n:
#     n.write("fsfjbj\n")
#     n.write("dsvjbv\n")
# with open("text.txt","r") as m:
#     z=m.read()
#     print(z)
#######################################################################################
# 4. Write a program that opens a file in read mode, reads the first 
# 10 characters, prints the current cursor position using tell(), 
# moves the cursor back to the beginning using seek(0), and 
# reads the full content again.  

# with open("text.txt", "r") as p:

#     s = p.read(10)
#     print(s)

#     print(p.tell())

#     p.seek(0)

#     s = p.read()
#     print(s)

# 5. Create a custom context manager using a class that opens a 
# file in write mode in the __enter__ method, writes a line to 
# the file, closes the file in the __exit__ method, and properly 
# prints or logs any exception information received in 
# __exit__. 
#################################################
# class myfile :
#     def __init__(self):
#         self.f=open("text.txt","w")
#         self.f.write("hello  python\n")
#         return self.f
#     def __exit__(self, exc_type, exc, tb):
#         if exc_type:
#             print("error",exc)
#         self.f.close()
# with myfile() as f:
#     print("file is open")
###############################################
# 6. Create a custom context manager using @contextmanager 
# from the contextlib module that opens a file, yields the file 
# object, and ensures the file is closed even if an exception 
# # occurs. 

# from contextlib import contextmanager

# @contextmanager
# def myfile():
#     f=open("text.txt","r")
#     try:
#         yield f
#     finally:
#         f.close()
# with myfile() as f:
#     print(f.read())

# 7. Write a program using a context manager that opens a file in 
# read mode, uses a loop to read the file in small chunks (for 
# example, 5 characters at a time), prints the cursor position after 
# each read using tell(), uses seek() to move to a specific position, 
# and continues reading from there
# with open("text.txt", "r") as f:

#     while True:
#         s = f.read(5)

#         if not s:
#             break

#         print(s)
#         print("Cursor position:", f.tell())

#         f.seek(10)

#         s = f.read(5)
#         print("After seek:", s)
#         print("Cursor position:", f.tell())

#         break           