#matrix multiplcation

matrix_one = [[1,2],
              [4,5]]

matrix_two = [[9,8],
              [7,6],]
              


mm_height = len(matrix_one[0])
mm_length = len(matrix_two)

print(str(mm_height) + " X " + str(mm_length))
#build a blank matrix to populate
multiplied_matrix = list()
for rows in range(mm_length):
    top_row = [0 for _ in range(mm_height)]
    # top_row = [0] * mm_height
    multiplied_matrix.append(top_row)

print(multiplied_matrix)


#calculate the values

result = 0
#first 2 for loops loop through the blank matrix
for a in range(mm_height):
    for b in range(mm_length):
        # next 2 for loops calculate the result for that index
        for c in range(mm_height-1):
            print("a: %d b: %d c: %d" % (a,b,c))
            result = matrix_one[c][a] * matrix_two[b][c]
            print(str(result))
            multiplied_matrix[a][b] += result
            print(multiplied_matrix)


print(multiplied_matrix)


        





"""
start_list = []
while len(start_list) < 5:
    start_list.append(int(input("Add a number to the list ")))
print("Starting List:")
print(start_list)


# Positive Numbers II
positive_list = []
for number in start_list:
    if number >= 0:
        positive_list.append(number)
print("Positives: ")
print(positive_list)
"""