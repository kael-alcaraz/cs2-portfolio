import time
import random
import math

# Random loading times
randnum1 = random.uniform(1, 5)
randnum2 = random.uniform(1, 5)
randnum3 = random.uniform(1, 5)

# Functions (fixed to return strings instead of None)
def calculate_average(score1, score2, score3):
    totalscore = score1 + score2 + score3
    return totalscore / 3
    
def get_performance(average):
    if average >= 85:
        return "Pip-tan: 'You have gained Mastery for this performance!'"
    elif average >= 70:
        return "Pip-tan: 'You are Developing in this performance.'"
    else:
        return "Pip-tan: 'Oh no! Your score Needs Review!'"

def get_performance2(average):
    if average >= 85:
        return "Mastery"
    elif average >= 70:
        return "Developing"
    else:
        return "Needs Review"

def is_eligible(average, completed_tasks):
    if average >= 85 and (3 <= completed_tasks <= 5):
        return "Pip-tan: 'You are Eligible for The Challenge!'"
    else:
        return "Pip-tan: 'You are NOT Eligible for the Challenge.'"

def is_eligible2(average, completed_tasks):
    return average >= 85 and (3 <= completed_tasks <= 5)

# First Loading Screen
print("Pip-tan: 'Hey! Hello! Let me get things set up for you.'")
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

# Input Block
time.sleep(0.5)
name = str(input("Pip-tan: 'Hello! What's your name? "))
time.sleep(0.5)
s1 = int(input("Pip-tan: 'So, how well did you score on a test?' "))
time.sleep(0.5)
s2 = int(input("Pip-tan: 'Now, how much did you score on another test?' "))
time.sleep(0.5)
s3 = int(input("Pip-tan: 'Again, how much did you score on yet another test?' "))

average = calculate_average(s1, s2, s3)
perfmessage = get_performance(average)
time.sleep(0.5)
perfcategory = get_performance2(average)

print(f"Pip-tan: 'You have gotten an average of {average}.'") 
time.sleep(0.5)
print(perfmessage)
time.sleep(0.5)

completed_tasks = int(input("Pip-tan: 'Okay, now, how many tasks did you complete?' "))
time.sleep(0.5)

eligmessage = is_eligible(average, completed_tasks)
eligcategory = is_eligible2(average, completed_tasks)
print(eligmessage) 
time.sleep(0.5)

# Second Loading Screen
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

# Counter for easy reading
print("Calculated!")
print("=============================================================")
time.sleep(0.5) 
print(f"Name: {name}") 
time.sleep(0.5)
print(f"First Score: {s1}")
time.sleep(0.5)
print(f"Second Score: {s2}")
time.sleep(0.5)
print(f"Third Score: {s3}") 
time.sleep(0.5)
print(f"Performance: {perfcategory}")
time.sleep(0.5)
print(f"Eligibility: {eligcategory}") 
time.sleep(0.5)
print(f"Pip-tan: '{name} has gotten an average of {average} across 3 selected tasks, has completed {completed_tasks} tasks, is in the Performance Category of {perfcategory}, and is Eligible: {eligcategory} for The Challenge.'")
time.sleep(0.5)

time.sleep(1)
print("=============================================================")
print(" ")

# Final Loading Screen
print("=============================================================")
time.sleep(0.5)
print()
time.sleep(0.5)
print("Tidying up...")
time.sleep(randnum3)
print(f"Done! [Tidied up for {math.ceil(randnum3)} secon-")
print("Pip-tan: 'Wait!'")
time.sleep(0.5)
print("Pip-tan: 'Goodbye, and thank you for using the Student Performance Calculator! <3'")
time.sleep(0.5)
print("Tidying up... (again)")
time.sleep(randnum3)
print(f"Done! [Tidied up for {math.ceil(randnum3)} seconds.]")
time.sleep(0.5)
print()
time.sleep(0.5)
print("=============================================================")
# Documentation Question 1: The function calculate_average returns a number, the function get_performance returns a string, and the function is_eligible2 returns a boolean.
# Documentation Question 2: The function get_average gets stored into the variable average, in which it gets used to calculate get_performance.
# Documentation Question 3: They will not be eligible for The Challenge.
# Documentation Question 4: Because instead of printing then returning, using only return gives no response of None.
