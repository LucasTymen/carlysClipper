hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0

# step 1 & 2
for price in prices :
  total_price += price

# step 3
average_price = total_price / len(prices)

# step 4
print("average_price : ${0} ".format(average_price))

# step 5
new_prices = [price - 5 for price in prices]

# step 6
print(new_prices)

# step 7
total_revenue = 0

# step 8
for i in range(len(hairstyles)):
  # step 9
  total_revenue += prices[i] * last_week[i]

# step 10
print("Total Revenue : ${} ".format(total_revenue))

# step 11
average_daily_revenue  = total_revenue / 7
print("average Daily revenue : ${} ".format (average_daily_revenue))

# step 12
cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]< 30]

# step 13
print(cuts_under_30)
