from django.shortcuts import render  
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from data_parser.data_parser import DataParser

@csrf_exempt
@require_http_methods(["POST"])
def post_data(request):
    return HttpResponse(request)

@csrf_exempt
@require_http_methods(["GET"])
def get_data(request):
    return HttpResponse(DataParser.GetQuestionare("before"))