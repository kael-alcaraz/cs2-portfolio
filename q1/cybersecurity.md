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

# Part C: Program Implementation
## Programming Language
> Python
## Source Code File
> [`workshop-validator.py`](workshop-validator.py)
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
print("=============================================================")```

---

## Validation Techniques Used

### Presence Validation
> Name and email validators.

### Data Type Validation
> Age and grade validators.

### Range Validation
> Age and grade validators.

### Acceptable Value Validation
> Age and Grade validators.

### Pattern Validation
> The string must contain "@".
> Email validators.

### Length Validation
> The length must be 6.
> Registration code validators.

# Part D - Testing
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case |Registration end message|Registration end message| PASS |
| 2 | Blank student name | Presence |Fail message/invalid message/end message|Fail message/invalid message/end message| PASS |
| 3 | Age = `fourteen` | Data type | Fail message/invalid message/end message | Fail message/invalid message/end message | PASS |
| 4 | Age = `11` | Minimum boundary | Success message | Success message | PASS |
| 5 | Age = `18` | Maximum boundary | Success message | Success message | PASS |
| 6 | Age = `10` | Range | Fail message/invalid message/end message | Fail message/invalid message/end message | PASS |
| 7 | Grade Level = `13` | Acceptable value | Fail message/invalid message/end message | Fail message/invalid message/end message | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Fail message/invalid message/end message | Fail message/invalid message/end message | PASS |
| 9 | Registration Code = `ABC` | Length | Fail message/invalid message/end message | Fail message/invalid message/end message | PASS |
| 10 | Registration Code = `CS2026` | Valid length | Success message | Success message | PASS |

---

# Part E: Output Verification

## Verification Test 1
**INPUT**
``` text
student.pshs.edu.ph
```
**EXPECTED OUTPUT**
``` text
"Pip-tan: 'Whoops! That is not a valid e-mail address. Goodbye!'"
```
**ACTUAL OUTPUT**
``` text
"Pip-tan: 'Whoops! That is not a valid e-mail address. Goodbye!'"
```
**Result:** **PASS**
**EXPLANATION**
> It passed, as the expectations met reality. It passed because the rule of having "@" in the sentence prevented it from success.

## Verification Test 2
**INPUT**
``` text
13
```
**EXPECTED OUTPUT**
``` text
"Pip-tan: 'Whoops! That is not a valid grade level. Goodbye!'"
```
**ACTUAL OUTPUT**
``` text
"Pip-tan: 'Whoops! That is not a valid grade level. Goodbye!'"
```
**Result:** **PASS**
**EXPLANATION**
> It passed, as the expectations met reality. It passed, as the range only goes up to 12, which means 13 is excluded.

## Verification Test 3
**INPUT**
``` text
fourteen
```
**EXPECTED OUTPUT**
``` text
"Pip-tan: 'Whoops! That is not a valid age. Goodbye!'"
```
**ACTUAL OUTPUT**
``` text
"Pip-tan: 'Whoops! That is not a valid age. Goodbye!'"
```
**Result:** **PASS**
**EXPLANATION**
> It passed, as the expectations met reality. It passed, as the datatype stored is an integer, and since "fourteen" is a string, it didn't pass through.

---

# Reflection

### 1. Why should a program validate input before processing it?
> So that it is easier to process, and that there are no uncesessary information left.

### 2. What is the difference between input validation and output verification?
> Input validation makes sure the output is correct, and output verification is to make sure the input is correct.

### 3. Which validation technique was easiest for you to implement? Why?
> The length validation technique, as it already exists as the function len().

### 4. Which validation technique was most challenging? Why?
> The presence technique but for the name, as it required a nested if statement.

### 5. How did testing invalid inputs help you improve your program?
> It showed me what inputs were going wrong, and to fix it, to improe the work.

---

# Files for this activity
- [`workshop-validator.py`](workshop-validator.py)
- `input-validation.md`

---

# [←-- psst, here's a link to go back to the main portfolio](../README.md)