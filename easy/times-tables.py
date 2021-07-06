def times_tables(number):
    num = int(number)
    num_list = [[0 for x in range(num)] for y in range(num)]
    
    z = 1
    for i in range(0, num):

        for count in range(0, len(num_list[i])):
            num_list[i][count] = (count+1) * z
        
        z += 1
    return(f"Here are all of the times tables up to {number}: \n{num_list}")

print(times_tables(input("Please type in a number: ")))