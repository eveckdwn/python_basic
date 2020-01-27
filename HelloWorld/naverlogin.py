from selenium import webdriver

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
#options = webdriver.ChromeOptions()
#options.add_argument('headless')
#options.add_argument('window-size=1920x1080')
#options.add_argument("disable-gpu")
#driver = webdriver.Chrome('C:/IT\python util/chromedriver_win32/chromedriver', chrome_options=options)

driver = webdriver.Chrome('C:/IT\python util/chromedriver_win32/chromedriver')
# PhantomJS의 경우 | 아까 받은 PhantomJS의 위치를 지정해준다.
# driver = webdriver.PhantomJS('C:/IT/python util/phantomjs-2.1.1-windows/bin/phantomjs')

# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')

driver.implicitly_wait(3)
