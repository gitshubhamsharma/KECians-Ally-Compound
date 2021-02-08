import json

def room_check(num, arr, dept):
    """
    It checks whether the room can be booked if it does not lie in the given timeframe.
    """
    if num in range(arr, dept):
        return True
    else:
        return False

def validate_input(choice, choice1):
  """
  Validate Input of Arrival and Departure
  """

  acceptable_range = range(0, 24)
  if int(choice) in acceptable_range and int(choice1) in acceptable_range:
   return True
  else:
   return False

class UserDB:
  def __init__(self):
    self.__data = None

  def connect(self, data_file):
    with open(data_file) as json_file:
      self.__data = json.load(json_file)

  def get_data(self, name):
    for user in self.__data['Users']:
      if user['Name'] == name:
        return user

  def close(self):
      pass
