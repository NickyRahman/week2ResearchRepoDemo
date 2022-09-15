#Cat and Dog Program

def callPET():
  petName = input('Type in CAT or DOG : ')
  
  if petName == 'CAT':
    print('Meow')
  if petName == 'DOG':
    print('Woof, woof')
  if petName != 'CAT' or petName!= 'DOG':
    print ('Input must be CAT or DOG')
    callPET()

# press Ctrl + forward slash(/) to add or remove comment symbol (#)
# press Ctrl+C to quit previous program


# ----------------
# I did another quick exercise using a slightly different re-call function **else**
# ----------------
def petCalling():
  petName = input('Type in BIRD or RABBIT : ')
  
  if petName == 'BIRD':
    print('chirp')
  if petName == 'RABBIT':
    print('Squeak')
  else:
    print('Input must be BIRD or RABBIT')
    petCalling()

petCalling()
