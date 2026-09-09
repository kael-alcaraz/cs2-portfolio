# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator
**Name:** Kael Dominic V. Alcaraz
**Section:** 8-Dahlia
**Quarter:** 1

---

## Activity Overview:
In this activity, I created a program that validates information for a PSHS Workshop registration.
It identifies if inputs meet specific requirements.
The program validates:
- name
- age
- grade level
- email address
- registration code

---

# Part A


| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name |Non-empty string|Presence check|" "|There should be the presence of a character|"Pip-tan: 'Whoops! That's an invalid name. Goodbye!'"|
| Age |Whole number between 11 and 18|Range check/Type check|36|A whole number that is >= 11 yet <= 18.|"Pip-tan: 'Whoops! That's an invalid age. Goodbye!'" |
| Grade Level |Whole number between 7 and 12 |Range check/type check |21 |A whole number that is >= 7 yet <= 12|"Pip-tan: 'Whoops! That's an invalid grade level. Goodbye!'" |
| Email Address |Any string containing the character "@" |Presence check |kdvalcaraz.brc.pshs.edu.ph |Must contain the character "@" |"Pip-tan: 'Whoops! That's an invalid e-mail address. Goodbye!'" |
| Registration Code |Must be a 6 character long item |Length check | comsci2026 | The length of the character must = 6 |"Pip-tan: 'Whoops! That's an invalid registration code. Goodbye!'" |

---

## Validation Questions
### 1. Why should the student name not be blank?
> Because there are no names that do not contain a character in them.
### 2. Why should age be checked for both data type and range?
> Because it is hard to calculate decimal age, and there is only a select range of ages that is permitted to attend Pisay.
### 3. Why should grade level only accept specific values?
> The Pisay curriculum contains only grades 7 to 12; nothing more, nothing less.
### 4. What format requirements did you use for the email address?
> The format requirement is for the string to contain the character "@"
### 5. What length requirement did you use for the registration code?
> 6 characters length only.

---

# Part B: Program Design
## Pseudocode
``` text
START
 // Initialization
SET randnum1 TO RANDOM_FLOAT(1, 5)
SET randnum2 TO RANDOM_FLOAT(1, 5)
SET randnum3 TO RANDOM_FLOAT(1, 5)

// Initial Loading Screen
OUTPUT "Pip-tan: 'Hey! Welcome back! Let me get things set up for you.'"
OUTPUT "======================================================="
DELAY 0.5 seconds
OUTPUT ""
DELAY 0.5 seconds
OUTPUT "Loading..."
DELAY randnum1 seconds
OUTPUT "Done! [Loaded for " + CEIL(randnum1) + " seconds.]"
DELAY 0.5 seconds
OUTPUT ""
DELAY 0.5 seconds
OUTPUT "======================================================="
DELAY 0.5 seconds

// Block 1: Name
OUTPUT "Pip-tan: 'So, what's your name?' "
INPUT name

IF TRIM(name) EQUALS ".quit" THEN
    OUTPUT "Pip-tan: 'Goodbye!'"
    TERMINATE PROGRAM
ENDIF

DELAY 0.5 seconds
IF TRIM(name) IS EMPTY THEN
    OUTPUT "Pip-tan: 'Whoops! That isn't a valid name. Goodbye!'"
    TERMINATE PROGRAM WITH ERROR
ELSE
    OUTPUT "Pip-tan: 'Great!'"
ENDIF
DELAY 0.5 seconds

// Block 2: Age
OUTPUT "Pip-tan: 'Now, what's your age?' "
INPUT age_input

IF TRIM(age_input) EQUALS ".quit" THEN
    OUTPUT "Pip-tan: 'Goodbye!'"
    TERMINATE PROGRAM
ENDIF

IF IS_NUMERIC(age_input) THEN
    SET age TO CONVERT_TO_INTEGER(age_input)
    IF age < 11 OR age > 18 THEN
        OUTPUT "Pip-tan: Whoops! That is not a valid age. Goodbye!"
        TERMINATE PROGRAM WITH ERROR
    ELSE
        OUTPUT "Pip-tan: Great!"
    ENDIF
ELSE
    OUTPUT "Pip-tan: 'Whoops! That is not a valid age. Goodbye!'"
    TERMINATE PROGRAM WITH ERROR
ENDIF
DELAY 0.5 seconds

// Block 3: Grade
OUTPUT "Pip-tan: 'Now, what grade are you in?' "
INPUT grade_input

IF TRIM(grade_input) EQUALS ".quit" THEN
    OUTPUT "Pip-tan: 'Goodbye!'"
    TERMINATE PROGRAM
ENDIF

IF IS_NUMERIC(grade_input) THEN
    SET grade TO CONVERT_TO_INTEGER(grade_input)
ELSE
    SET grade TO 0
ENDIF

IF grade < 7 OR grade > 12 THEN
    OUTPUT "Pip-tan: 'Whoops! That is not a valid grade. Goodbye!'"
    TERMINATE PROGRAM WITH ERROR
ELSE
    OUTPUT "Pip-tan: 'Great!'"
ENDIF
DELAY 0.5 seconds

// Block 4: Email
OUTPUT "Pip-tan: 'Now, what's your e-mail address?' "
INPUT email

IF TRIM(email) EQUALS ".quit" THEN
    OUTPUT "Pip-tan: 'Goodbye!'"
    TERMINATE PROGRAM
ENDIF

IF email CONTAINS "@" THEN
    OUTPUT "Pip-tan: 'Great!'"
ELSE
    OUTPUT "Pip-tan: 'Whoops! That is not a valid e-mail address. Goodbye!'"
    TERMINATE PROGRAM WITH ERROR
ENDIF
DELAY 0.5 seconds

// Block 5: Registration Code
OUTPUT "Pip-tan: 'Now, what's your registration code?' "
INPUT code

IF TRIM(code) EQUALS ".quit" THEN
    OUTPUT "Pip-tan: 'Goodbye!'"
    TERMINATE PROGRAM
ENDIF

IF LENGTH(code) EQUALS 6 THEN
    OUTPUT "Pip-tan: 'Great!'"
ELSE
    OUTPUT "Pip-tan: 'Whoops! That is not a valid registration code. Goodbye!'"
    TERMINATE PROGRAM WITH ERROR
ENDIF

// Global Validation Determiner System
SET has_invalid_input TO FALSE

IF LENGTH(code) NOT EQUALS 6 THEN
    SET has_invalid_input TO TRUE
ENDIF

IF age < 11 OR age > 18 THEN
    SET has_invalid_input TO TRUE
ENDIF

IF grade < 7 OR grade > 12 THEN
    SET has_invalid_input TO TRUE
ENDIF

IF name NOT EQUALS TRIM(name) THEN
    SET has_invalid_input TO TRUE
ENDIF

IF email DOES NOT CONTAIN "@" THEN
    SET has_invalid_input TO TRUE
ENDIF

DELAY 1 second

// Second Loading Screen
OUTPUT "======================================================="
DELAY 0.5 seconds
OUTPUT ""
DELAY 0.5 seconds
OUTPUT "Loading..."
DELAY randnum2 seconds
OUTPUT "Done! [Loaded for " + CEIL(randnum2) + " seconds.]"
DELAY 0.5 seconds
OUTPUT ""
DELAY 0.5 seconds
OUTPUT "======================================================="
DELAY 0.5 seconds

// Registration Determiner Output
IF has_invalid_input THEN
    OUTPUT "Pip-tan: 'Registration failed. One or more inputs were invalid.'"
ELSE
    OUTPUT "======================"
    OUTPUT "REGISTRATION ACCEPTED!"
    OUTPUT "======================"
    DELAY 0.5 seconds
    OUTPUT "Name: " + name
    DELAY 0.5 seconds
    OUTPUT "Age: " + age
    DELAY 0.5 seconds
    OUTPUT "Grade Level: " + grade
    DELAY 0.5 seconds
    OUTPUT "Email: " + email
    DELAY 0.5 seconds
    OUTPUT "Registration Code: " + code
ENDIF
DELAY 1 second

// Final Clearing Screen
OUTPUT "============================================================="
DELAY 0.5 seconds
OUTPUT ""
DELAY 0.5 seconds
OUTPUT "Tidying up..."
DELAY randnum3 seconds
OUTPUT "Done! [Tidied up for " + CEIL(randnum3) + " se-"
OUTPUT "Pip-tan: 'Wait!'"
DELAY 0.5 seconds
OUTPUT "Pip-tan: 'Goodbye, and thank you for using the Workshop Registration Validation site! <3'"
DELAY 0.5 seconds
OUTPUT "Tidying up... (again)"
DELAY randnum2 seconds
OUTPUT "Done! [Tidied up for " + CEIL(randnum3) + " seconds.]"
DELAY 0.5 seconds
OUTPUT ""
DELAY 0.5 seconds
OUTPUT "============================================================="
END
```
# Part C: Program Implementation
## Programming Language
> Python
## Source Code File
> [`workshp-validator.py`](workshop-validator.py)
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
if name.strip() == ".quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
time.sleep(0.5)
if not name.strip():
  print("Pip-tan: 'Whoops! That isn't a valid name. Goodbye!'")
  sys.exit(1)
else:
  print("Pip-tan: 'Great!'")
time.sleep(0.5)

# Block 2: Age

age = str(input("Pip-tan: 'Now, what's your age?' "))
if age.strip() == ".quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
if age.isdigit():
    age = int(age)
    if age < 11 or age > 18:
        print("Pip-tan: Whoops! That is not a valid age. Goodbye!")
        sys.exit(1)
    else:
        print("Pip-tan: Great!")
else:
    print("Pip-tan: 'Whoops! That is not a valid age. Goodbye!'")
    sys.exit(1)
time.sleep(0.5)

# Block 3: Grade

grade_input = input("Pip-tan: 'Now, what grade are you in?' ")
if grade_input.strip() == ".quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
# Safely handle the conversion to avoid internal crashes on bad inputs
try:
    grade = int(grade_input)
except ValueError:
    grade = 0 # Fallback so the downstream logic catches the validation error cleanly

if grade < 7 or grade > 12:
  print("Pip-tan: 'Whoops! That is not a valid grade. Goodbye!'")
  sys.exit(1)
else:
  print("Pip-tan: 'Great!'")
time.sleep(0.5)

# Block 4: Email

email = input("Pip-tan: 'Now, what's your e-mail address?' ")
if email.strip() == ".quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
if "@" in email:
  print("Pip-tan: 'Great!'")
else:
  print("Pip-tan: 'Whoops! That is not a valid e-mail address. Goodbye!'")
  sys.exit(1)
time.sleep(0.5)

# Block 5: Registration Code

code = input("Pip-tan: 'Now, what's your registation code?' ")
if code.strip() == ".quit":
    print("Pip-tan: 'Goodbye!'")
    sys.exit(0)
if len(code) == 6:
  print("Pip-tan: 'Great!'")
else:
  print("Pip-tan: 'Whoops! That is not a valid registration code. Goodbye!'")
  sys.exit(1)

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
```

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
