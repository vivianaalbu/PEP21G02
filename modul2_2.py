# chr
"""
print(chr(101))
print(ord('e'))

# if
a = 3
if 1 == a:
    print("1")
elif 1 == a:
    print('2')
else:
  print("3")
"""

from time import sleep

for letter in 'my text':
    print(letter, end='')
    sleep(1)

print(letter)



#True and True --> true


#False or False --> false

#XOR
a='a'
b='b'

print(a and b)

if a:
    print(b)
else:
    print(a)

  a='a'
  b='b'

    print(a or b)

    if a:
        print(a)
    else:
        print(b)