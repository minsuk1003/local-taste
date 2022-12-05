from django.shortcuts import render
from ..models import Restaurant

def post_view(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'recom_result.html', {"restaurants":restaurants})