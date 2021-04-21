"""
get from input 23:30:31
get from input 23:31:31

find difference between the 2 inputs in seconds
"""
""""
x = input("Get time1: ")
hours = int(x[0:2])
minutes = int(x[3:5])
seconds = int(x[6:8])

print(type(hours))
print(hours)
print(type(minutes))
print(seconds)
print(type(seconds))

y = input("Get time2: ")
hours2 = int(y[0:2])
minutes2 = int(y[3:5])
seconds2 = int(y[6:8])

print(type(hours))
print(hours)
print(type(minutes))
print(seconds)
print(type(seconds))

t1 = 3600 * hours + 60 * minutes + seconds
t2 = 3600 * hours2 + 60 * minutes2 + seconds2
print(t2 - t1)


Get text from input:abcdefg
return:bcdefg
"""

text = input("Get text: ")
f_letter = text[0:1]
s_letter = text[1:2]
t_letter = text[2:3]
f1_letter = ord(f_letter) + 1
f2_letter = chr(f1_letter)
s1_letter = ord(s_letter) + 1
s2_letter = chr(s1_letter)
print(f2_letter,s2_letter, sep='')
