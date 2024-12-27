# inp = input("Enter Farenheit temperature: ")
# try:
#     fahr = float(inp)
#     cel = (fahr - 32.0) * 5.0/9.0
#     print(cel)
# except:
#     print("Please enter a number")

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.


# hrs = input("Enter Hours:")
# h = float(hrs)
# rate = float(input("Enter Regular Rate:"))

# if h > 40:
#     overtime = (h-40) * (1.5 * rate)
#     pay = 40 * rate + overtime
# else:
#     pay = h * rate
    
# print(pay)

#     Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:


try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = float(input("Enter Regular Rate:"))
    if h > 40:
        overtime = (h-40) * (1.5 * rate)
        pay = 40 * rate + overtime
    else:
        pay = h * rate
        
    print(pay)
except:
    print('Please provide a number')