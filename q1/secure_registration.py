import time
import random
import math
import sys

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
if name.strip() == "quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
time.sleep(0.5)
if not name.strip():
  print("Pip-tan: 'Whoops! That isn't a valid name. Goodbye!'")
  sys.exit(1)
else:
  print("Pip-tan: 'Great!'")
time.sleep(0.5)

# Block 2: Section

section = str(input("Pip-tan: 'Now, what's your section?' ")).capitalize()
sectionlist = ["Diamond", "Emerald", "Jade", "Sapphire", "Dahlia", "Ilang-Ilang", "Rosal", "Sampaguita", "Beryllium", "Magnesium", "Platinum", "Silicon", "Electron", "Gluon", "Graviton", "Photon", "Biology", "Biochemistry", "Chemistry", "Physics"]
if section.strip() == "quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
if section not in sectionlist:
        print(f"Pip-tan: Whoops! That entry, {section}, is not a valid section. Goodbye!")
        sys.exit(1)
else:
        print("Pip-tan: Great!")
time.sleep(0.5)

# Block 3: Club

club = input("Pip-tan: 'Now, what club do you want to join?' ").capitalize()
clublist = ["Robotics", "Science", "Mathematics", "Programming"]
if club.strip() == "quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
# Safely handle the conversion to avoid internal crashes on bad inputs

if club not in clublist:
  print(f"Pip-tan: 'Whoops! That entry, {club}, is not a valid club. Goodbye!'")
  sys.exit(1)
else:
  print("Pip-tan: 'Great!'")
time.sleep(0.5)

# Block 4: Email

email = input("Pip-tan: 'Now, what's your e-mail address?' ")
if email.strip() == ".quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
if "@" in email and "." in email:
  print("Pip-tan: 'Great!'")
else:
  print(f"Pip-tan: 'Whoops! That entry, {email}, is not a valid e-mail address. Goodbye!'")
  sys.exit(1)
time.sleep(0.5)

# Block 5: Attendance Status

attendance = input("Pip-tan: 'Now, what's your attendance status?' ").capitalize()
attstatlist = ["Present", "Absent", "Late"]
if attendance.strip() == "quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
if attendance in attstatlist:
  print("Pip-tan: 'Great!'")
else:
  print(f"Pip-tan: 'Whoops! That entry, {attendance}, is not a valid attendance status. Goodbye!'")
  sys.exit(1)

# The following code is the validation determiner system.

has_invalid_input = False
if club not in clublist:
    has_invalid_input = True
if attendance not in attstatlist:
    has_invalid_input = True
if section not in sectionlist:
    has_invalid_input = True
if not str(name) == name.strip():
    has_invalid_input = True
if "@" not in str(email) and "." not in str(email):
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
  print(f"Section: {section}")
  time.sleep(0.5)
  print(f"Club: {club}")
  time.sleep(0.5)
  print(f"Email: {email}")
  time.sleep(0.5)
  print(f"Attendance: {attendance}")
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
print("Pip-tan: 'Goodbye, and thank you for using the Club Registration site! <3'")
time.sleep(0.5)
print("Tidying up... (again)")
time.sleep(randnum2)
print(f"Done! [Tidied up for {math.ceil(randnum3)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=============================================================")