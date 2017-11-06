#!/user/bin/python
inputs = float(input("enter ur number"))
if inputs == 3:
    print ("con is truu")
else: 
    print "input is not 3"



##elif
inputs = float(input("enter the second number"))
if inputs == 2:
    print "given number is 2"
elif inputs > 2:
    print "given number below 2"
else:
    print "given number abow 2"

##Nested if
inputs = float(input("enter the 3rd number"))
if inputs <= 4:
    if inputs == 4:
        print "Given number is 4"
    else:
        print "given number below 4"
else:
    print "given number not in 0 to 4"

friends = raw_input("type a first later of ur friend name")
if friends == 'm':
    print ("Mounika")
elif friends == 'p':
    print ("Praveen")
elif friends == 'r':
    print ("rama rao")
elif friends == 'k':
    print ("Koti")
else:
    print (" your friends list need to update ")


print "Thank you !"

a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
if a < b < c:
    print ( "given numbers a < b < c")
else: 
    print ( " given numbers are not like a<b<c")


ab = int(input("enter a number only: "))
cd = int(input("enter a number morethen ab"))
if ab < cd:
    print("ab < cd")
else:
    print("ab > cd ")
if ab < 10 and ab > 5:
    print ( " ab value in betwin 5 to 10")
else:
    print (" ab value not inbetwin 5 to 10")

