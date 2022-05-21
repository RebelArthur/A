import time
import random

lessons = ['Math', 'Literature', 'Chemistry', 'Physics', 'Biology',
           'History','Geography', 'German','Islam Religion',
           'Islam Religion2', 'Health and Traffic Culture']

chosenlesson = random.choice(lessons)
period = random.randint(15, 50)

if chosenlesson in ('Islam Religion2' or 'Islam Religion'):
    period = random.randint(15,40)
    print(chosenlesson, "," , period, "minutes")
else:
    print(chosenlesson, "," , period, "minutes")

time.sleep(3.20)

input("Press ENTER to exit.")
