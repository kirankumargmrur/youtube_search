# fampay_youtube_search
### Project Goal
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

### Requirements
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.
- Add support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
- Make a dashboard to view the stored videos with filters and sorting options (optional)
    
### How to <i>Setup</i>
 - Follow the instructions on docker website [https://docs.docker.com/engine/install/] to install docker on your system.
 - Install docker compose - https://docs.docker.com/compose/install/
 - Clone the repository and navigate inside it
 - Run `docker-compose up -d --build`

The application will come up @http://localhost

### API Description
This App contains the following 
#### Get Api [/videos](http://localhost/videos)
  - This will list the stored videos in reverse chronological order of their publishing date


#### Search Api(http://localhost/search?q=)
  - This is search api which will accept either title or description as a querying parameter and returns the videos that has the query parameter either in their title or description.
  You need to pass the query string in the url after `q=`
  For example: http://localhost/search?q=cricket. Here `cricket` is the querying parameter

#### Dashboard (http://localhost/dashboard)
  - A dashboard which will be having the list of all stored videos. You can filter videos either using search bar provided or you can choose the video from the available list of videos in the dropdown.It also has options to sort elements in ascending or descending based on the field choosen.

### Reference
[YouTube data v3 API](https://developers.google.com/youtube/v3/getting-started)

[Django](https://docs.djangoproject.com/en/3.2/)


 
