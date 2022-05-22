import time
import random

lessons = ['Math', 'Literature', 'Chemistry', 'Physics', 'Biology',
           'History','Geography', 'German','Islam Religion',
           'Islam Religion2', 'Health and Traffic Culture']

chosenlesson = random.choice(lessons)
period = random.randint(10, 40)

if chosenlesson in ('Islam Religion2' or 'Islam Religion'):
    period = random.randint(8,25)
    print(chosenlesson, "," , period, "minutes")
else:
    print(chosenlesson, "," , period, "minutes")

time.sleep(3.20)

input("Press ENTER to exit.")
