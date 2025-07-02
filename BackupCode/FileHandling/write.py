# f = open("/Users/mohitkumar/Desktop/PythonTutorial/FileHandling/demo.txt","a")
# # f.write("Hello, World!")
# # f.write("\nThis is a new line.")
# # f.write("Hello, World!")
# f.write("\nAppending a new line to the file.")
# f.close()

#r+ = read and write mode(Overwrite from starting of the file)
#w+ = write and read mode (overwrites the file)
#a+ = append and read mode (does not overwrite the file)(End of the file)
# f = open("/Users/mohitkumar/Desktop/PythonTutorial/FileHandling/demo.txt","a+")
# f.write("abc")
# f.close()


#With Syntax
# with open("/Users/mohitkumar/Desktop/PythonTutorial/FileHandling/demo.txt","a") as f:
#     # data = f.read()
#     f.write("\nAppending a new line using with syntax.")

# os
import os
os.remove("/Users/mohitkumar/Desktop/PythonTutorial/FileHandling/demo.txt")

