from django.shortcuts import render  
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from data_parser import data_parser as parser
from http_interface import http_interface as siema

@csrf_exempt
@require_http_methods(["GET"])
def get_questionaire(request):
    qkey = request.headers['type']

    if qkey != 'before' and qkey != 'after':
        return HttpResponse('Invalid type header. before or after required.')
    
    return HttpResponse(parser.DataParser.GetQuestionare(qkey))
