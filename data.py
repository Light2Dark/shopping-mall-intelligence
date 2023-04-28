from enum import Enum

class PriceLevel(Enum):
  """Price level for a shop"""
  LOW = 25
  MEDIUM = 50
  HIGH = 75

shop_list_crowd_price = [  # [x,y,name,category, crowd_density, price_level]
  [120, 293, "PokeBowl", "Food", 25, PriceLevel.LOW],
  [52, 264, "Kinokuniya", "Books", 43, PriceLevel.HIGH],
  [98, 201, "Aeon", "Grocery", 140, PriceLevel.LOW],
  [115, 167, "Guardian", "Pharmacy", 20, PriceLevel.LOW],
  [161, 88, "Levis", "Fashion", 10, PriceLevel.HIGH],
  [200, 136, "Uniqlo", "Fashion", 68, PriceLevel.MEDIUM],
  [211, 177, "H&M", "Fashion", 36, PriceLevel.MEDIUM],
  [190, 290, "Floramiya", "Fashion", 18, PriceLevel.HIGH],
  [230, 271, "RalphLauren", "Fashion", 12, PriceLevel.HIGH],
  [250, 145, "Tealive", "Food", 49, PriceLevel.LOW],
  [238, 112, "Daboba", "Food", 20, PriceLevel.MEDIUM],
  [285, 216, "Popular", "Books", 46, PriceLevel.MEDIUM],
  [208, 34, "CaringPharmacy", "Pharmacy", 16, PriceLevel.MEDIUM],
  [284, 40, "McDonalds", "Food", 80, PriceLevel.LOW],
  [188, 198, "Fleurs", "Gifts", 6, PriceLevel.HIGH],
  [180, 167, "Animix", "Gifts", 11, PriceLevel.LOW],
  [310, 186, "Acer", "Technology", 20, PriceLevel.MEDIUM],
  [371, 120, "Dell", "Technology", 53, PriceLevel.MEDIUM],
  [345, 95, "HP", "Technology", 15, PriceLevel.HIGH],
]

shop_list = [  # [x,y,name,category]
  [120, 293, "PokeBowl", "Food"],
  [52, 264, "Kinokuniya", "Books"],
  [98, 201, "Aeon", "Grocery"],
  [115, 167, "Guardian", "Pharmacy"],
  [161, 88, "Levis", "Fashion"],
  [200, 136, "Uniqlo", "Fashion"],
  [211, 177, "H&M", "Fashion"],
  [190, 290, "Floramiya", "Fashion"],
  [230, 271, "RalphLauren", "Fashion"],
  [250, 145, "Tealive", "Food"],
  [238, 112, "Daboba", "Food"],
  [285, 216, "Popular", "Books"],
  [208, 34, "CaringPharmacy", "Pharmacy"],
  [284, 40, "McDonalds", "Food"],
  [188, 198, "Fleurs", "Gifts"],
  [180, 167, "Animix", "Gifts"],
  [310, 186, "Acer", "Technology"],
  [371, 120, "Dell", "Technology"],
  [345, 95, "HP", "Technology"],
]

# Opening/Exit coordinates
opening_list = [
  [138, 352, "OpeningOne"],
  [384, 30, "OpeningTwo"]
]

# Walkway coordinates
walkway_list = [
  [94, 267, "A"],
  [127, 272, "B"],
  [185, 258, "C"],
  [211, 240, "D"],
  [290, 145, "E"],
  [344, 116, "F"],
  [270, 82, "G"],
  [210, 85, "H"],
  [180, 104, "I"],
  [130, 169, "J"]
]

# Possible improvement - compute Euclidean distances automatically

step_cost = [ # path cost from one node to another connected node
  ['OpeningOne', 'B', 120],
  ['B', 'PokeBowl', 24],
  ['B', 'A', 52],
  ['B', 'C', 67],
  ['A', 'Kinokuniya', 47],
  ['A', 'Aeon', 56],
  ['A', 'J', 104],
  # ['Aeon', 'J', 60],
  ['J', 'Guardian', 25],
  ['J', 'Animix', 33],
  ['J', 'C', 178],
  ['J', 'I', 82],
  # ['Animix', 'I', 47],
  ['I', 'Levis', 34],
  ['I', 'Uniqlo', 42],
  ['I', 'H', 36],
  # ['Uniqlo', 'H', 65],
  ['H', 'CaringPharmacy', 30],
  ['H', 'Daboba', 30],
  ['H', 'G', 88],
  ['H', 'E', 180],
  ['G', 'McDonalds', 42],
  ['G', 'F', 193],
  ['F', 'HP', 15],
  ['F', 'OpeningTwo', 161],
  ['F', 'Dell', 38],
  ['F', 'E', 30],
  ['E', 'Acer', 35],
  ['E', 'Tealive', 45],
  ['E', 'Popular', 48],
  ['E', 'D', 210],
  ['D', 'RalphLauren', 35],
  ['D', 'H&M', 42],
  ['D', 'Fleurs', 46],
  # ['Fleurs', 'C', 52],
  ['C', 'D', 32],
  ['C', 'Floramiya', 30],
]