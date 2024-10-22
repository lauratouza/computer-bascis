# Function to calculate monthly payment
def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_months):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    if annual_interest_rate == 0:
        return loan_amount / loan_term_months
    else:
        return loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -loan_term_months)

# Inputs
loan_amount = float(input("Enter the loan amount: "))
annual_interest_rate = float(input("Enter the annual interest rate (as a percent): "))
loan_term_months = int(input("Enter the loan term (in months): "))

# Calculation
monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_months)

# Output
print(f"Your monthly payment is: {monthly_payment:.2f}")
