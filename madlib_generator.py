import random
"""
def caps_word(word):
    word = str(word)
    word = word.capitalize()
    return word
"""
worst_food = input("What's your least favorite food? ")
# worst_food = caps_word(worst_food)
index = random.randint(1,5)

def build_madlib(food, index):
    if index == 1:
        result = "It was the best of %s, it was the worst of %s" % (food, food)
    elif index == 2:
        result = ("Reach for the stars, for if you fall you'll land in the %s" % food)
    elif index == 3:    
        result =  ("Call me %s" % food)
    else:
        result =  ("May the %s be with you" % food)
    return result

print(build_madlib(worst_food, index))

"""
if __name__ == '__main__':
    madLib()
"""


