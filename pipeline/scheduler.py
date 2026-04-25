from apscheduler.schedulers.blocking import BlockingScheduler
from pipeline import daily_runner

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon-fri', hour=16, minute=45, timezone='America/New_York')
def run():
    daily_runner.main()

scheduler.start()