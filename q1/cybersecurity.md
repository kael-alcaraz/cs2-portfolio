# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System
**Name:** Kael Dominic V. Alcaraz
**Section:** 8-Dahlia
**Quarter:** 1

---

## Activity Overview:
In this activity, I created a program that captures information for a PSHS Club registration.
It identifies if inputs are necessary and correct.

---

# Part A - Cybersecurity Threat Analysis
## Assigned Case
### **Case Number:** 2
### **Case Title:** Fake Prize
> A student supposedly wins a prize, yet they must provide personal and payment info.

<hr width="15%">

### 1. What cybersecurity threat is shown?
> The cybersecurity threat is Phishing.

### 2. What warning signs make the situation suspicious?
> Asking for personal and financial details.

### 3. What may be affected?
Check all that apply:
- Data (✓)
- Account
- Application
- Device
- Network
- Financial info (✓)
> Phishing scams only want your data for marketing, and your financial data for getting money out of it.

### 4. What information could be exposed or misused?
> Financial and personal.

### 5. What should the user do to reduce the risk?
> Do not click on links that are suspicious, and do not imput private information.

---

# Part B


| Data | Collect/Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | The club needs to know who the person is. |
| Section | Collect | The club needs to search for the person, and in the section is best. |
| Club Choice | Collect | The system needs to know what club the student wants to join. |
| Email Address | Collect | For easy contact. |
| Attendance status | Collect | To know whether or not the student was  actually there. |
| Password | Do not Collect | The system does not need to log in to the person's email. |
| OTP | Do not Collect | The system does not need an OTP to log in, thus deeming this unnecessesary. |
| Home Address | Do not Collect | A club does not need to know where a  student goes home to. |
| Parent Bank Account | Do not Collect | The system does not need to know where a student gets money from. |

<hr width="15%">

## Privacy Question
### Why is it safer to collect only information that the program actually needs?
> Because it is easier to deter attackers when the progam gives data not much needed.

---

# Part C: Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error
Message |
|---:|---|---|---|---|---|
| Student Name | Anything with characters | None | " " | There must be a character in the input | Pip-tan: 'Whoops! That isn't a valid name. Goodbye!' |
| Section | A section in the list of sections | None | Kamia | The input must be in the list "sectionlist." | Pip-tan: 'Whoops! That entry, {section}, is not a valid section. Goodbye!' |
| Club Choice | A club in the list of clubs given | There may be other clubs to be put, yet the only ones provided are counted. | Gaming | The input must be in the list "clublist." | Pip-tan: 'Whoops! That entry, {club}, is not a valid club. Goodbye!' |
| School Email | An email with the characters "@" and "." | None | student.pshs.brc | Input must have the characters "@" and "." | Pip-tan: 'Whoops! That entry, {email}, is not a valid e-mail address. Goodbye!' |
| Attendance Status | A status in the list of attendance statuses | None | Gone | Input must be in the list "attstatlist." | Pip-tan: 'Whoops! That entry, {attendance}, is not a valid attendance status. Goodbye!' |

<hr width="15%">

## Secure Data Capture Questions

### 1. What should your program accept?
> Valid, correct, necessary answers.

### 2. What should your program reject?
> Invalid, wrong, unnecessaty answers.

### 3. How do your validation rules help reduce incorrect and unsafe input?
>By putting strict rules on what is to be inputted.

---

# Part D: Secure Program Implementation
## Programming Language
> Python
## Source Code File
> [`secure_registration.py`](secure_registration.py)
## Final Code
``` python
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
        print(f"Pip-tan: 'Whoops! That entry, {section}, is not a valid section. Goodbye!'")
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
print("=============================================================")```

---

## Security Practices Applied

### Required Input
> Using .strip() to scan for blank inputs.

### Allowed Values
> Section, Club, and Attendance Status validators.

### Format Check
> Using if "@" not in email and "." not in email.

### Error Messages
> So that we know where you went wrong.

### Data Minimization
> OTPs, Passwords, Home adresses, bank accounts.
> These are unnecessary and personal. Better not to use such as it would make it more suspicious

---

# Part E - Testing and Reflection
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | Registered message | Registered message | **PASS** |
| 2 | Blank student name | Error message | Error message | **PASS** |
| 3 | Invalid section | Error message | Error message | **PASS** |
| 4 | Invalid club choice | Error message | Error message | **PASS** |
| 5 | Email missing `@` | Error message | Error message | **PASS** |
| 6 | Email missing `.` | Error message | Error message | **PASS** |
| 7 | Invalid attendance status | Error message | Error message | **PASS** |
| 8 | Different valid inputs | Registered message | Registered message | **PASS** |

<hr width="15%">

# Reflection

### 1. What is one cybersecurity threat that can affect an application or user?
> Phishing is an example of a cybersecurity threat that affects users.

### 2. How can users reduce the risk of phishing or suspicious messages?
> Not clicking on suspicous links and not interacting with suspicious internet items.

### 3. How can validation rules improve the security of user input?
> It dfends extra because the inputs are from small sets that are not known to users.

### 4. Why should a aprogram avoid collecting unnecessary personal information?
> To make the digital world a safer place, and to defend personal information more by not sharing it outside.

### 5. How SG7's input validation concepts become security practices in SG8?
> Input validation is very good as security, as it provides small sets to work on. Removing incorrect or invalid information makes a program more secure.

---

# Files for this activity
- [`secure_registration.py`](secure_registration.py)
- `cybersecurity.md`

---

# [←-- psst, here's a link to go back to the main portfolio](../README.md)