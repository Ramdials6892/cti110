item_name = str(input('Enter food item name:\n'))
item_price = float(input('Enter item price:\n'))
item_quantity = int(input('Enter item quantity:\n'))
item_total = item_price * item_quantity
print("")
print("RECEIPT")
print(item_quantity,item_name,'@','${:.2f}'.format(item_price),'=','${:.2f}'.format(item_total))
print('Total cost:','${:.2f}'.format(item_total))
print("")
print("")
second_item_name = str(input('Enter second food item name:\n'))
second_item_price = float(input('Enter item price:\n'))
second_item_quantity = int(input('Enter item quantity:\n'))
second_item_total = second_item_price * second_item_quantity
total = item_total + second_item_total
print("")
print("RECEIPT")
print(item_quantity,item_name,'@','${:.2f}'.format(item_price),'=','${:.2f}'.format(item_total))
print(second_item_quantity,second_item_name,'@','${:.2f}'.format(second_item_price),'=','${:.2f}'.format(second_item_total))
print('Total cost:','${:.2f}'.format(total))
print("")
gratuity = total * .15
total_with_tip = gratuity + total
print('15% gratuity:','${:.2f}'.format(gratuity))
print('Total with tip:','${:.2f}'.format(total_with_tip))