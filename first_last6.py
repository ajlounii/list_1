def extra_end(str):
  sum=""
  for i in range(3):
    o=str[len(str)-2:len(str)]
    sum=sum+o
  return sum
