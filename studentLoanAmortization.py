# Matthew Petersen              02-24-2025
# Lab 6
# During this -code we will use python to calculate monthly patment on a loan.
# In order to do so we must repeatedly subtract the monthly paymant amount from the remaining balance.

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    monthlyInterestRate = yearlyInterestRate / 12  
    numberOfMonths = numberOfYears * 12  

      
    monthlyPayment = (principal * monthlyInterestRate) / (1 - (1 + monthlyInterestRate) ** -numberOfMonths)

    print(f"\n{'Period':<8}{'Total Payment Due':<20}{'Computed Interest Due':<25}{'Principal Due':<20}{'Principal Balance':<20}")
    print("=" * 90)

    balance = principal  

    for period in range(1, numberOfMonths + 1):
        interestDue = balance * monthlyInterestRate  
        principalDue = monthlyPayment - interestDue  
        balance -= principalDue 

        print(f"{period:<8}{monthlyPayment:<20.2f}{interestDue:<25.2f}{principalDue:<20.2f}{balance:<20.2f}")

        if balance < 0:
            balance = 0

def main():
    principal = float(input("Enter the loan principal amount: "))
    yearlyInterestRate = float(input("Enter the yearly interest rate: "))
    numberOfYears = int(input("Enter the loan term: "))

    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)

if __name__ == "__main__":
    main()

    