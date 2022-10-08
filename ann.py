import random
import matplotlib.pyplot as plt
from places import Location, Walkway, Entrance, Shop
from road import Road
from ant import Ant
from data import PriceLevel, shop_list, entrance_list, walkway_list, step_cost, shop_list_crowd_price

# visualise
def create_graph(locs):
  fig = plt.figure()
  ax = fig.add_subplot(1,1,1)
  locs_x = [loc.coordinates[0] for key, loc in locs.items()]
  locs_y = [loc.coordinates[1] for key, loc in locs.items()]
  categories = [loc.__class__.__name__ for key, loc in locs.items()]

  colors = {'Shop': 'blue', 'Entrance': 'red', 'Walkway': 'green'}

  ax.scatter(locs_x, locs_y, c=[colors.get(cat) for cat in categories])
  ax.set_aspect(aspect=1.0)
  # ax.invert_yaxis()
  return ax

def draw_pheromone(ax, roads):
  lines = []
  for road in roads:
    from_coord = road.connectedLocs[0].coordinates
    to_coord = road.connectedLocs[1].coordinates
    coord_x = [from_coord[0], to_coord[0]]
    coord_y = [from_coord[1], to_coord[1]]
    lines.append(ax.plot(coord_x, coord_y, c='k', linewidth=road.pheromone**2))
  return lines
    

# **** Testing function ****
def locList(locH):
  return ', '.join([y.name for y in locH])
  
def get_frequency_of_paths(ants):
  paths = []
  locs = []
  frequencies = []
  for ant in ants:
    if len(ant.path) != 0:
      if ant.path in paths:
        frequencies[paths.index(ant.path)] += 1
      else:
        paths.append(ant.path)
        locs.append(ant.locHistory)
        frequencies.append(1)
  return [frequencies, paths, locs]

# Used for termination condition - % ants taking same path 
def get_percentage_of_dominant_path(ants):
  [frequencies, _, _] = get_frequency_of_paths(ants)
  if len(frequencies) == 0:
    percentage = 0
  else:
    percentage = max(frequencies)/sum(frequencies)
  return percentage

def set_shops_crowd_price(locations):
  for coord1, coord2, name, category, crowd_density, price_level in shop_list_crowd_price:
    locations[name] = Shop(name)
    locations[name].category = category
    locations[name].set_coordinates([coord1, coord2])
    locations[name].set_crowd_density(crowd_density)
    locations[name].set_price(price_level)
  return locations

def set_shops(locations):
  for coord1, coord2, name, category in shop_list:
    locations[name] = Shop(name)
    locations[name].category = category
    locations[name].set_coordinates([coord1, coord2])
  print(locations)
  return locations
  
if __name__ == "__main__":
  # Instantiate Shop, Walkway, Entrance objects w/ lists provided
  locations = {}
  
  # set shops
  # locations = set_shops(locations)
  locations = set_shops_crowd_price(locations)
  
  for coord1, coord2, name in walkway_list:
    locations[name] = Walkway(name)
    locations[name].set_coordinates([coord1, coord2])

  for coord1, coord2, name in entrance_list:
    locations[name] = Entrance(name)
    locations[name].set_coordinates([coord1, coord2])
  
  roads = []
  for city1, city2, cost in step_cost:
    road = Road([locations[city1], locations[city2]], cost)
    locations[city1].add_road(road)
    locations[city2].add_road(road)
    roads.append(road)

  # print(type(locations['OpeningTwo']))

  # ***** Preprocessing to determine target dest - category, price ****

  # Define origin and destination cities
  origin = locations['OpeningTwo']
  # targetShops = [locations['Fleurs'], locations['McDonalds']]
  # targetShops = [locations['Acer'], locations['RalphLauren'], locations['Kinokuniya']]
  # targetShops = [locations['H&M'], locations['Tealive'], locations['McDonalds']]
  targetShops = [locations['HP'], locations['Fleurs'], locations['Kinokuniya']]
  # targetShops = [locations['HP']]

  # Define ACO parameters
  n_ant = 20    # Number of ants
  alpha = 1     # Pheromone influence constant
  rho = 0.5     # Evaporation rate

  # Set pheromone levels of all roads 
  initial_pheromone = 0.001
  for road in roads:
    road.set_pheromone(initial_pheromone)

  # Instantiate Ant objects
  ants = [Ant() for _ in range(n_ant)]
  
  # Termination threshold
  max_iteration = 30
  percentage_of_dominant_path = 0.9
  
  iteration = 0

  # visualise
  ax = create_graph(locations)
  lines = draw_pheromone(ax, roads)

  while (iteration < max_iteration and get_percentage_of_dominant_path(ants) < percentage_of_dominant_path): # termination conditions
    # loop through all the ants to identify the path of each ant
    for ant in ants:
      # reset the path of the ant
      ant.reset()
      # identify the path of the ant
      ant.get_path(origin, targetShops, alpha, locations, roads)
    # loop through all roads
    for road in roads:
      # evaporate the pheromone on the road
      road.evaporate_pheromone(rho)
      # deposit the pheromone
      # road.deposit_pheromone(ants)
      road.deposit_pheromone_crowd_price(ants)

    # visualise
    for l in lines:
      del l
    lines = draw_pheromone(ax, roads)
    plt.pause(0.05)

    # increase iteration count
    iteration += 1
  # after exiting the loop, return the most occurred path as the solution
  [freq, paths, cities_used] = get_frequency_of_paths(ants)
  print([c.name for c in cities_used[freq.index(max(freq))]])   # Get path sequence most frequent path sequence

  # input()