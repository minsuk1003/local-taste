from django.shortcuts import render
from django.db import connection
from ..models import Restaurant

def detail(request, restaurant_num, city):
    type_eng_kor = {'korean': '한식', 'japanese': '일식', 'chinese': '중식',
                    'western': '양식', 'snack': '간식/야식',
                    'cafe': '카페', 'bar': '술집', 'others': '기타'
                    }

    cursor = connection.cursor()
    strSql = "SELECT * FROM restaurant " \
             "WHERE restaurant_num = (%s) AND city = (%s)"
    result = cursor.execute(strSql, (restaurant_num, city, ))
    datas = cursor.fetchall()

    connection.commit()
    connection.close()

    restaurant = {
        'restaurant_num' : datas[0][0],
        'restaurant_name' : datas[0][1],
        'city' : datas[0][2],
        'address' : datas[0][3],
        'phone_num' : datas[0][4],
        'type' : datas[0][5],
        'sun': datas[0][6],
        'mon': datas[0][7],
        'tue': datas[0][8],
        'wed': datas[0][9],
        'thu': datas[0][10],
        'fri': datas[0][11],
        'sat': datas[0][12],
        'average_rating': datas[0][13],
        'review_count': datas[0][14],
        'image_link': datas[0][15],
        'local_rating' : datas[0][16],
        'normal_rating': datas[0][17],
        'total_rating' : datas[0][18],
        'local_count' : datas[0][19],
        'normal_count': datas[0][20],
        'map_image' : datas[0][21]
    }

    context = {'restaurant' : restaurant, 'city' : city, 'type_eng_kor': type_eng_kor}


    return render(request, 'restaurant_detail.html', context)