from functools import wraps
from studyroom_forum.response import *
from rest_framework.response import Response
from rest_framework import status




SAMPLE_TOKEN = "TENET"


def authorized_user(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        try:
            token = request.headers.get("token")
            print("Calling decorated function")
            profile = dummyAuthorization(token)
            if profile is not None:
                request.data["created_by"] = profile.id
                request.data["updated_by"] = profile.id
                return function(request, *args, **kwargs)
            else:
                return Response(getGenericResponse("You are not authorized to perform this action", None), status = status.HTTP_401_UNAUTHORIZED)
        except:
                return Response(getGenericResponse("Please pass token", None), status = status.HTTP_401_UNAUTHORIZED)
    return wrap

def dummyAuthorization(token):
    if(token=="TENET"):
        return User(4, "Rust")
    return None

class User():
    def __init__(self, id, name):
        self.id = id
        self.name = name
