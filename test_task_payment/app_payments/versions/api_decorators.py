import json
from django.http.response import HttpResponse
from django.conf import settings
from rest_framework.decorators import  api_view
from rest_framework.response import Response

@api_view(['GET'])
def error_access_token(request,status=403):
    return Response({'errors':{'access-token':'invalid access_token'}},status=status)

def access_token_checker():
    def decorator(fn):
        def case_decorator(*args, **kwargs):
            request = args[0]
            access_token = request.META.get('HTTP_ACCESS_TOKEN')
            if access_token  and access_token in settings.ACCESS_TOKENS:
                return fn(*args, **kwargs)
            else:
                return error_access_token(*args,**kwargs)
        return case_decorator
    return decorator


