#本程式曾用於 二階段分年級選課成功
#半自動，遇到驗證碼仍須自己輸入

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()

#登入完成後，register()負責選課
def register():	
	driver.get('http://course.ncku.edu.tw/course/second2.php')
	
	#這裡可能要設置要等一下
	driver.switch_to_alert().accept()

	
	
	depNo = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[1]/input")
	seqNo = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input")

	depNo.send_keys("") #課程系所代碼 XX
	seqNo.send_keys("") #課程代碼 XXX

	submit = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/input[1]")
	submit.click()

	print("請手動輸入驗證碼！之後按下補選")
	#之後都是人工操作：就由手動輸入驗證碼，按下補選，即選課成功！
	
def login():
	driver.get('http://course.ncku.edu.tw/course/anlogin.php')

	#這裡要等一下
	try:
		stuid = WebDriverWait(driver, 60).until(
			EC.presence_of_element_located((By.XPATH, "//input[@name = 'stu_no']"))
		)
		print("wait ok!")
	except TimeoutException:
		print("Loading took too much time!")
		
	#stuid = driver.find_element_by_xpath("//input[@name = 'stu_no']")
	passwd = driver.find_element_by_xpath("//input[@name = 'passwd']")

	stuid.send_keys("") #學生帳號
	passwd.send_keys("") #學生密碼


	submit = driver.find_element_by_xpath("//input[@name = 'sendto']")
	submit.click()
 
	#這裡可能要設置等待時間
	#假設登入之後 畫面有 "該帳號已在線上，目前無法重覆登入" 這句話，代表上一個登入狀況還未登出
	text = driver.find_element_by_tag_name("body")
	
	if(text.text.find("該帳號已在線上，目前無法重覆登入") != -1):
		print("剛剛有登入過帳號了，現在系統自動幫您登出，請稍待！")
		driver.get('http://course.ncku.edu.tw/course/logout.php')
		
		login()
	else:
		print("順利登入，現在導向 second2.php 開始搶課！")
		return "register"
		'''
		driver.get('http://course.ncku.edu.tw/course/second2.php')
		return "go"
		#說明：本來這裡有上面這兩句，但是系統在導引到second2.php時，會有confirm的js視窗跑出來干擾換頁，
		#因此driver.get('http://course.ncku.edu.tw/course/second2.php') 這句沒辦法完成，
		#當然，下一句return也沒辦法執行
		'''


#主程式這裡開始
driver.get('http://course.ncku.edu.tw/course/anlogin.php')
while(1):
	page_time = driver.find_element_by_xpath('//*[@id="timezone"]')
	#<div align="center" id="timezone" name="timezone">Current Time：15:58:30</div>
	page_real_time = page_time.text.replace('Current Time：','').split(':')
	
	#判斷時間：是不是已經開放搶課 page_real_time[0] 小時，page_real_time[1] 分，page_real_time[1] 秒
	if(int(page_real_time[0]) == 9):
		print("時間已到，開始搶課！")
		login()
		break
		# break後，就執行 while 外面的 register() 開始搶課
		# Python 內沒有 GOTO: 功能 
	else:
		print("現在時間",page_real_time[0],":",page_real_time[1],":",page_real_time[2],"還不能搶課")
		time.sleep(5)

register()
	

