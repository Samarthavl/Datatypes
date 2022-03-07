Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 5
print(type(x)) 

SyntaxError: multiple statements found while compiling a single statement
x = 5
print(type(x))
<class 'int'>
#disply x:
print(x)
5
print(type(x))
<class 'int'>
x = "hello samarth"
print(type(x))
<class 'str'>
x=20.5
print(type(x))
<class 'float'>
x=1j
print(type(x))
<class 'complex'>
x={"rcb","delhi","mumbai")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
x=["rcb","delhi","mumbai"]


print(type(x))
<class 'list'>
x=range(6)
print(type(x))
<class 'range'>
x={"sam","ram","rom"}
print(type(x))
<class 'set'>
x-=frozenset({"apple","banana","mango"})
print(type(x))
<class 'set'>
x=frozenset({"apple","banana","mango"})
print(type(x))
<class 'frozenset'>
print(type(x))
<class 'frozenset'>
x= True
print(type(x))