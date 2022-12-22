from django.shortcuts import render
from django.db import connection
from django.core.paginator import Paginator
from django.db.models import Q
from ..models import Restaurant


def result(request, city):
    city_eng_kor = {'namyangju': '남양주시', 'hanam': '하남시', 'gwangju': '광주시',
                    'naju': '나주시', 'boseong': '보성군', 'jangseong': '장성군',
                    'damyang': '담양군', 'yeonggwang': '영광군', 'gyeonghee': '경희대'}
    type_eng_kor = {'korean': '한식', 'japanese': '일식', 'chinese': '중식',
                    'western': '양식', 'snack': '간식/야식', 'asian': '아시아',
                    'cafe': '카페', 'bar': '술집', 'others': '기타'
                    }

    try:
        cursor = connection.cursor()
        strSql = "SELECT * " \
                 "FROM restaurant " \
                 "WHERE review_count >= 20 AND total_rating >= 3 " \
                 "AND city = (%s) " \
                 "ORDER BY local_rating DESC"
        result = cursor.execute(strSql, (city,))
        datas = cursor.fetchall()

        connection.commit()
        connection.close()

        restaurants = []
        for data in datas:
            row = {
                'restaurant_num': data[0],
                'restaurant_name': data[1],
                'city': data[2],
                'type': data[5],
                'review_count': data[14],
                'image_link': data[15],
                'local_rating': data[16],
                'total_rating': data[18],
                'local_count': data[19]
            }
            restaurants.append(row)
    except:
        connection.rollback()
        print("Failed selecting in restaurant list")

    restaurants = Restaurant.objects.order_by('-local_rating')
    restaurants = restaurants.filter(
        Q(city=city) &
        Q(local_rating__gte=3.0) &
        Q(review_count__gte=20) &
        Q(local_count__gte=5)
    ).distinct()

    f = request.GET.getlist('f')
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    if kw:
        restaurants = Restaurant.objects.order_by('-local_rating')
        restaurants = restaurants.filter(
            (Q(restaurant_name__icontains=kw) | Q(address__icontains=kw)) &
            Q(city=city)
        ).distinct()

    if f:
        query = Q()
        query &= Q(type__in=f)
        restaurants = restaurants.filter(query).distinct()

    
    paginator = Paginator(restaurants, 12)
    page_obj = paginator.get_page(page)
    context = {'restaurants': page_obj, 'city': city,
               'city_eng_kor': city_eng_kor, 'type_eng_kor': type_eng_kor,
               'page': page, 'kw': kw, 'f': f}
    return render(request, 'recom_result.html', context)
