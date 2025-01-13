from schedule import every, repeat, run_pending
import time

@repeat(every(10).seconds)
# TODO: Create a job function that print a message
def task_a():
    print("This is Job A")

while True:
    run_pending()
    time.sleep(1)