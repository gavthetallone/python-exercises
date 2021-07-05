print("#### Welcome to Grade Calculator ####")

marks = {"maths":0, "chemistry":0, "physics":0}

marks["maths"] = int(input("Please enter your maths mark: "))
marks["chemistry"] = int(input("Please enter your chemistry mark: "))
marks["physics"] = int(input("Please enter your physics mark: "))

percentage_average = float(sum(marks.values())/len(marks.values()))
print(f"Your percentage score is ""{:.1f}%".format(percentage_average))     #converting float output to 1 decimal place

if percentage_average >= 70:
    print("You scored a grade of: A")
elif percentage_average >= 60:
    print("You scored a grade of: B")
elif percentage_average >= 50:
    print("You scored a grade of: C")
elif percentage_average >= 40:
    print("You scored a grade of: D")
elif percentage_average < 40:
    print("You failed")