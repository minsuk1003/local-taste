from django.urls import path
from .views import base_views, question_views, answer_views,\
    region_select_views, recom_result_views, restaurant_detail_views

urlpatterns = [
    # region_select_views.py
    path('',
         region_select_views.index, name='index'),
    path('gangwon/',
         region_select_views.gangwon, name='gangwon'),
    path('chungbuk/',
         region_select_views.chungbuk, name='chungbuk'),
    path('jeonnam/',
         region_select_views.jeonnam, name='jeonnam'),
    path('gh/',
         region_select_views.gh, name='gh'),

    # recom_result_views.py
    path('<str:city>/',
         recom_result_views.result, name='result'),


    # restaurant_detail_views.py
    path('<str:city>/detail_<int:restaurant_num>/',
         restaurant_detail_views.detail, name='detail'),


    # base_views.py
    path('question/',
         base_views.pybo_index, name='pybo_index'),
    path('<int:question_id>/',
         base_views.pybo_detail, name='pybo_detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('question/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),
    path('answer/vote/<int:answer_id>/',
         answer_views.answer_vote, name='answer_vote'),

]