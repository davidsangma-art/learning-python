# Write code below 💖
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry=entry
    self.name=name
    self.types=types
    self.description=description
    self.is_caught=is_caught

  def speak(self):
    print(self.name+" "+self.name+"!")

  def display_details(self):   
    print("Entry Number:",self.entry)
    print("Name:",self.name)
    print("Type:",self.types)
    print("Description:",self.description)
    if self.is_caught:
      print(self.name+" has already been caught!")
    else:
      print(self.name+" hasn't caught yet!")

pikachu=Pokemon(25,'Pikachu','Electric','It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs',True)
bulbasaur=Pokemon(1, 'Bulbasaur', 'grass, Poison','A strange seed was planted on its back at birth', False )

pikachu.speak()
bulbasaur.display_details()
pikachu.display_details()
