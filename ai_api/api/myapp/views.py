from django.shortcuts import render  
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from data_parser.data_parser import DataParser
import json

@csrf_exempt
@require_http_methods(["POST"])
def post_data(request):
    request_data = json.loads(request.body)

    return JsonResponse(request_data)

@csrf_exempt
@require_http_methods(["POST"])
def get_data(request):
    request_data = json.loads(request.body)
    qkey = request_data.get('type')
    
    if qkey != "before" and qkey != "after":
        return JsonResponse({
            "error": "Wrong 'type' header"
        })

    response = JsonResponse(json.loads(DataParser.GetQuestionare(qkey)))
    return response