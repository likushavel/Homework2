name = input('entre something in English')
buks = 'IOEAUioeau'
s = 0
for i in name :
    if i in buks:
        s += 1
print(s)