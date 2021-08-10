import os, sys
import pathlib
from datetime import datetime
from testconf.delreport import deletereports
time = str(datetime.today().strftime('%Y-%m-%d'))

path = pathlib.Path(__file__).parent / "counter.txt"

fileToRead =open(path, 'r+')
data = int(fileToRead.read())

newData = (data + 1)

fileToRead.seek(0)
fileToRead.write(str(newData))
fileToRead.truncate()
fileToRead.close()

fileToReadForNewData = open(path, 'r')
readNewData = fileToReadForNewData.read()
fileToReadForNewData.close()

#For running testCases
command = "pytest -s --alluredir=ReportAllure1/"+ time + "_" + readNewData + " --html=ReportHtml/report_"+ time + "_" + readNewData + ".html --self-contained-html" + " " + "TestCase"
os.system(command)

# keep only 2 reports
number = 2
deletereports(number)

#For generating report
os.system("allure serve "+"ReportAllure1/" + time + "_" + readNewData)
