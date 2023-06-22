
# created two options to choose from
option_1 = "1 - Calculator"
option_2 = "2 - Show the equation"
print(option_1)
print(option_2)

# user choice
opt_selected = input("Please select the \"1\" or \"2\" option: ")

# when the calculator is selected - option 1
if opt_selected == "1":
    try:   # need to enter two numbers to perform the calculation and convert str to a floating number
        number_1 = float(input("Please enter a first number: ")) 
        number_2 = float(input("Please enter a second number: "))
        
        while True:  # if numbers are correct need to enter the operation
            opertion = input("Plese enter the operation you need to do: ")
            # create formulas for different types of operation
            if opertion == "+":
                answer = number_1 + number_2                       # calculation result
                equation = f"{number_1} + {number_2} = {answer}"   # equation
                print (equation)                                   
            elif opertion == "-":
                answer = number_1 - number_2
                equation = f"{number_1} - {number_2} = {answer}"
                print (equation)
            elif opertion == "*":
                answer = number_1 * number_2
                equation = f"{number_1} * {number_2} = {answer}"
                print (equation)
            elif opertion == "/":
                try:
                    answer = number_1 / number_2
                    equation = f"{number_1} / {number_2} = {answer}"
                    print (equation)
                except ZeroDivisionError:     # in case the second number is zero
                    print("Division by zero is impossible. Please enter a divisor greather than zero")
            elif opertion == "%":
                try:
                    answer = number_1 % number_2
                    equation = f"{number_1} % {number_2} = {answer}"
                    print (equation)
                except ZeroDivisionError:     # in case the second number is zero
                    print("Modulus Error! Division by zero is impossible. Please enter a divisor greather than zero")
            elif opertion == "**":
                answer = number_1 ** number_2
                equation = f"{number_1} ** {number_2} = {answer}"
                print (equation)
            else:                             # in case the user enter invalid operation
                print("The operation is not correct. Please enter the right operation")
            break

    except ValueError:   # in case the user doesn't enter a number
         print("Invalid value. Please enter the number")

    try:  # create and add each equation to a text file
        file = open("myCalculator.txt", "a")
        file.write(f"{equation}\n")
    except NameError:    # if at some stage due to an error we didn't get the Eq
        print("The equation is incorrect, no answer found. Please try again")

# when the show the equation is selected - option 2
elif opt_selected == "2":
    try:  # read and display the content of the file
        file = open("myCalculator.txt", "r")
        content = file.read()
        print(content)
        file.close()   
    except FileNotFoundError: # in case the file is not found
        print("Sorry, the file does not exist")
else:     # when user's choice is other than "1" or "2"
    print("Invalid input! Please enter the number 1 or 2 to select an option")

    






