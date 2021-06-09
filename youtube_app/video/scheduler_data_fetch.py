import requests
from apscheduler import events
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc
from django.conf import settings




def fetch_response_from_api():
    """[This function actually requests data from youtube api]
    """
    params = {'part': 'snippet', 'key': settings.API_KEY,
              'q': settings.SEARCH_QUERY, 'max_results': 1000}
    url = 'https://www.googleapis.com/youtube/v3/search'
    try:
        response = requests.get(url=url, params=params)
        json_data = response.json()
    except requests.exceptions.RequestException as e:
        print("Error ", str(e))
        json_data = {}
    # print(json_data)
    return json_data


def save_in_database(json_response):
    """[Create an entry in database if the video does  not exist already]
    """
    from .models import Video
    if 'items' in json_response:
        for each_video in json_response['items']:
            print(each_video)
            id = each_video['id']['videoId']
            publishing_datetime = each_video['snippet']['publishedAt']
            title = each_video['snippet']["title"]
            description = each_video['snippet']["description"]
            thumbnails = each_video['snippet']["thumbnails"]
            if not Video.objects.filter(id=id).exists():
                Video.objects.create(id=id, 
                                    publishing_datetime=publishing_datetime,
                                    title=title, 
                                    description=description, 
                                    thumbnails=thumbnails,
                                    )



def youtube_sync():
    """[The function that syncs with youtube every 10 seconds]
    """
    json_response = fetch_response_from_api()

    save_in_database(json_response)


def begin():
    """[Schedules a task to fetch api response every 10 s]
    """
    print("Async task begun!")
    # setup scheduler
    scheduler = BackgroundScheduler()
    scheduler.configure(timezone=utc)

    # Create task
    scheduler.add_job(youtube_sync, 'interval', seconds=10)

    # Begin the task
    scheduler.start()
