import requests
from apscheduler import events
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc


def fetch_response_from_api():
    """[This function actually requests data from youtube api]
    """
    pass



def youtube_sync():
    """[The function that syncs with youtube every 10 seconds]
    """
    response = fetch_response_from_api()

    save_in_database(response)


def begin():
    """[Schedules a task to fetch api response every 10 s]
    """
    # setup scheduler
    scheduler = BackgroundScheduler()
    scheduler.configure(timezone=utc)

    # Create task
    scheduler.add_job(youtube_sync, 'interval', seconds=10)



