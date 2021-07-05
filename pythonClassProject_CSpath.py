class Menu:
  '''
  The class that deals with menus at different time
  '''
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

  def calculate_bill(self, purchased_items):
    self.total = 0
    for item in purchased_items:
      self.total += self.items.get(item, 0)
    return "The amount you have to pay is {}".format(self.total)

class Franchise:
  '''
  The information of different restaurant.
  '''
  
  def __init__(self, name, address, menus):
    self.name = name
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "The address of the restaurant is {}".format(self.address)

  def available_menus(self, time):
    self.available = []
    for menu in self.menus:
      if menu.start_time <= time and menu.end_time >= time:
       self.available.append(menu.name)
    return "Th available menu will be: {}".format(str(self.available))

class Business:
  '''
  Different store with the same menu will be combined into Business
  '''
  def __init__(self, name, franchise):
    self.name = name
    self.franchise = franchise

  def show_franchise(self):
    print("The franchise in this business will be:")
    for store in self.franchise:
      print("-->",store.name)



items_brunch = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
# all converted to 24 hours format
brunch = Menu("Brunch",items_brunch, 1100, 1600)

items_early_bird = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
early_bird = Menu("Early Bird", items_early_bird, 1500, 1800)

items_dinner = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu("Dinner", items_dinner, 1700, 2300)

item_kids ={
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00,
}
kids = Menu("Kids", item_kids,1100, 2100)
print(brunch)
# brunch calculate bills!
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate','mushroom ravioli (vegan)']))

flagship_store = Franchise("flagship_store","1232 West End Road",[brunch, early_bird, dinner, kids])
new_installment =  Franchise("new_installment", "12 East Mulberry Street",[brunch, early_bird, dinner, kids])
print(flagship_store)
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment]) 

# areapas??
arepa_menu = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_place = Franchise("areapas_place","189 Fitzgerald Avenue", arepa_menu)
new_business = Business("Take a' Arepa",[arepas_place])
business.show_franchise()
