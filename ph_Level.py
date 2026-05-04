ph=int(input('Enter a ph Value (0-14):'))
if ph>7:
  print('Basic')
elif ph<7:
  print('Acid')
else:
  print('Neutral')
