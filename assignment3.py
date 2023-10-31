"""
Assignment 3: "Branching Out"

Author: Kirti Subramanian
CWID: 20531478
Date: 10/16/2022

Program Description: This program determines the user's auto insurance premium rates based on their age,
the value of their car, and the number of tickets that they have received in the last three years. If first
takes in these three input values from the user. Then, the program performs a series of calculations based on
the user's inputs and outputs a final monthly premium rate for the user.
"""


# This asks the user for the required information and sets a base premium value.
age = int(input("Driver's Age? "))
tickets = int(input("Number of Tickets? "))
value = int(input("Value of Car? "))
premium = 0.05*value

# This updates the value of the premium based on the user's age.
if age < 25:
    premium = premium + (0.15*premium)
elif age >= 25 and age <= 29:
    premium = premium + (0.1*premium)

# This updates the value of the premium based on the number of tickets the user has received in the past 3 years.
# If the user has more than 3 tickets, their premium is set to 0.
if tickets == 1:
    premium = "%.2f" % (premium + (0.1*premium))
elif tickets == 2:
    premium = "%.2f" % (premium + (0.25*premium))
elif tickets == 3:
    premium = "%.2f" % (premium + (0.5*premium))
elif tickets > 3:
    premium = 0

# This outputs the user's monthly premium rates after the calculations.
# If the user has more than 3 tickets, the program outputs a statement explaining why premium is denied (in a new line).
if premium != 0:
    print(f"Premium: ${premium}")
else:
    print(f"Premium: ${premium}")
    print("You are refused coverage because you have more than 3 tickets.")


# first test
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment3.py
Driver's Age? 35
Number of Tickets? 1
Value of Car? 10000
Premium: $550.00

Process finished with exit code 0
"""

# second test
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment3.py
Driver's Age? 29
Number of Tickets? 2
Value of Car? 15000
Premium: $1031.25

Process finished with exit code 0
"""

# third test
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment3.py
Driver's Age? 19
Number of Tickets? 3
Value of Car? 850
Premium: $73.31

Process finished with exit code 0
"""

# fourth test
"""
/Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/venv/bin/python /Users/kirtisubramanian/PycharmProjects/foothill/CS_3A_Fall_2022/assignment3.py
Driver's Age? 81
Number of Tickets? 4
Value of Car? 12500
Premium: $0
You are refused coverage because you have more than 3 tickets.

Process finished with exit code 0
"""