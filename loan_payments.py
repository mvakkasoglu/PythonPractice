# Write a program that lets the user enter the
# interest rate, number of years, and loan
# amount, and computes monthly payment and
# total payment.
# monthly_payment = (loan_amount * monthly_interest_rate) / (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))


def monthly_payment():
    loan_amount = int(input("enter loan amount: "))
    monthly_interest_rate = float(input("enter monthly interest rate: "))
    number_of_years = int(input("enter loan period (years): "))
    monthly_payment = (loan_amount * monthly_interest_rate) / (
                1 - (1 / (1 + monthly_interest_rate) ** (number_of_years * 12)))
    return monthly_payment


print("your monthly payment is: {}".format(round(monthly_payment(), 2)))



