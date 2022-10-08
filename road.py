import places

class Road:
  def __init__(self, connectedLocs, cost, pheromone=0):
    self.connectedLocs = connectedLocs
    self.cost = cost
    self.pheromone = pheromone
    
  def set_pheromone(self, pheromone):
    self.pheromone = pheromone
    
  def evaporate_pheromone(self, rho):
    self.pheromone = (1-rho) * self.pheromone
    
  def deposit_pheromone(self, ants):
    deposited_pheromone = 0

    # Search for ants that have used the road
    for ant in ants:
      if self in ant.path:
        # Deposited pheromone is inversely proportional to path length
        deposited_pheromone += 5/ant.get_path_length()**1
    self.pheromone += deposited_pheromone
      
  # deposit pheromone but factoring in price, crowd and walking distance    
  def deposit_pheromone_crowd_price(self, ants):
    deposited_pheromone = 0

    for ant in ants:
      if self in ant.path:
        cost = 0
        if (type(self.connectedLocs[-1]) == places.Shop):   # end of the road is the destination
          shop: places.Shop = self.connectedLocs[-1]
          cost = (1/3 * ant.get_path_length()**1)  + (1/3 * 1/shop.crowd) + (1/3 * 1/shop.price.value)
        else:
          cost = ant.get_path_length()**1
        deposited_pheromone += 5/cost
        
    self.pheromone += deposited_pheromone

  # **** Pheromone increase function based on connectedLoc types (???) ****