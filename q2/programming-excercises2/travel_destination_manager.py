import time
destinations = ['Cebu', 'Manila', 'Davao', 'Baguio', 'Palawan']
print("Here are the destinations available:")
for place in destinations[0:4]:
  print(place)
  time.sleep(0.3)
travel = input(str("Please input a destination: "))
travel.capitalize()
if travel in destinations:
  print("This destination exists in the list.")
else:
  print("This destination does not exist on the list.")
destinations[2] = 'Iloilo'
print("Here is the updated list of the destinations available:")
for place in destinations:
  print(place)
  time.sleep(0.3)
