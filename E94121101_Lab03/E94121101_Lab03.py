n=int(input("please input a number :")) #example:7

if n%2==1:
    print("this is odd")
else:
    print("this is even")

c=input("please input your student ID first character")
i=int(input("please input your student ID last 8 numbers")) #example: E94121101

if i%2==1:
    print("your student ID number is odd")
else:
    print("your student ID number is even")
print("your student ID is:",end="")
print(c,end="")
print(i)
