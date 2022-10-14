import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

data = list(csv.reader(open('name.csv')))

for i in range(len(data)-1):
    print(data[i+1][0])
    print(data[i+1][1])
    print(data[i+1][2])