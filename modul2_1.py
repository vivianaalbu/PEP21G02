name='Jhon'
age=26
# print('name:',name,'age',age)
# print='print'

#type function

result=type(name)
print(result)

result=type(age)
print(result)

print(5*name)
result1=5*name
result2=type(result1)
print(result2)

result=id(name)
print(result)


print(8*8)
print((8).__add__(8))

print(8*'text')
print((8).__mul__('text'))
print(('text').__mul__(8))


print(8-8)
print((8).__sub__(8))


print(8/8)
print((8).__truediv__(8))


print(8**8)
print((8).__pow__(8))
print(pow(8,8))



#FLOAT

var=(8).__truediv__(8)
print(type(var))


#Exercitiu:

a=3
b=4
c=5
x=(-b+((b**2)-4*a*c)**(1/2))/(2*a)
x=(-b-((b**2)-4*a*c)**(1/2))/(2*a)

#Metode

bsqr=b.__pow__(2)
mul=(4).__mul__(a.__mul__(c))
var=(1).__truediv__(2)
dif1=bsqr.__sub__(mul)
print(type(dif1))
dif1=float(dif1)

#rad=dif.__pow__((1).__truediv__(2))

rad=dif1.__pow__(var)
print(type(rad))


dif2=rad.__sub__(b)
mul1=(2).__mul__(a)
impartire=dif2.__truediv__(mul1)


#Complex

nr1=1.0+1.0j
nr2=3+5j
print(nr1+nr2)
print(type(nr1))


#Strings
my_str1='My String \n no multi string'

print(my_str1)

#my_str1='''
this
a 
multi
string
test
'''

#print(my_str1)

my_str2=r"My String \n no multi line"
print(my_str2)


my_str2=f"""My String{my_str1}"""
print(my_str2)


#dir

info=dir(my_str2)
print(info)
var1='this is {}'
cap = var1.capitalize()
print(cap)
format1= var1.format('Sparta')
print(format1)

phone="0747.655.444"
split1=phone.split("7")
print(split1) 

phone="0747.655.444"
split1 = phone.split (SEP=".", MAXSPLIT=1)
print(split1)

#input
name= input('Give me your name:')

print(var1, input('give me your name'))

#slice
text="My Text"
first_letter="My Text"[0]
print(first_letter)
slice1 = text[1:4]
print(slice1)
slice2=text[0:7:1]
print(slice2)


text = input('Enter 10 characters text here: ')
slice1 = text[0:5]
slice2 = text[5:11]
print(slice2 + slice1)

#negative step
reverse= text[::-1]
print(reverse)

reverse1 = slice1[::-1]
reverse2 = slice2[::-1]
print(riverse2 + reverse1)

#True, False
my_bool = True
print(type(my_bool))
my_bool = False
print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))

Print(True+False)
print(dir(True))
x=True.__add__(False)
print(x)


#NONE
my_none = None
x = print('')
print(x)

print(bool(0+0j))
print(bool(0.0))







