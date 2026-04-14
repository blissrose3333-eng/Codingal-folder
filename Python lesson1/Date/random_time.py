import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between",startDate,"and",endDate)
    randomGenerator =random.random()
    dateformat='%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate,dateformat))
    endTime = time.mktime(time.strptime(endDate,dateformat))
    randomTime = startTime +randomGenerator + (endTime - startTime)
    randomDate = time.strftime(dateformat,time.localtime(randomTime))
    return randomDate

print("Random Date =",getRandomDate("1/1/2016","12/12/2018"))