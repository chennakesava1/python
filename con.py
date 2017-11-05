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
