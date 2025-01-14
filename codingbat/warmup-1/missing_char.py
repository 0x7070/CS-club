def missing_char(str, n):
  return str[:n] + str[n+1:]
  # str[:] -> "index slicing"
  # str[:n] -> from the beginning of the string until the character at index `n`
  # str[n+1:] -> skip the character at index `n`, and proceed from the next index
