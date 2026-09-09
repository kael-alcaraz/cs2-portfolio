import time
import random
import math

# Variables needed for loadtime

randnum1 = random.uniform(1, 5)
randnum2 = random.uniform(1, 5)
randnum3 = random.uniform(1, 5)

# Initial Loading Screen

print("Pip-tan: 'Hey! Welcome back! Let me get things set up for you.'")
print("=======================================================")
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

# Block 1: Name

name = input("Pip-tan: 'So, what's your name?' ")
time.sleep(0.5)
if not name.strip():
  print("Pip-tan: 'Whoops! That isn't a valid name.'")
else:
  print("Pip-tan: 'Great!'")
time.sleep(0.5)

# Block 2: Age

age = str(input("Pip-tan: 'Now, what's your age?' "))
if age.isdigit():
    age = int(age)
    if age < 11 or age > 18:
        print("Pip-tan: Whoops! That is not a valid age.")
    else:
        print("Pip-tan: Great!")
else:
    print("Pip-tan: 'Whoops! That is not a valid age.'")
time.sleep(0.5)

# Block 3: Grade

grade = int(input("Pip-tan: 'Now, what grade are you in?' "))
if grade < 7 or grade > 12:
  print("Pip-tan: 'Whoops! That is not a valid grade.'")
else:
  print("Pip-tan: 'Great!'")
time.sleep(0.5)

# Block 4: Email

email = input("Pip-tan: 'Now, what's your e-mail address?' ")
if "@" in email:
  print("Pip-tan: 'Great!'")
else:
  print("Pip-tan: 'Whoops! That is not a valid e-mail address.'")
time.sleep(0.5)

# Block 5: Registration Code

code = input("Pip-tan: 'Now, what's your registation code?' ")
if len(code) == 6:
  print("Pip-tan: 'Great!'")
else:
  print("Pip-tan: 'Whoops! That is not a valid registration code.'")

# The following code is the validation determiner system.

has_invalid_input = False
if not len(code) == 6:
    has_invalid_input = True
if int(age) < 11 or int(age) > 18:
    has_invalid_input = True
if int(grade) < 7 or int(grade) > 12:
    has_invalid_input = True
if not str(name) == name.strip():
    has_invalid_input = True
if "@" not in str(email):
    has_invalid_input = True
time.sleep(1)

# Second Loading screen

print("=======================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Loading...")
time.sleep(randnum2)
print(f"Done! [Loaded for {math.ceil(randnum2)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=======================================================")
time.sleep(0.5)

# Determiner output

if has_invalid_input:
    print("Pip-tan: 'Registration failed. One or more inputs were invalid.'")
else:
  print(f"""======================
REGISTRATION ACCEPTED!
======================""")
  time.sleep(0.5)
  print(f"Name: {name}")
  time.sleep(0.5)
  print(f"Age: {age}")
  time.sleep(0.5)
  print(f"Grade Level: {grade}")
  time.sleep(0.5)
  print(f"Email: {email}")
  time.sleep(0.5)
  print(f"Registration Code: {code}")
time.sleep(1)

#Final clearing screen

print("=============================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Tidying up...")
time.sleep(randnum3)
print(f"Done! [Tidied up for {math.ceil(randnum3)} se-")
print("Pip-tan: 'Wait!'")
time.sleep(0.5)
print("Pip-tan: 'Goodbye, and thank you for using the Workshop Registration Validation site! <3'")
time.sleep(0.5)
print("Tidying up... (again)")
time.sleep(randnum2)
print(f"Done! [Tidied up for {math.ceil(randnum3)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=============================================================")
