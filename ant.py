import random

class Ant:
  def __init__(self):
    self.locHistory = []    # Locations the ant passes through, in sequence
    self.path = []      # Roads the ant uses, in sequence
    self.visited_shops = []
    
  # Find destination from given origin based on input
  def findLoc(self, origin, dest, alpha):
    # Store snapshot of locHistory and path
    locLog = [origin]
    pathLog = []
      
    # If last city is not goal, search for next city
    while (locLog[-1].category is not dest or locLog[-1] in self.visited_shops):

      if len(pathLog) > 0:
        # Add all roads connected to current city except the one traversed in previous round
        availablePaths = [r for r in locLog[-1].roads if r is not pathLog[-1]]
      else:
        availablePaths = locLog[-1].roads

      # If reached dead end, allow Ant to travel back where it came
      if len(availablePaths) == 0:
        availablePaths = [pathLog[-1]]

      # Calculate probability of choosing each road/edge
      pheromones_alpha = [r.pheromone**alpha for r in availablePaths]
      probabilities = [pa/sum(pheromones_alpha) for pa in pheromones_alpha]

      # Obtain cumulative probabilities
      acc_probabilities = [sum(probabilities[:i+1]) for i,p in enumerate(probabilities)]  

      # Select road
      chosen_value = random.random()
      for ai,ap in enumerate(acc_probabilities):
        if ap > chosen_value:
          break
      # Add selected road to path list
      pathLog.append(availablePaths[ai])  
      # Add city to which new road connects to
      if pathLog[-1].connectedLocs[0] is locLog[-1]:
        locLog.append(pathLog[-1].connectedLocs[1])
      else:
        locLog.append(pathLog[-1].connectedLocs[0])

    # Remove looping paths
    while len(set(locLog)) != len(locLog):
      for i,loc in enumerate(set(locLog)):
        loc_indices = [i for i, x in enumerate(locLog) if x == loc]

        if len(loc_indices) > 1:
          # Remove all locations & paths between first & last occurence of same city
          locLog = locLog[:loc_indices[0]] + locLog[loc_indices[-1]:]
          pathLog = pathLog[:loc_indices[0]] + pathLog[loc_indices[-1]:]
          break
    
    return [locLog, pathLog]
    
  def getPath(self, origin, targetShops, alpha, locations, roads):
    # List of unselected target shops
    remainingDest = targetShops.copy()
    print([dest.name for dest in remainingDest])

    # Append origin to list of traversed locations
    self.locHistory.append(origin)
    self.visited_shops = []

    targetsFound = False
    exitFound = False
    getPathLength = self.getPathLength

    # Continue loop if there are still untraversed destinations
    while (len(remainingDest) != 0 and exitFound == False):
      locAndPos = []
      print("-----------" * 10)

      targetOptions = remainingDest.copy()

      for target in targetOptions:
        locAndPos.append(self.findLoc(self.locHistory[-1], target, alpha))

      minCostPath = min(locAndPos, key=lambda x: getPathLength(x[1]))
      self.locHistory += minCostPath[0][1:]
      self.path += minCostPath[1]

      # print(self.locHistory[-1].name)
      remainingDest.remove(self.locHistory[-1])
      self.visited_shops.append(self.locHistory[-1])
      # print([dest.name for dest in remainingDest])

      # Mark exit as found - triggered only once after all targets found
      if (targetsFound):
        exitFound = True

      # Check if all targets reached
      if (len(remainingDest) == 0 and targetsFound == False):
        targetsFound = True

      # Locate exit 
      if (targetsFound == True and exitFound == False):
        # Identify all possible exits
        remainingDest = ['Opening']

  def getAntPathLength(self):
    return sum([road.cost for road in self.path])
  
  def getPathLength(self, pathList):
    return sum([road.cost for road in pathList])    
  
  def reset(self):
    self.locHistory = []
    self.path = []

  
  
  
  
  def findLocCategory(self, origin, remainingDest, alpha):
    # Store snapshot of locHistory and path
    locLog = [origin]
    pathLog = []
      
    # If last city is not goal, search for next city
    while (locLog[-1] not in remainingDest):

      if len(pathLog) > 0:
        # Add all roads connected to current city except the one traversed in previous round
        availablePaths = [r for r in locLog[-1].roads if r is not pathLog[-1]]
      else:
        availablePaths = locLog[-1].roads

      # If reached dead end, allow Ant to travel back where it came
      if len(availablePaths) == 0:
        availablePaths = [pathLog[-1]]

      # Calculate probability of choosing each road/edge
      pheromones_alpha = [r.pheromone**alpha for r in availablePaths]
      probabilities = [pa/sum(pheromones_alpha) for pa in pheromones_alpha]

      # Obtain cumulative probabilities
      acc_probabilities = [sum(probabilities[:i+1]) for i,p in enumerate(probabilities)]  

      # Select road
      chosen_value = random.random()
      for ai,ap in enumerate(acc_probabilities):
        if ap > chosen_value:
          break
      # Add selected road to path list
      pathLog.append(availablePaths[ai])  
      # Add city to which new road connects to
      if pathLog[-1].connectedLocs[0] is locLog[-1]:
        locLog.append(pathLog[-1].connectedLocs[1])
      else:
        locLog.append(pathLog[-1].connectedLocs[0])

    # Remove looping paths
    while len(set(locLog)) != len(locLog):
      for i,loc in enumerate(set(locLog)):
        loc_indices = [i for i, x in enumerate(locLog) if x == loc]

        if len(loc_indices) > 1:
          # Remove all locations & paths between first & last occurence of same city
          locLog = locLog[:loc_indices[0]] + locLog[loc_indices[-1]:]
          pathLog = pathLog[:loc_indices[0]] + pathLog[loc_indices[-1]:]
          break
    
    return [locLog, pathLog]
  
  
  def getPathCategory(self, origin, targetShops, alpha, locations, roads):
    # List of unselected target shops
    remainingDest = targetShops.copy()
    print("remainingDest", remainingDest)
    # print([dest.name for dest in remainingDest])

    # Append origin to list of traversed locations
    self.locHistory.append(origin)

    targetsFound = False
    exitFound = False
    getPathLength = self.getPathLength

    # Continue loop if there are still untraversed destinations
    while (len(remainingDest) != 0 and exitFound == False):
      locAndPos = []
      print("-----------" * 10)

      targetOptions = remainingDest.copy()

      for target in targetOptions:
        locAndPos.append(self.findLocCategory(self.locHistory[-1], target, alpha))

      minCostPath = min(locAndPos, key=lambda x: getPathLength(x[1]))
      self.locHistory += minCostPath[0][1:]
      self.path += minCostPath[1]

      print(self.locHistory[-1].name)
      remainingDest.remove(self.locHistory[-1])
      print([dest.name for dest in remainingDest])

      # Mark exit as found - triggered only once after all targets found
      if (targetsFound):
        exitFound = True

      # Check if all targets reached
      if (len(remainingDest) == 0 and targetsFound == False):
        targetsFound = True

      # Locate exit 
      if (targetsFound == True and exitFound == False):
        # Identify all possible exits
        remainingDest = [loc for k, loc in locations.items() if loc.__class__.__name__ == 'Opening']
  
  
  
  
  
  # # Find destination from given origin based on input
  # def getPathCategory(self, origin, dList, alpha, locations, roads):
  #   # List of untraversed target shops
  #   remainingDest = dList.copy()

  #   # Append origin to list of traversed locations
  #   locationLog = []  # Track locs leading up to 1 target
  #   visited_shops = [] # Use to keep track of already visited shops. 
  #   locationLog.append(origin)
  #   targetsFound = False
  #   exitFound = False
  #   self.locHistory.append(origin)

  #   # Continue loop if there are still untraversed destinations
  #   while (len(remainingDest) != 0 and exitFound == False):

  #     # If last shop is not goal, search for next shop
  #     # If last shop is already visited, search for next shop
  #     while (locationLog[-1].category not in remainingDest or locationLog[-1] in visited_shops):

  #       if len(self.path) > 0:
  #         # Add all roads connected to current city except the one traversed in previous round
  #         availablePaths = [r for r in locationLog[-1].roads if r is not self.path[-1]]
  #       else:
  #         availablePaths = locationLog[-1].roads

  #       # If reached dead end, allow Ant to travel back where it came
  #       if len(availablePaths) == 0:
  #         availablePaths = [self.path[-1]]

  #       # Calculate probability of choosing each road/edge
  #       pheromones_alpha = [r.pheromone**alpha for r in availablePaths]
  #       probabilities = [pa/sum(pheromones_alpha) for pa in pheromones_alpha]

  #       # Obtain cumulative probabilities
  #       acc_probabilities = [sum(probabilities[:i+1]) for i,p in enumerate(probabilities)]  

  #       # Select road
  #       chosen_value = random.random()
  #       for ai,ap in enumerate(acc_probabilities):
  #         if ap > chosen_value:
  #           break
  #       # Add selected road to path list
  #       self.path.append(availablePaths[ai])  
  #       # Add city to which new road connects to
  #       if self.path[-1].connectedLocs[0] is locationLog[-1]:
  #         locationLog.append(self.path[-1].connectedLocs[1])
  #       else:
  #         locationLog.append(self.path[-1].connectedLocs[0])
          
        

  #     # Remove looping paths
  #     while len(set(locationLog)) != len(locationLog):
  #       for i,loc in enumerate(set(locationLog)):
  #         loc_indices = [i for i, x in enumerate(locationLog) if x == loc]

  #         if len(loc_indices) > 1:
  #           # **** Ignore if loopy path is returning back to walkway from visited store (e.g. E > Acer > E)
  #           # **** Separate locHistory lists for each target location reached ****
            
  #           # Remove all locations & paths between first & last occurence of same city
  #           locationLog = locationLog[:loc_indices[0]] + locationLog[loc_indices[-1]:]
  #           self.path = self.path[:loc_indices[0]] + self.path[loc_indices[-1]:]

  #           break

  #     # Target location found - remove from list, set new origin.
  #     remainingDest.remove(locationLog[-1].category)
  #     visited_shops.append(locationLog[-1])
  
  #     self.locHistory += locationLog[1:]
  #     locationLog = [locationLog[-1]]  # Clear all locs except the last - new origin
          
  #     # Mark exit as found - triggered only once after all targets found
  #     if (targetsFound):
  #       exitFound = True
  #       remainingDest.clear()

  #     # Check if all targets reached
  #     if (len(remainingDest) == 0 and targetsFound == False):
  #       targetsFound = True
  #       self.path.clear()  # Reset path

  #     # Locate exit 
  #     if (targetsFound == True and exitFound == False):
  #       # Identify all possible exits
  #       remainingDest = ['Opening']

  
  
  # Find destination from given origin based on input
  # def get_path(self, origin, dList, alpha, locations, roads):
  #   # List of untraversed target shops
  #   remainingDest = dList.copy()

  #   # Append origin to list of traversed locations
  #   # self.locHistory.append(origin)
  #   locationLog = []  # Track locs leading up to 1 target
  #   locationLog.append(origin)
  #   targetsFound = False
  #   exitFound = False
  #   self.locHistory.append(origin)

  #   # **** Add to locationLog immediately if adjacent loc is target ****

  #   # Continue loop if there are still untraversed destinations
  #   while (len(remainingDest) != 0 and exitFound == False):

  #     # If last city is not goal, search for next city
  #     while (locationLog[-1] not in remainingDest):

  #       if len(self.path) > 0:
  #         # Add all roads connected to current city except the one traversed in previous round
  #         availablePaths = [r for r in locationLog[-1].roads if r is not self.path[-1]]
  #       else:
  #         availablePaths = locationLog[-1].roads

  #       # If reached dead end, allow Ant to travel back where it came
  #       if len(availablePaths) == 0:
  #         availablePaths = [self.path[-1]]

  #       # Calculate probability of choosing each road/edge
  #       pheromones_alpha = [r.pheromone**alpha for r in availablePaths]
  #       probabilities = [pa/sum(pheromones_alpha) for pa in pheromones_alpha]

  #       # Obtain cumulative probabilities
  #       acc_probabilities = [sum(probabilities[:i+1]) for i,p in enumerate(probabilities)]  

  #       # Select road
  #       chosen_value = random.random()
  #       for ai,ap in enumerate(acc_probabilities):
  #         if ap > chosen_value:
  #           break
  #       # Add selected road to path list
  #       self.path.append(availablePaths[ai])  
  #       # Add city to which new road connects to
  #       if self.path[-1].connectedLocs[0] is locationLog[-1]:
  #         locationLog.append(self.path[-1].connectedLocs[1])
  #       else:
  #         locationLog.append(self.path[-1].connectedLocs[0])

  #     # Remove looping paths
  #     while len(set(locationLog)) != len(locationLog):
  #       for i,loc in enumerate(set(locationLog)):
  #         loc_indices = [i for i, x in enumerate(locationLog) if x == loc]

  #         if len(loc_indices) > 1:
  #           # **** Ignore if loopy path is returning back to walkway from visited store (e.g. E > Acer > E)
  #           # **** Separate locHistory lists for each target location reached ****

  #           # print("Loopy path removed")
  #           # print(f"Original: {locList(locationLog)}")

  #           # Remove all locations & paths between first & last occurence of same city
  #           locationLog = locationLog[:loc_indices[0]] + locationLog[loc_indices[-1]:]
  #           self.path = self.path[:loc_indices[0]] + self.path[loc_indices[-1]:]

  #           # print(f"Removed: {locList(locationLog)}")
  #           # print()

  #           break
      
  #     # print("-----" * 20)

  #     # Target location found - remove from list, set new origin.
  #     remainingDest.remove(locationLog[-1])
  #     # print(locList(locationLog[1:]))
  #     self.locHistory += locationLog[1:]
  #     locationLog = [locationLog[-1]]  # Clear all locs except the last - new origin
     
  #     # self.path.clear()  # Reset path
  #     # for r in roads:   # Reset pheromones
  #     #     r.set_pheromone(0.01)

  #     # Mark exit as found - triggered only once after all targets found
  #     if (targetsFound):
  #       exitFound = True
  #       remainingDest.clear()

  #     # Check if all targets reached
  #     if (len(remainingDest) == 0 and targetsFound == False):
  #       targetsFound = True
  #       self.path.clear()  # Reset path
  #       for r in roads:   # Reset pheromones
  #         r.set_pheromone(0.01)

  #     # Locate exit 
  #     if (targetsFound == True and exitFound == False):
  #       # Identify all possible exits
  #       remainingDest = [loc for k, loc in locations.items() if loc.__class__.__name__ == 'Entrance']
