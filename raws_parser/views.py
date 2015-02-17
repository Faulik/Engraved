from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from raws_parser import tojson, utils
import json
import os

PACKS_DIR = os.getcwd() + '/packs/'


class Packs(APIView):
    """
    /raws/packs | GET | Get all the packs names
    /raws/packs | POST | Upload pack
    /raws/packs | PUT | Update pack
    """
    def get(self, request, format=None):
        result = {
            "packs": [
            ]
        }
        for d in os.listdir(PACKS_DIR):
            if os.path.isdir('./packs/' + d):
                files = []
                for f in os.listdir(PACKS_DIR + d + '/raw/objects/'):
                    if os.path.isfile(PACKS_DIR + d + '/raw/objects/' + f):
                        files.append(f)
                result["packs"].append({"dir_name": d, "files": files})
        return Response(result)

    def post(self, request, format=None):
        pass

    def put(self, request, format=None):
        pass


class Pack(APIView):
    """
    /raws/packs/{pack_name}/{file_name} | GET | Get file from pack
    /raws/packs/{pack_name}/{file_name}?format=json | GET | Get file for d3 lib
    /raws/packs/{pack_name}/{file_name} | PUT | Update file in pack
    """
    def get(self, request, pack_name, file_name, format=None):
        path = PACKS_DIR + pack_name + '/raw/objects/' + file_name + '.txt'
        if os.path.isfile(path):
            with open(path, 'r') as f:
                file = f.read()
                return Response(file)
        return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, pack_name, file_name, format=None):
        pass


def get_test_d3_json(request):
    with open(os.getcwd() +'/raws_parser/tests/assets/test_d3_json.json', 'r') \
            as f:
        data = json.load(f)
    return JsonResponse(data)
