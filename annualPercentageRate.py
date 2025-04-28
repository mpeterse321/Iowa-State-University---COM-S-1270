# Matthew Petersen
# Lab 4 
# Description: Calculating the annual percentage rate (APR) using code.

def annualPercentageRate(nominalRate, periods):
    return (1 + nominalRate / periods) ** periods - 1

def main():
    nominalRate = float(input("Enter nominal interest rate: "))
    periods = int(input("Enter number of periods: "))
    apr = annualPercentageRate(nominalRate, periods)
    print(f"Annual Percentage Rate (APR): {apr}")

if __name__ == "__main__":
    main()