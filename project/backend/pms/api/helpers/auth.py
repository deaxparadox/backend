from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status


############## RETREIVE TOKEN FOR AUTHORIZED USER ####################
# 
def get_token(user: User | None):
    """Return the Token
    
    If token does not exist return 404

    Returns:
        Reponse: dictionary of user auth token
    """
    try:
        token: Token = Token.objects.get(user=user)
    except Token.DoesNotExist as e:
        return Response({"message": "token not found"}, status=status.HTTP_404_NOT_FOUND)
    except Token.MultipleObjectsReturned as e:
        return Response({"message": "multiple object found"}, status=status.HTTP_404_NOT_FOUND)
    return Response({"token": token.key}, status=status.HTTP_200_OK)




########## GET TOKEN FROM REQUEST HEADER
#
def get_token_from_header(request) -> str | None:
    """Retreive the token from header
    
    Token is stored in the `Authorization` key in header.
    
    If `Authorization` key not found in header, return None
    
    if

    Args:
        request: incoming request

    Returns:
        str: user_token
    """
    # print(request.META)
    AUTORIZATION: str | None = request.META.get("HTTP_AUTHORIZATION")
    if not AUTORIZATION:
        return 
    
    TOKEN = AUTORIZATION.split(" ")[-1]
    
    try:
        user_token = Token.objects.get(key=TOKEN)
    except Token.DoesNotExist:
        return 
    return user_token