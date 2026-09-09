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
