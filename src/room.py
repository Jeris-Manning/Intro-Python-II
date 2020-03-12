# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description
  def describe(self):
    print(self.description, "\n")
  def __repr__(self):
    return (f'{self.__class__.__name__}('
               f'{self.name!r}, {self.description!r})')