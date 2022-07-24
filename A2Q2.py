#Write a python program to print a dictionary whose keys should be the alphabet from a-z and the values should be corresponding to the ASCII values.

dict={}
for i in range(97, 123):
    dict[str(i)]=chr(i)
print(dict)