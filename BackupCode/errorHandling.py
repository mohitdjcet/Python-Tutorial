# try:
#     a = int(input("Enter a number:"))
#     b = 10/a
#     print("Result:", b)
# except (ValueError,ZeroDivisionError):
#     print("Invalid Input")

# try:
#     num = int(input("Enter age"))
# except ValueError:
#     print("Invalid Input")
# else:
#     print("Your age is :",  num)

try:
    f = open("demo.txt")
    print(f.read())
except FileNotFoundError:
    print("File Not found")
finally:
    print("Excuted completed")
