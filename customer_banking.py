# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account 
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = float(input("Please enter your savings balance: "))
    savings_interest = float(input("Please enter the savings interest rate: "))
    savings_maturity = int(input("Please enter the length of the month for account: "))



    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Here is your savings interest earned: ${savings_interest_earned:.2f}")
    print(f"This is the total savings account balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = float(input("Please enter your CD balance: "))
    cd_interest = float(input("Please enter the CD interest rate: "))
    cd_maturity = int(input("Please enter the length of the month for account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Here is your CD interest earned: {cd_interest_earned:.2f}") 
    print(f"This is the total CD account balance: ${updated_cd_balance:.2f}")


if __name__ == "__main__":
    # Call the main function.
    main()

""" Additional note: The Customer banking takes in the inputted information to be converted 
    from the functions imported (Savings and CD).

    The Account class to set the balance and interest for each functions.


    The calculation and convertion is done in the cd and savings functions. 

    Customer banking more like the front-end and cd and savings and account class is the back-end"""