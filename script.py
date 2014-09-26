#Tip Calculator

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)

#Date and Time
from datetime import datetime
now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

#If, Elseif, Else Statements
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

#Control Flow
ef clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

