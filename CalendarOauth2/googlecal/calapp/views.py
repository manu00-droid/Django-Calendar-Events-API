from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests as requestlib
import os

client_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                '/home/manav/PycharmProjects/CalendarOauth2/googlecal/calapp/client_secret.json')
scope_for_calendar = 'https://www.googleapis.com/auth/calendar'
client_file = open(client_file_path)
file_data = json.load(client_file)
client_id = file_data['web']['client_id']
client_secret = file_data['web']['client_secret']


@api_view(['GET'])
def GoogleCalendarInitView(request):
    endpoint = 'https://accounts.google.com/o/oauth2/v2/auth'
    redirect_uri = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
    access_type = 'offline'
    URL = f"{endpoint}?scope={scope_for_calendar}&access_type={access_type}&response_type=code&redirect_uri={redirect_uri}&client_id={client_id}"
    return redirect(URL)


@api_view(['GET'])
def GoogleCalendarRedirectView(request):
    data = request.query_params
    code = data['code']
    print(code)
    grant_type = 'authorization_code'
    redirect_uri = 'http://127.0.0.1:8000/rest/v1/calendar/redirect/'
    endpoint = 'https://oauth2.googleapis.com/token'
    PARAMS = {"client_id": client_id, 'client_secret': client_secret, 'code': code, 'grant_type': grant_type,
              'redirect_uri': redirect_uri}
    response = requestlib.post(url=endpoint, params=PARAMS)
    data = response.json()
    access_token = data['access_token']

    # Getting calendarId
    access_token = "Bearer " + access_token
    headers = {"Authorization": access_token}
    endpoint_calendar_list = 'https://www.googleapis.com/calendar/v3/users/me/calendarList'
    response = requestlib.get(url=endpoint_calendar_list, headers=headers)
    data = response.json()
    calendar_id = data['items'][0]['id']

    # Getting calendar EVENTS
    endpoint_get_events = f"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"
    response = requestlib.get(url=endpoint_get_events, headers=headers)
    data = response.json()
    return Response(data)
