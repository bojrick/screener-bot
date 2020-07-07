from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from automate import send_text

def job_function():
    print("Hello World")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_text, 'interval', hours=2)

sched.start()