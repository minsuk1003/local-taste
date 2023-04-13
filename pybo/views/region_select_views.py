from django.shortcuts import render
from django.db import connection

def index(request):
    citys = [
        {'eng_name': 'namyangju',
         'kor_name': '남양주시',
         'image': "data:image/jpeg;base64,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",
         'represent': '장어, 먹골배, 시래기 비빔밥',
         },
        {'eng_name': 'hanam',
         'kor_name': '하남시',
         'image': "https://blog.kakaocdn.net/dn/L3qvK/btqw87mBi2S/Ks07Xmqq8I6xqJxZW99oN0/img.jpg",
         'represent': '오리백숙, 닭내장탕, 소곱창',
         },
        {'eng_name': 'gwangju',
         'kor_name': '광주시',
         'image': "https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Ftupj5%2Fbtqw9NuNznT%2FLEcCsS1KicOykLDQmQ6aC0%2Fimg.jpg",
         'represent': '소머리국밥, 산채정식, 붕어찜',
         },
    ]
    context = {'citys': citys}
    return render(request, 'region_select.html', context)

def gangwon(request):
    citys = [
        {'eng_name': 'wonju',
         'kor_name': '원주시',
         'image': "https://blog.kakaocdn.net/dn/djHElD/btqxf4wzGkH/2oe0OcS8qlju0h3FVO2T6k/img.jpg",
         'represent': '추어탕, 뽕잎밥, 복숭아불고기',
         },
    ]
    context = {'citys': citys}
    return render(request, 'region_select/gangwon.html', context)

def chungbuk(request):
    citys = [
        {'eng_name': 'jecheon',
         'kor_name': '제천시',
         'image': "https://www.jecheon.go.kr/site/www/download/new-brand.jpg",
         'represent': '순대국밥, 장어, 홍어, 불고기',
         },
    ]
    context = {'citys': citys}
    return render(request, 'region_select/chungbuk.html', context)

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