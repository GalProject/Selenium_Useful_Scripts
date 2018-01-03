from selenium import webdriver
import urllib
import time

linkSrc = "http://stat.bgu.ac.il/vod/safotform01.mp4"
# driver = webdriver.Chrome("C:\\Users\\GalBenEvgi\\Desktop\\chromedriver.exe")

for x in range(1, 24):
    if x < 10:
        print '0' + str(x)
    else:
        print str(x)

