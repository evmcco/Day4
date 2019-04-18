
# Bill Calculator
bill = int(input("What's the total bill amount? "))
service = input("How was the service? ").lower()
split = int(input("Split how many ways? "))
tip = 0

def print_amounts():
    print("Tip Amount:  $%.2d" % tip)
    print("Total Amount: $%.2d" % (tip+bill))
    print("Amount per person: $%.2d" % ((tip + bill) / split))

if service == 'good':
    tip = bill * .2
    print_amounts()
elif service == 'fair':
    tip = bill * .15
    print_amounts()
elif service == 'bad':
    tip = bill * .1
    print_amounts()
else:
    print("Invalid Response, please try again")

"""
# Temp Conversion
temp_c = int(input("What's the temperature in C? "))
temp_f = temp_c * 1.8 + 32
print(str(temp_f)+ " F")

------------------------------------------------------------------

# Day of the Week
day = int(input("Pick a number 0-6 "))
string_ending = 'day'
if day == 0:
    string_beginning = 'Sun'
elif day == 1:
    string_beginning = 'Mon'
elif day == 2:
    string_beginning = 'Tues'
elif day == 3:
    string_beginning = 'Wednes'
elif day == 4:
    string_beginning = 'Thurs'
elif day == 5:
    string_beginning = 'Fri'
elif day == 6:
    string_beginning = 'Satur'
else:
    print("Invalid response, please try again")
print(string_beginning + string_ending)

if day in range(1,6):
    print("Go to work!")
elif day == 0 or day == 6:
    print("Sleep in")
"""