choice = "y"

while choice == "y":

    quiz_1 = int(input("Enter the score for Quiz 1: "))
    quiz_2 = int(input("Enter the score for Quiz 2: "))
    quiz_3 = int(input("Enter the score for Quiz 3: "))

    average = (quiz_1 + quiz_2 + quiz_3) / 3

    if average >= 50:
        print("Congrats you passed with an average of", average)
    else:
        print("Sorry you failed with an average of", average)

    choice = input("Do you want to enter another student's scores? (y/n): ")

    print("Thank you for using the student average calculator!")