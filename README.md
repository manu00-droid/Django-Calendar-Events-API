# Django-Calendar-Events-API
**API used to fetch google calendar events**.

**You need to replace client_secret.json file with your own client_secret.json file**.

**You can get it from https://console.cloud.google.com/ , then going to APIs section, then in credentials section**.

It uses oauth2.0 to get access token for the user and then included the access token in a request to the API in an Authorization HTTP header Bearer value.

Below are detail of API endpoint:

1) /rest/v1/calendar/init/   :
    This starts the step 1 of the OAuth. It redirect the user to Google's OAuth 2.0 server to initiate the authentication and authorization process, which will prompt user for his/her credentials.
2) /rest/v1/calendar/redirect/    :
  This view do two things:
  a) Handle redirect request sent by google with code for token and fetch authorization code from it and to exchange an authorization code for an access        token, call the https://oauth2.googleapis.com/token endpoint.
  b) Fetch events from calendars API.
  
  At the end you recieve a json response

  # Basic Flow
  
  ![abc drawio (1)](https://github.com/manu00-droid/Django-Calendar-Events-API/assets/79694635/50a3c568-b3f7-44e6-8cc7-65915bfaf6aa)

   # Application Flow

1) User is prompted for his/her credentials
  ![image](https://user-images.githubusercontent.com/79694635/178118959-b9bd514b-ea46-414e-87a5-7f504dd04bee.png)

2) After authorization events are fetched:

![Screenshot from 2022-07-10 00-06-20](https://user-images.githubusercontent.com/79694635/178118772-7630c8ce-536c-4a80-a8d2-b2cbc9352a20.png)
![Screenshot from 2022-07-10 00-06-38](https://user-images.githubusercontent.com/79694635/178118779-86812049-7c47-4536-b9ae-9d2b433afd75.png)
