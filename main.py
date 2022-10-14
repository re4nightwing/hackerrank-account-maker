import time
import csv
from colorama import init
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


init()
try:
    data = list(csv.reader(open('name1.csv')))
except:
    print("csv failed!")
    exit()

fCount = 0
sCount = 0

for i in range(len(data)-1):
    try:
        print(Back.CYAN,Fore.BLACK,"Record ",i+1," - ",data[i+1][0]," Starting...!")
        driver = webdriver.Firefox()
        driver.get("https://www.hackerrank.com/auth/signup")
        element = driver.find_element_by_id("input-1") #username
        element.send_keys(data[i+1][0])
        element = driver.find_element_by_id("input-2") #email
        element.send_keys(data[i+1][1])
        element = driver.find_element_by_id("input-3") #password
        element.send_keys(data[i+1][2])
        element.send_keys(Keys.RETURN)
        time.sleep(5)
        #/html/body/div[4]/div/div/div/div/div[2]/div/main/form/div/div/label[2]/input
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div/main/form/div/div/label[2]/input").click();
        time.sleep(2)
        #/html/body/div[4]/div/div/div/div/div[2]/div/main/form/button/div/span
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div[2]/div/main/form/button/div/span").click();
        time.sleep(2)
        print(Back.GREEN,Fore.WHITE,"Record ",i+1," - ",data[i+1][0]," - ",data[i+1][2]," DONE!")
        sCount += 1
        driver.close()
    except:
        fCount += 1
        driver.close()
        print(Back.RED,Fore.WHITE,"Record ",i+1," - ",data[i+1][0]," - ",data[i+1][2]," FAILED!")

print(Back.GREEN,Fore.BLUE,"Total ",sCount," successes!")
print(Back.BLUE,Fore.GREEN,"Total ",fCount," failures!")