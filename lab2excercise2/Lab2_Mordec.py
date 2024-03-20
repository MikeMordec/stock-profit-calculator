'''
Created on Feb 24, 2022

@author: Michael Mordec
'''
#from lab2excercise2.Exercise2 import original_comission
from lab2excercise2.Exercise2 import original_investment, original_comission
number_of_shares = float(input("Number of shares: "))
original_price_per_share = float(input("Amount paid per share: "))
original_investment = number_of_shares * original_price_per_share
original_comission = original_investment * 0.03

new_price_per_share = original_price_per_share * 2.25
new_total_value = number_of_shares * new_price_per_share
new_comission = new_total_value * 0.03

profit = new_total_value - original_investment - new_comission - original_comission
print("The amount of money Joe paid:", original_investment)
print("The amount of commission Joe paid his broker when he bought the stock:", original_comission)
print("The amount that Joe sold the stock for:", new_total_value)
print("The amount of commission Joe paid his broker when he sold the stock:", new_comission)
print("Display the amount of money that Joe had left when he sold the stock and paid his broker:",profit)

