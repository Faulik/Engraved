from django.shortcuts import render
from django.http import JsonResponse
import json
import os

def JsonResponse(request):
    with open(os.getcwd() +'/raws_parser/tests/assets/test_d3_json.json', 'r') \
            as f:
        data = json.load(f)
    return JsonResponse(data)
