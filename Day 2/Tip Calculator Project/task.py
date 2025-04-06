# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
#
# tip_as_percent = (tip / 100)
# total_tip_amt = tip_as_percent * bill
# bill_with_tip = bill + total_tip_amt
# amount_payable =  (bill_with_tip / people)
#
# print(f"Tip percentage: {tip}%")
# print(f"Tip amount: {total_tip_amt}")
# print(f"Total bill with tip: {bill_with_tip}")
# print(f"Each person will pay: ${round(amount_payable, 2)}")
#
#
#

print("Welcome to Kemma's Treasury Bill calculator!")
print("Treasury Bill Rates in Ghana as at April 2025\n 91 DAY BILL ----Rate 15.0606%\n 182 DAY BILL ----Rate 15.2438%\n 364 DAY BILL ----Rate 15.8464%")

amount_invested = float(input("What amount are you investing? GHS"))
T_bill_type = int(input("What treasury bill days are you going for ? 91 182 364 "))
Rate = 0
DAY_91_BILL_Rate = 15.0606
DAY_182_BILL_Rate = 15.2438
DAY_364_BILL_Rate = 15.8464
#people = int(input("How many people to split the bill? "))

# def calculator ():
#     if T_bill_type == 91:
#         Rate = DAY_91_BILL_Rate
#         interest_convert = (Rate / 100)/4
#         interest_amt = amount_invested * interest_convert
#         amt_invest_plus_interest = amount_invested +interest_amt
#         print(".......Results......")
#         print(f"Principal Amount: {amount_invested}")
#         print(f"Treasury Bill Type: 91 DAY BILL")
#         print(f"Rate for 91 Days: {DAY_91_BILL_Rate}%")
#         print(f"Interest Return for 91 Days: {round(interest_amt, 2)}")
#         print(f"Total Total Return after 91 Days: {round(amt_invest_plus_interest,2)}")
#     elif T_bill_type == 182:
#         Rate = DAY_182_BILL_Rate
#         interest_convert = (Rate / 100)/6
#         interest_amt = amount_invested * interest_convert
#         amt_invest_plus_interest = amount_invested +interest_amt
#         print(".......Results......")
#         print(f"Principal Amount: {amount_invested}")
#         print(f"Treasury Bill Type: 182 DAY BILL")
#         print(f"Rate for 182 Days: {DAY_182_BILL_Rate}%")
#         print(f"Interest Return for 182 Days: {round(interest_amt, 2)}")
#         print(f"Total Total Return after 182 Days: {round(amt_invest_plus_interest,2)}")
# calculator()


def calculator ():
    if T_bill_type == 91:
        Rate = DAY_91_BILL_Rate
        interest_convert = (Rate / 100 + 1) ** (T_bill_type / 365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested
        print(".......Results......")
        print(f"Principal Amount: {amount_invested}")
        print(f"Treasury Bill Type: 91 DAY BILL")
        print(f"Rate for 91 Days: {DAY_91_BILL_Rate}%")
        print(f"Interest Return for 91 Days: {round(interest_amt, 2)}")
        print(f"Total Total Return after 91 Days: {round(amt_invest_plus_interest,2)}")
    elif T_bill_type == 182:
        Rate = DAY_182_BILL_Rate
        interest_convert = (Rate / 100 +1)**(T_bill_type/365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested
        print(".......Results......")
        print(f"Principal Amount: {amount_invested}")
        print(f"Treasury Bill Type: 182 DAY BILL")
        print(f"Rate for 182 Days: {DAY_182_BILL_Rate}%")
        print(f"Interest Return for 182 Days: {round(interest_amt, 2)}")
        print(f"Total Total Return after 182 Days: {round(amt_invest_plus_interest,2)}")
    elif T_bill_type == 364:
        Rate = DAY_364_BILL_Rate
        interest_convert = (Rate / 100 + 1) ** (T_bill_type / 365)
        amt_invest_plus_interest = amount_invested * interest_convert
        interest_amt = amt_invest_plus_interest - amount_invested
        print(".......Results......")
        print(f"Principal Amount: {amount_invested}")
        print(f"Treasury Bill Type: 364 DAY BILL")
        print(f"Rate for 364 Days: {DAY_182_BILL_Rate}%")
        print(f"Interest Return for 364 Days: {round(interest_amt, 2)}")
        print(f"Total Total Return after 364 Days: {round(amt_invest_plus_interest, 2)}")
calculator()
