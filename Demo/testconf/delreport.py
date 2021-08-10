import shutil
import os
from pathlib import Path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../ui'))
#folder deleting method
def del_dir(num_of_dir):
    baseDir = Path(__file__).resolve().parent.parent
    dirName = "ReportAllure1"
    dirPath = os.path.join(baseDir, dirName)
    # print(dirPath)
    # dirList = [f for f in sorted(os.listdir(dirPath))]
    dirList = [os.path.join(dirPath, f) for f in sorted(os.listdir(dirPath))]
    dirList = dirList[:len(dirList) - num_of_dir]
    # print(dirList)

    for delDir in dirList:
        try:
            shutil.rmtree(delDir)
            # print('delete: ' + delDir)

        except OSError as e:
            print("Error: %s : %s" % (delDir, e.strerror))
    # print('dir deleted')

#file deleting method
def del_file(num_of_file):
    baseDir = Path(__file__).resolve().parent.parent
    dirName = "ReportHtml"
    dirPath = os.path.join(baseDir, dirName)
    fileList = [os.path.join(dirPath, f) for f in sorted(os.listdir(dirPath))]
    fileList = fileList[:len(fileList) - num_of_file]
    # print(fileList)

    for delfile in fileList:
        os.remove(delfile)


def deletereports(number):
    del_dir(number + 1)
    del_file(number)
