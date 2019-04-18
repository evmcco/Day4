#caesar cypher
string_to_cypher = input("What string do you want to cypher? ")
cyphered_string = ""
key = int(input("How many letters do you want to shift? "))
while key >= 26: # make sure the key is between 0 and 25
    key -= 26
i = 0
while i < len(string_to_cypher):
    if string_to_cypher[i] != " ": # skip spaces
        ascii_val = ord(string_to_cypher[i]) # grab the ascii val of the letter
        new_ascii_val = ascii_val + key # add the key to the ascii val
        while new_ascii_val > 122: # make sure the ascii val is between 96 and 122
            new_ascii_val -= 26
        while new_ascii_val < 96:
            new_ascii_val += 26
        cyphered_string = cyphered_string + chr(new_ascii_val) # add the moved char to the string
    else:
        cyphered_string = cyphered_string + " "
    i += 1
print(cyphered_string)

# lbh zhfg hayrnea jung lbh unir yrnearq



"""
#1337 3p34k
string = input("What phrase do you want to translate? ")
leet_string = ""
i = 0
while i < len(string):
    test_char = string[i].lower()
    if test_char == "a":
        leet_string = leet_string + "4"
    elif test_char == "e":
        leet_string = leet_string + "3"
    elif test_char == "g":
        leet_string = leet_string + "6"
    elif test_char == "i":
        leet_string = leet_string + "1"
    elif test_char == "o":
        leet_string = leet_string + "0"
    elif test_char == "s":
        if i == (len(string) - 1):
            leet_string = leet_string + "z"
        else:
            leet_string = leet_string + "5"
    elif test_char == "t":
        leet_string = leet_string + "7"
    else:
        leet_string = leet_string + string[i]
    i += 1
print(leet_string)


#reverse a string
old_string = "hello this is a test"
new_string = ""
i = len(old_string) - 1

while i >= 0:
    new_string = new_string + old_string[i]
    i -= 1
print(new_string)
"""