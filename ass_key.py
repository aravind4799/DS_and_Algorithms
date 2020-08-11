
# input:
# b 3
# output:
# e

# input:
# Z 5
# output:
# E

val = str(input("enter a char:"))
displacement=int(input("enter a num:"))
# print("ass_key value:",ord(val))

# print("ans:",str(chr( ord(val) + displacement )) )
new_disp = ord(val) + displacement
if val.isupper():
    if new_disp > 90:
        new_disp=new_disp-90+65-1

if val.islower():
    if new_disp >122:
        new_disp=new_disp-122+97-1

#print(new_disp)
print("ans:",chr(new_disp))