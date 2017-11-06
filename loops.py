#!/usr/bin/python

items = [ "tea","coffiee","bred","milk" ] 

for item in items:
    print(item)
items = [ "Abby","Brenda","Cindy","Diddy" ]
 
for item in items:
    print(item)


for i in range(2,20):
    print(i)
#### it contunies 

'''
x = 4
while x < 5:
    print(x)
'''
#####



correntnumber = 4
print (correntnumber)
guess = 1
while guess != correntnumber:
    guess = int(input("guess the number: "))
    if guess != correntnumber:
        print('no guess')
print (" your first guess right")


for x in range(1,10):
    for y in range(1,10):
        print("(" + str(x) + "," + str(y) + ")")


z = 1
while(z < 50):
    j = 2
    while(j <= (2/j)):
        if not(2%j): break
        j = j + 1
    if (j > z/j) : print z, " is prime"
    z = z + 1
print "wellcom!"
