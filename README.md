# youtube_search
## Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

## Requirements
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Make a dashboard to view the stored videos with filters and sorting options (optional)
    
## How to <i>Setup</i>
 - Follow the instructions on [docker website](https://docs.docker.com/engine/install/) to install docker on your system.
 - Install docker compose - https://docs.docker.com/compose/install/
 - Clone the repository and navigate inside it
 - Create `.env` file.
 
   Example:
    ```
    CELERY_BROKER_URL='amqp://rabbitmq'
    CELERY_TASK_DEFAULT_QUEUE='fampay'
    GOOGLE_API_KEYS=APIKEY_1,APIKEY_2,APIKEY_3,....,APIKEY_N
    QUERY_STRING=cricket
    DB_NAME='fampay'
    DB_USER='postgres'
    DB_PASSWORD='wDnfWovh4uf3'
    DB_HOST='db'
    ```
    
      You can copy and paste the above contents to `.env` file and replace APIKEY_1,APIKEY_2,...,APIKEY_N with your Google api keys. 
      And also replace DB_PASSWORD value, you can refer `POSTGRES_PASSWORD` in [docker-compose.yml](/docker-compose.yml) for database password
  
 - Finally run `docker-compose up -d --build` from your terminal

The application will come up @http://localhost

## API Description
This App contains the following 
##### Get Api [(http://SERVER_IP/videos)](http://localhost/videos)
  - This will list the stored videos in reverse chronological order of their publishing date


##### Search Api [(http://SERVER_IP/search?q=query_string)](http://localhost/search?q=)
  - This is search api which will accept a querying parameter and returns the videos that has the query string either in their title or description.
  You need to pass the query string in the url after `q=`
  
  For example: http://localhost/search?q=cricket. Here `cricket` is the querying parameter

##### Dashboard [(http://SERVER_IP/dashboard)](http://localhost/dashboard)
  - A dashboard which will be having the list of all stored videos. You can filter videos either using search bar provided or you can choose the video from the available list of videos in the dropdown. It also has options to sort elements in ascending or descending order based on the field choosen.

### Reference
[YouTube data v3 API](https://developers.google.com/youtube/v3/getting-started)

[Django](https://docs.djangoproject.com/en/3.2/)


 
