def parrot_trouble(talking, hour):
  if talking:
    if hour < 7 or hour > 20:
      return True
      
  return False

# since we would `return` if all of the first if statement is True, we do not need to explicitly add a return False there.
# instead, we can just put a `return False` at the end of the code.
