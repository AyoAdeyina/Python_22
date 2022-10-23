for x in range (0,151):
    print(x)

for y in range (5,1001,5):
    print(y)


for z in range (0,101):
    if z % 10 == 0:
        print("Coding Dojo")
    elif z % 5 == 0:
        print("Coding")
    else:
        print(z)


sum = 0
for x in range (0,500001,1):
    sum += x
print(sum)


for y in range (2018,0,-4):
    print(y)


lowNum = 2
highNum = 9
mult = 3

for z in range (lowNum,highNum +1):
    if z % mult == 0:
        print(z)