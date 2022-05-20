import random
lessons = ['Math', 'Literature', 'Chemistry', 'Physics', 'Biology', 'History', 'Geography', 'German', 'Islam Religion', 'Islam Religion2']
lesson = random.choice(lessons)
period = random.randint(15, 50)
if lesson in ('Islam Religion2' or 'Islam Religion'):
    period = random.randint(15,40)
    print(lesson, "," , period, "minutes")

else:
    print(lesson, "," , period, "minutes")
input("Press ENTER to exit.")
