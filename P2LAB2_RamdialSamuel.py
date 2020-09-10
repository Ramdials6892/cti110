current_price = int(input())
last_months_price = int(input())
monthly_mortgage = (current_price * 0.051) / 12
change = current_price - last_months_price
print("This house is ${current}. The change is ${change} since last month.".format(current = current_price,change = change))
print('The estimated monthly mortgage is ${mortgage:.2f}.'.format(mortgage = monthly_mortgage))