import random

class Ant:
  def __init__(self):
    self.locHistory = []    # Locations the ant passes through, in sequence
    self.path = []      # Roads the ant uses, in sequence
    
  # Find destination from given origin based on input
  def get_path(self, origin, dList, alpha, locations, roads):
    # List of untraversed target shops
    remainingDest = dList.copy()

    # Append origin to list of traversed locations
    # self.locHistory.append(origin)
    locationLog = []  # Track locs leading up to 1 target
    locationLog.append(origin)
    targetsFound = False
    exitFound = False
    self.locHistory.append(origin)

    # **** Add to locationLog immediately if adjacent loc is target ****

    # Continue loop if there are still untraversed destinations
    while (len(remainingDest) != 0 and exitFound == False):

      # If last city is not goal, search for next city
      while (locationLog[-1] not in remainingDest):

        if len(self.path) > 0:
          # Add all roads connected to current city except the one traversed in previous round
          availablePaths = [r for r in locationLog[-1].roads if r is not self.path[-1]]
        else:
          availablePaths = locationLog[-1].roads

        # If reached dead end, allow Ant to travel back where it came
        if len(availablePaths) == 0:
          availablePaths = [self.path[-1]]

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
        self.path.append(availablePaths[ai])  
        # Add city to which new road connects to
        if self.path[-1].connectedLocs[0] is locationLog[-1]:
          locationLog.append(self.path[-1].connectedLocs[1])
        else:
          locationLog.append(self.path[-1].connectedLocs[0])

      # Remove looping paths
      while len(set(locationLog)) != len(locationLog):
        for i,loc in enumerate(set(locationLog)):
          loc_indices = [i for i, x in enumerate(locationLog) if x == loc]

          if len(loc_indices) > 1:
            # **** Ignore if loopy path is returning back to walkway from visited store (e.g. E > Acer > E)
            # **** Separate locHistory lists for each target location reached ****

            # print("Loopy path removed")
            # print(f"Original: {locList(locationLog)}")

            # Remove all locations & paths between first & last occurence of same city
            locationLog = locationLog[:loc_indices[0]] + locationLog[loc_indices[-1]:]
            self.path = self.path[:loc_indices[0]] + self.path[loc_indices[-1]:]

            # print(f"Removed: {locList(locationLog)}")
            # print()

            break
      
      # print("-----" * 20)

      # Target location found - remove from list, set new origin.
      remainingDest.remove(locationLog[-1])
      # print(locList(locationLog[1:]))
      self.locHistory += locationLog[1:]
      locationLog = [locationLog[-1]]  # Clear all locs except the last - new origin
     
      # self.path.clear()  # Reset path
      # for r in roads:   # Reset pheromones
      #     r.set_pheromone(0.01)

      # Mark exit as found - triggered only once after all targets found
      if (targetsFound):
        exitFound = True
        remainingDest.clear()

      # Check if all targets reached
      if (len(remainingDest) == 0 and targetsFound == False):
        targetsFound = True
        self.path.clear()  # Reset path
        for r in roads:   # Reset pheromones
          r.set_pheromone(0.01)

      # Locate exit 
      if (targetsFound == True and exitFound == False):
        # Identify all possible exits
        remainingDest = [loc for k, loc in locations.items() if loc.__class__.__name__ == 'Entrance']

  def get_path_length(self):
    return sum([road.cost for road in self.path])    
  
  def reset(self):
    self.locHistory = []
    self.path = []
    