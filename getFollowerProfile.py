import time
import sys
from selenium import webdriver  
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

login_url = 'https://www.instagram.com/accounts/login/'        # ������ �� ����Ʈ �ּ�
NAME = 'hufs_chinese.csv'
datalist = []
profiles = []
data = pd.read_csv(NAME, header = None) # ���ϰ��/�����̸�.csv

datalist = data.values.tolist()
driver = webdriver.Chrome("C:/Users/user/Desktop/chromedriver.exe")  # ũ�� ����̹��� ũ�� �ѱ�
driver.get(login_url)                 # ������ url �ּҷ� �̵�

time.sleep(2)

#driver.find_element_by_name('username').send_keys(username)
#driver.find_element(By.NAME, 'username').send_keys(username)
#driver.find_element(By.NAME, 'password').send_keys(password)
#driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button').submit()# �α���
#/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]/h1
for i in datalist:
    for j in i:
        url = "https://instagram.com/" + str(j)
        driver.get(url)
        time.sleep(5)
        try:
            target = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[3]/h1').text
        except:
            target = '���� ����'
        profiles.append(target)

profile_df = pd.DataFrame(profiles)
profile_df.to_csv(NAME+'_profiles.csv', index=False, encoding='UTF8')
