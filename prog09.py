#Write a program to define and use user-defined functions with different types of arguments.

def display():
    print("This Is Simple Display Function")

def dis(nm):
    print()
    print(f"I am {nm} , This is Positional Argument")

def dis1(num=5,sq=2):
    return num**sq;

def keyword_arg(first,last):
    print()
    print("This Is Keyword Argument")
    print(f"Hiii My Name Is {first} {last}")

def vari_arg(num,*nm):
    for i in nm:
        print(" ",i*i)
  
display()

dis(nm="bobby")

sqr=dis1(num=5,sq=2)
print()
print(" This Is Default Argument ===",sqr)

keyword_arg(first="Bobby",last="Blexy")

print()
print("this is Variable Argument")
vari_arg(1,2,3,4,5,6,7,8,9)



