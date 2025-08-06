import schedule
import time

# Define a task
def greet():
    print("Hello! This is your scheduled task.")

# Schedule the task to run every 5 seconds
schedule.every(5).seconds.do(greet)

# Loop to keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
