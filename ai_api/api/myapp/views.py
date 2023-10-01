from django.shortcuts import render  
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from data_parser.data_parser import DataParser
import json
from http_interface.http_interface import GPTClient
import time

@csrf_exempt
@require_http_methods(["POST"])
def post_data(request):
    request_data = request.body
    gpt = GPTClient('gpt-3.5-turbo', 'You are a chat bot')

    answer = DataParser.AnswersToPrompt(request_data)
    jobs = gpt.jobs_by_questionare(answer)

    positions = DataParser.GetPositionsList(jobs)
    recommendations = []
    for i in range(2):
        ai_response = gpt.schools_by_job(positions[i])
        school_list = DataParser.GetScoolsList(ai_response)
        # print('SCHOOL LIST: ', school_list)
        recommendation = DataParser.CreateRecommendation(positions[i], school_list)
        # print('RECOMENDATION :', recommendation)
        recommendations.append(recommendation)
        time.sleep(2)
    
    response = DataParser.CreateResponse(recommendations)
    
    return HttpResponse(response)


@csrf_exempt
@require_http_methods(["GET"])
def get_data(request):
    return HttpResponse(DataParser.GetQuestionare('before'))
