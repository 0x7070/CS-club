def near_hundred(n):
  return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)
  # abs(89-100) = 11 -> 11>10, so False
  # abs(93-100) = 7  ->  7<10, so True 
