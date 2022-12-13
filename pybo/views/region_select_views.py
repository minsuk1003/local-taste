from django.shortcuts import render
from django.db import connection

def index(request):
    citys = [
        {'eng_name': 'namyangju',
         'kor_name': '남양주시',
         'image': "https://www.nyj.go.kr/preview/result/402/20171113140904168_60155.files/BIN000D.JPG",
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