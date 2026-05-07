# Write code below 💖
class Restaurant():
  def __init__ (self):
    self.name=''
    self.category=''
    self.rating=0.0
    self.delivery=False

bob_burgers=Restaurant()
bob_burgers.name="Bob's Burgers"
bob_burgers.category='American Diner'
bob_burgers.rating=4.7
bob_burgers.delivery=False

restaurant2=Restaurant()
restaurant2.name='Spice Garden'
restaurant2.category='Fine Dining'
restaurant2.rating=5.5
restaurant2.delivery=True

restaurant3=Restaurant()
restaurant3.name='Coffee Corner'
restaurant3.category='Cafe'
restaurant3.rating=6.6
restaurant3.delivery=False

print(vars(bob_burgers))
print(vars(restaurant2))
print(vars(restaurant3))
