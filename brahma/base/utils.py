from rest_framework import status, request
from rest_framework.response import Response


def success_response(data=None, message=None, request=None, extra_data={}):
    result = {"status": {"code": status.HTTP_200_OK, "message":message}, "data":data}
    result.update(extra_data)
    return Response(result)

def error_response(data=None, message=None, request=None, extra_data={}):
    result = {"status": {"code":status.HTTP_403_FORBIDDEN, "message":message}, "data":data}
    return Response(result)