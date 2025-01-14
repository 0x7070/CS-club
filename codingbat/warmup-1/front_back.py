def front_back(str): # "duck"
  if len(str) <= 1: # * this is required as index slicing will not work on empty strings
    return str # false
  else:
    front = str[0] # "d"
    back = str[-1] # "k"
    #         "k"    "uc"        "d"
    new_str = back + str[1:-1] + front
    return new_str # "kucd"

