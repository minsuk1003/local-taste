from django.shortcuts import render
from django.db import connection

def index(request):
    return render(request, 'region_select.html')

def gangwon(request):
    return render(request, 'region_select/gangwon.html')

def chungbuk(request):
    return render(request, 'region_select/chungbuk.html')

def jeonnam(request):
    citys = [
        {'eng_name' : 'naju',
         'kor_name': '나주시',
         'image' : "https://kmug.co.kr/data/file/design/data_logo_%EC%8B%AC%EB%B3%BC%EB%A7%88%ED%81%AC%EA%B8%B0%EB%B3%B8%ED%98%95.jpg",
         'represent' : '곰탕, 장어, 홍어, 불고기',
         },
        {'eng_name': 'boseong',
         'kor_name': '보성군',
         'image': "https://mblogthumb-phinf.pstatic.net/MjAxODEwMjNfNDUg/MDAxNTQwMjYyNDEzOTUy.XaU0Un7SUfG-lFlbovnQfh0dH4fI_w8DS2DoiIS_Q8Ig.P9QKsXR0kdSLN7KfaB_a4PRU-XLGLAepTFa5K8kWJWQg.JPEG.maeknok/%EB%85%B9%EC%B0%A8%EC%88%98%EB%8F%84%EB%B3%B4%EC%84%B1.jpg?type=w800",
         'represent' : '꼬막, 녹차, 녹돈, 전어회, 바지락회',
         },
        {'eng_name': 'jangseong',
         'kor_name': '장성군',
         'image': "https://blog.kakaocdn.net/dn/oUyTg/btqwZiWGfOF/0YFCtHdd6yYUV3JVr7M0wK/img.jpg",
         'represent': '닭숯불구이, 메기',
         },
        {'eng_name': 'damyang',
         'kor_name': '담양군',
         'image': "https://blog.kakaocdn.net/dn/K80va/btqwZ869j1G/JP3RkHtwzU90Qrlj2Ot3r1/img.jpg",
         'represent': '떡갈비, 대통밥, 멸치국수, 돼지숯불갈비',
         },
    ]

    context = {'citys' : citys}
    return render(request, 'region_select/jeonnam.html', context)

def gh(request):
    citys = [
        {'eng_name': 'gyeonghee',
         'kor_name': '경희대',
         'image' : "https://blog.kakaocdn.net/dn/bjsDsi/btqxXJM3JKe/WAK7xHbOm7kxyVqRIvoOaK/img.jpg",
         'represent' : '국제캠퍼스 근처'
         }
    ]
    context = {'citys': citys}
    return render(request, 'region_select/gyeonghee.html', context)