miles_gallon = float(input(''))
gasdollars_gallon = float(input(''))
cost20 = (20 / miles_gallon) * gasdollars_gallon
cost75 = (75 / miles_gallon) * gasdollars_gallon
cost500 = (500 / miles_gallon) * gasdollars_gallon
print('{:.2f} {:.2f} {:.2f}'.format(cost20, cost75, cost500))