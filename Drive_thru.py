# Write code below 💖
def get_item(item_number):
  if item_number==1:
    return 'Cheeseburger'
  elif item_number==2:
    return 'Fries'
  elif item_number==3:
    return 'Soda'
  elif item_number==4:
    return 'Ice Cream'
  elif item_number==5:
    return 'Cookie'
  else:
    return 'Sorry, we dont have that item Sir/Maam'

def welcome():
  return 'Welcome to our drive thru'

print(welcome())
order_number=int(input('What would You like to order Sir/maam'))
print(order_number)
print(get_item(order_number))
