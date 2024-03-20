'''
Created on Feb 24, 2022

@author: michaelmordec
'''
#from lab2excercise2.Lab2_Mordec import original_comission
#from lab2excercise2.Lab2_Mordec import original_comission

number_of_shares = 2000
original_price_per_share = 40
original_investment = number_of_shares * original_price_per_share
original_comission = original_investment * 0.03

new_price_per_share = 42.75
new_total_value = number_of_shares * new_price_per_share
new_comission = new_total_value * 0.03

profit = new_total_value - original_investment - original_comission - new_comission
print("The amount of money Joe paid:", original_investment)
print("The amount of commission Joe paid his broker when he bought the stock:", original_comission)
print("The amount that Joe sold the stock for:", new_total_value)
print("The amount of commission Joe paid his broker when he sold the stock:", new_comission)
print("Display the amount of money that Joe had left when he sold the stock and paid his broker:",profit)