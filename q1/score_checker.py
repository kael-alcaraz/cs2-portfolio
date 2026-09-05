import time
import random
import math

randnum1 = random.uniform(1, 5)
randnum2 = random.uniform(1, 5)

print("Pip-tan: 'Welcome! Let me get things set up for you.'")
print("=======================================================")
# The time.sleep(x) is more for aesthetic than it serves a technical purpose, because it makes a loading screen effect.
time.sleep(0.5)
print()
time.sleep(0.5)
print("Loading...")
time.sleep(randnum1)
print(f"Done! [Loaded for {math.ceil(randnum1)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=======================================================")
time.sleep(0.5)

score = int(input("Pip-tan: 'Hey! It's me, Pip-tan, your score assistant. Give me your score, and I'll classify it:'  "))
if not (0 <= score <= 100):
#This validates the range of the scores.
  print("Pip-tan: 'Whoops! That isn't a valid score.' ")
elif score >= 90:
  print(f"Pip-tan: 'Woah! That's an outstanding score of {score}. Keep it up!'")
elif score >= 80:
  print(f"Pip-tan: 'Yay! That's a very satisfactory score of {score}. Keep it up!'")
elif score >= 75:
  print(f"Pip-tan: 'Great! That's a satisfactory score of {score}. Keep it up!'")
else:
  print(f"Pip-tan: 'Oh no... that's a score of {score} that needs some improvement. Please do get your scores up, please?'")
# This is the full, complete classification system.
time.sleep(0.5)

print("=============================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Tidying up...")
time.sleep(randnum2)
print(f"Done! [Tidied up for {math.ceil(randnum2)} se-")
print("Pip-tan: 'Wait!'")
time.sleep(0.5)
print("Pip-tan: 'Goodbye, and thank you for using the Score Checker! <3'")
time.sleep(0.5)
print("Tidying up... (again)")
time.sleep(randnum2)
print(f"Done! [Tidied up for {math.ceil(randnum2)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=============================================================")
# Again, another final loading screen, purely for aesthetic.
