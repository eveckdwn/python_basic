# package: 어떤 기능들을 구현하는 모듈들의 합 (≒ liabrary(라이브러리))
#   ex. 날씨 정보를 알아보는 패키지, 위치 정보를 알아보는 패키지
# module: 코드를 잘 모아서 기능 하나를 구현해놓은 파일

#   animal package
#   dog, cat modules
#   dog, cat modules can say "hi"

"""
from animal import dog  # animal 패키지에서 dog라는 모듈을 갖고와줘
from animal import cat

d = dog.Dog()   #   instance
d.hi()

c = cat.Cat()
c.hi()
"""

"""
from animal import *    # animal 패키지가 갖고 있는 모듈을 다 불러와
d = Dog()
c = Cat()

d.hi()
c.hi()
"""

"""
VSCODE에서 패키지를 다운 받는 방법:
    - CMD에서 하기 명령어를 활용하여 패키지 다운로드
    - python -m pip install {패키지명}
"""

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="changjoo")
location = geolocator.geocode("Songpa-gu, Seoul, Republic of Korea")
print(location)