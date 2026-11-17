# Code 2:	The Countdown Timer

import time
# This imports the time library, containing functions such as time.sleep, to make it a more functional timer.
for i in range (10, 0, -1):
	print(i)
  # Again, I used a for loop instead of a while loop, as it feels more natural.
	time.sleep(1)
  # This is the time.sleep function. Having it set to 1 means that the code will sleep for 1 second.
print("Time is up!")
