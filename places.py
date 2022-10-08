from data import PriceLevel

# Abstract class for location points
class Location:
  def __init__(self, name):
    self.name = name
    self.roads = []
    self.coordinates = []
    
  def set_coordinates(self, coordinates):
    self.coordinates = coordinates

  def add_road(self, road):
    if road not in self.roads:
      self.roads.append(road)

class Walkway(Location):
  def __init__(self, name):
    super().__init__(name)

class Entrance(Location):
  def __init__(self, name):
    super().__init__(name)

class Shop(Location):
  def __init__(self, name):
    super().__init__(name)
    self.category = None
    
  def set_price(self,price: PriceLevel):
    self.price = price
    
  def set_crowd_density(self, crowd_amount):
    self.crowd = crowd_amount