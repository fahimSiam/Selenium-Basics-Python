from selenium import webdriver
from selenium.webdriver.common import action_chains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
import re

driver=webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://evaly.com.bd/")


#clicing the popup cut button
driver.find_element(By.XPATH,'//body/reach-portal[1]/div[1]/div[1]/div[1]/section[1]/div[1]/button[1]/*[1]').click()

#clicking the account icon
driver.find_element(By.XPATH,"//body/div[@id='__next']/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[1]/span[1]/span[1]/*[1]").click()

#input login credentials
driver.find_element(By.NAME,'phone').send_keys('01872627888')
driver.find_element(By.NAME,'password').send_keys('QPRYMQX3$v_RakQ')
driver.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
#logged in

time.sleep(3)
driver.find_element(By.LINK_TEXT,'Speaker').click()
#clicked products

#get the product names
#time.sleep(3)
productList=driver.find_elements(By.CSS_SELECTOR, 'p.BrandCard___StyledP-sc-1kq2v0k-1.bAWFRI')
#print(len(productList))
for i in productList:
    print(i.text)
#printed all the product names


#time.sleep(3)
for item in productList:
    if item.text=='MI':
        item.click()
        break
#CLICKED INTO MI SPEAKERS PAGE
time.sleep(3)


miList=driver.find_elements(By.CSS_SELECTOR, 'p.bzqEqm')
miList2=driver.find_elements(By.CSS_SELECTOR, 'p.cFzjHk')#added the discounted prices
for j in miList2:
    miList.append(j)


max=-1
for price in miList:
    taka=price.text.strip("৳")
    print(taka)
    if(int(taka)>max):
        max=int(taka) #finding the max price
print('maximum priced product is',max)


for k in miList:
    if(k=='৳',taka):
        k.click() #clicked into the max priced product
        break
#time.sleep(3)

#showing the info of maximum priced product
print('Name of max Product: ',driver.find_element(By.CSS_SELECTOR,'h2.text-gray-700').text)
print('Price of max Product: ',driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/h2[1]").text)
#PRODUCT WORK DONE

driver.find_element(By.XPATH,"//button[contains(text(),'I understand')]").click() #have to click this 1st before career
career=driver.find_element(By.XPATH,"//a[contains(text(),'Career')]")
career.click()


validMail=True;
#carrer page gmail checking
catagoriesList=driver.find_elements(By.CSS_SELECTOR,'h3.mb-0')
for i in catagoriesList:
    i.click()
links=driver.find_elements(By.CSS_SELECTOR,'a.text-blue-500')
regex = r'\b[A-Za-z0-9._%+-]+@evaly.com.bd'

#email validation method
def check(email):
     
    # pass the regular expression
    # and the string in search() method
    if(re.match(regex, email)):
        print("Valid Email")

    else:
        validMail=False
        print("Invalid Email")


for link in links:
    print(link.text)
    check(link.text)

#final printing
if(validMail==False):
    print('there was an invalid mail')
elif(validMail==True and len(catagoriesList)==len(links)):
    print('All categories have valid mails')
else:
    print('not all categories have mail')

time.sleep(3)
driver.quit()







