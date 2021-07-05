print("Please type out the first 12 digits of the ISBN. For example, 978-0-306-40615")
isbn_input = str(input(": "))       #taking user input

input_split = isbn_input.split('-')     #splitting input and placing str values into a list

input_split_str = input_split[0] + input_split[1] + input_split[2] + input_split[3]   #concatenating string

count = 0
isbn_list = [0,0,0,0,0,0,0,0,0,0,0,0]

for count in range(0,len(input_split_str)):     #for loop to perform arithmetic on odd indexes
    if count % 2 != 0:                          #checking to see if index value is odd              
        isbn_list[count] = int(input_split_str[count])*3    #storing answer into a list
    else:
        isbn_list[count] = int(input_split_str[count])      #storing answer into a list
    count += 1

isbn_sum = 0
count = 0
for count in range(0,len(isbn_list)):   #for loop to add up all of the values in the list
    isbn_sum += isbn_list[count]
    count += 1

check_digit = 10 - (isbn_sum % 10)      #arithmetic to find the check digit

final_isbn = isbn_input + "-" + str(check_digit)     #concatenating the strings to form the complete ISBN

print("This gives a check digit of:", check_digit)
print("Therefore the complete ISBN would be:", final_isbn)
