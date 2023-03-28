class Flower:
  def __init__(self, petals, whorls, stamens):
    self.petals = petals
    self.whorls = whorls
    self.stamens = stamens
    
  def grow(self, n):
    for i in range(n):
      self.petals = self.apply_rules(self.petals)
      self.whorls = self.apply_rules(self.whorls)
      self.stamens = self.apply_rules(self.stamens)
  
  def apply_rules(self, components):
    new_components = []
    for component in components:
      if component == "P":
        new_components.append("PP")
      elif component == "W":
        new_components.append("WW")
      elif component == "S":
        new_components.append("SS")
      else:
        new_components.append(component)
    return new_components

# Define initial components of the flower
petals = ["P"]
whorls = ["W"]
stamens = ["S"]

# Create a new flower object
flower = Flower(petals, whorls, stamens)

# Apply L-system rules to grow the flower
flower.grow(3)
