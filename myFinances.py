def compoundAmount(principal, rate, time):
    return principal * (1 + rate) ** time

def main():
    principal = float(input("Enter 'initial amount': "))
    rate = float(input("Enter 'interest rate': "))
    time = float(input("Enter 'time': "))
    amount = compoundAmount(principal, rate, time)
    print(f"Final amount: ${amount}")

if __name__ == "__main__":
    main()

#--------------------------------------------------


def annualPercentageRate(nominalRate, periods):
    return (1 + nominalRate / periods) ** periods - 1

def main():
    nominalRate = float(input("Enter nominal interest rate: "))
    periods = int(input("Enter number of periods: "))
    apr = annualPercentageRate(nominalRate, periods)
    print(f"Annual Percentage Rate (APR): {apr}")

if __name__ == "__main__":
    main()