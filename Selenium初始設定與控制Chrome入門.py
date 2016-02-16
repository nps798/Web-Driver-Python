import time
from selenium import webdriver

'''
Find the latest version of chromedriver (https://sites.google.com/a/chromium.org/chromedriver/home)
Once downloaded, unzip it at the root of your python installation, 
eg C:/Program Files/Python-3.5, and that's it. 
You don't even need to specify the path anywhere and/or add chromedriver to your path or the like. 

若不想這樣移動chromedriver.exe, 則可以在webdriver.Chrome中 指出 chromedriver.exe的位置
driver = webdriver.Chrome('C:\\Users\\Home\\Downloads\\chromedriver_win32\\chromedriver.exe')
'''


driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('天大地大台科大')
search_box.submit()
time.sleep(3)
search_box.send_keys('，台清交成在腳下')
time.sleep(1)
search_box.send_keys('，國立普大都是渣')
time.sleep(1)
search_box.send_keys('，其他砍掉重練啦')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()

