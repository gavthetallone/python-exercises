def near_enough(input1, input2):

    if len(input2) != len(input1)-1:
        return(f"\n{False}. The second word CANNOT be made from the first by removing a letter!\n")
    else:
        for count in range(0,len(input1)):
            if input1[:count] + input1[count+1:] == input2:
                return(f"\n{True}. The second word CAN be made from the first by removing a letter!\n")
        else:
            return(f"\n{False}. The second word CANNOT be made from the first by removing one letter!\n")

print("\n*\t*\t*\t*\tIS IT NEAR ENOUGH?\t*\t*\t*\t*\n")
print(near_enough(input("Please input two words. Can the second be made from the first by removing a letter?\n\n1: "), input("2: ")))