# =============================================================================
#                                    TASK
# =============================================================================
# Write the code that will do the following:
#
# ● The user should be allowed to choose which calculation they want to do.
#   The first output that the user sees when the program runs should look like
#   this:
#
#   __________________________________________________________________________
#  | Investment - to calculate the amount of interest you'll earn on your     |
#  |              investment.                                                 |
#  | Bond       - to calculate the amount you'll have to pay on a home loan.  |
#  |                                                                          |
#  | Enter either “investment” or “bond” from the menu above to proceed:      |
#   --------------------------------------------------------------------------
#
# ● How the user capitalises their selection should not affect how the program
#   proceeds. In other words, “Bond”, “bond”, “BOND”, or “Investment”,
#   “investment”, “INVESTMENT”, etc., should all be recognised as valid
#   entries.
#   If the user doesn’t type in a valid input, show an appropriate error
#   message.
#
# ● If the user selects “investment”, ask the user to input:
#   ○ The amount of money that they are depositing.
#   ○ The interest rate (as a percentage). Only the number of the interest rate
#     should be entered – don’t worry about having to deal with the added “%”,
#     e.g., the user should enter 8 and not 8%.
#   ○ The number of years they plan on investing.
#   ○ Then ask the user to input if they want “simple” or “compound” interest,
#     and store this in a variable called interest. Depending on whether or not
#     they typed “simple” or “compound”, output the appropriate amount that
#     they will get back after the given period at the specified interest rate.
#     See the following block for the formulae to be used.
#
#    _____________________ INTEREST FORMULAE ______________________
#   | The total amount when simple interest is applied is          |
#   | calculated as follows: 𝐴 = 𝑃(1 + 𝑟 × 𝑡)                      |
#   | The Python equivalent is very similar: A = P * (1 + r*t)     |
#   |                                                              |
#   | The total amount when compound interest is applied is        |
#   | calculated as follows: 𝐴 = 𝑃(1 + 𝑟)^𝑡                        |
#   | The Python equivalent is slightly different:                 |
#   | A = P * math.pow((1+r), t)                                   |
#    --------------------------------------------------------------
#
#   In the formulae above:
#   ● “r” is the interest entered above divided by 100, e.g., if 8% is entered,
#     then “r” is 0.08.
#   ● “P” is the amount that the user deposits.
#   ● “t” is the number of years that the money is being invested.
#   ● “A” is the total amount once the interest has been applied.
#
#   ○ Print out the answer!
#   ○ Try entering 20 years and 8(%) and see what the difference is depending
#     on the type of interest rate!
#
# ● If the user selects “bond”, ask the user to input:
#   ○ The present value of the house, e.g., 100 000.
#   ○ The interest rate, e.g., 7.
#   ○ The number of months they plan to take to repay the bond, e.g., 120.
#
#    ___________________ BOND REPAYMENT FORMULA ___________________
#   | The amount that a person will have to repay on a home loan   |
#   | each month is calculated as follows:                         |
#   |                                                              |
#   | repayment = (i × P) / (1 − (1 + i)^(−n))                     |
#   |                                                              |
#   | The Python equivalent is slightly different:                 |
#   | repayment = (i * P) / (1 - (1 + i)**(-n))                    |
#    --------------------------------------------------------------
#
#   In the formula above:
#   ● “P” is the present value of the house.
#   ● “i” is the monthly interest rate, calculated by dividing the annual
#     interest rate by 12. Remember to divide the interest entered by the user
#     by 100, e.g., (8 / 100), before dividing by 12.
#   ● “n” is the number of months over which the bond will be repaid.
#   ● Calculate how much money the user will have to repay each month and
#     output the answer.
# =============================================================================


# =============================================================================
#                                    SOLUTION
# =============================================================================

# Import the math library:
# import math

# Create and display the introductory statement stating what options the user
#   has to choose from:
intro_text = '''
-------------------------------------------------------------------------------
                INVESTMENT / BOND REPAYMENT CALCULATOR
-------------------------------------------------------------------------------
Investment - to calculate the amount of interest you'll earn on your
             investment.
Bond       - to calculate the amount you'll have to pay on a home loan.
-------------------------------------------------------------------------------
'''
seperator_line = "------------------------------------------------------------\
-------------------"
print(intro_text)

# Request the user to choose either "investment" or "bond".
# Loop continues until the user enters a valid choice.
user_choice = ""         # Initialise the user choice as an empty string
valid_choices = ("investment", "bond")  # Store valid options in a tuple
while user_choice not in valid_choices:
    user_choice = input('Enter either “investment” or “bond” from the menu\
above to proceed: ').lower().strip()
    if user_choice not in valid_choices:
        print("Please select a valid option (investment / bond)")

# -------------------------------------------------------------------------
# INVESTMENT CALCULATION:
# -------------------------------------------------------------------------
# Create a tuple storing valid interest types:
valid_interest_types = ("simple", "compound")
interest_type = ""         # Initialise the user choice as an empty string
if user_choice == "investment":
    # Collect deposit, interest and investment period details from the user
    # Convert user input to float and round to 2 decimals:
    deposit_amt = round(float(input("Enter a deposit amount: ")), 2)
    # Convert percentage (user input) to a decimal number:
    interest_perc = float(
        input("Enter an interest rate: ").replace("%", "")
        ) / 100
    # Number of years invested:
    no_years = int(input("How long will the deposit be invested (in years)? "))
    # Ask user for type of interest (simple/compound) until valid
    while interest_type not in valid_interest_types:
        interest_type = input(
            "Select the interest type (simple or compound): "
            ).lower().strip()
        if interest_type not in valid_interest_types:
            print("Please select a valid interest type (i.e. simple or\
compound).")

    # --------------------------------------------------------------------
    # Calculate the investment value based on the interest type
    if interest_type == "simple":
        # Formula: A = P * (1 + r * t)
        investment_value = round(
            deposit_amt * (1 + interest_perc * no_years), 0)
    elif interest_type == "compound":
        # Formula: A = P * (1 + r)^t
        investment_value = round(
            deposit_amt * (1 + interest_perc) ** no_years, 0)
    # --------------------------------------------------------------------

    # Display the result of the investment calculation
    print("\n" + seperator_line)
    print(f"Your investment will be worth: R{investment_value}")
    print(seperator_line + "\n")

# -------------------------------------------------------------------------
# BOND CALCULATION:
# -------------------------------------------------------------------------
elif user_choice == "bond":
    # Collect house loan details from the user
    # Present value of the house:
    house_pv = round(
        float(input("Enter the current value of the house: ")), 2)
    # Obtain nominal interest rate & convert to a monthly rate in decimals
    # (i.e.: divide by 100, then by 12):
    mnthly_interest_perc = float(input("Enter the nominal interest rate: ").
                                 replace("%", "")) / 1200
    # Number of months for repayment:
    repayment_months = int(input("Enter the number of repayment months: "))

    # --------------------------------------------------------------------
    # Calcualte the repayment amount using the bond repayment formula:
    # Repayment = (i * P) / (1 - (1 + i)^(-n))
    repayment_amt = round((mnthly_interest_perc * house_pv)
                          / (1 - (1 + mnthly_interest_perc) **
                             (-repayment_months)), 2)
    # -------------------------------------------------------------------

    # Display the result of the monthly repayment calculation
    print("\n" + seperator_line)
    print(f"Your monthly bond repayment is: R{repayment_amt}")
    print(seperator_line + "\n")

# -------------------------------------------------------------------------
# END OF TASK
# -------------------------------------------------------------------------
# NOTES:
#
# To make it a little more challenging and gain experience with tools
# beyond what is expected so in the course so far, I've attempted to
# create a similar interest rate calculator in Streamlit.
# I've created the file called 𝑓𝑖𝑛𝑎𝑛𝑐𝑒_𝑐𝑎𝑙𝑐𝑢𝑙𝑎𝑡𝑜𝑟𝑠_𝑠𝑡𝑟𝑒𝑎𝑚𝑙𝑖𝑡.𝑝𝑦 for that
# purpose.
# -------------------------------------------------------------------------
