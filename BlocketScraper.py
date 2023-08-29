import time

from selenium import webdriver 

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from chromedriver_py import binary_path 
#svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome()
# Optional argument, if not specified will search path.
# driver = webdriver.Chrome('D:/games/chromedriver')
driver.get("https://www.blocket.se/")

button = driver.find_element("id", "accept-ufti")
driver.execute_script("arguments[0].click();", button)
time.sleep(3)

price = []
name = []
pricename = []
counter = 0
underOver = True
underOverValue = 7500
articles = []

search_bar = driver.find_element("class name", "react-autosuggest__input")
        


search_bar.clear()
search_bar.send_keys("macbook")
search_bar.send_keys(Keys.RETURN)

print(driver.title)
time.sleep(3)
# Let the user actually see something!
dropdown = Select(driver.find_element("id", "sort-select"))
dropdown.select_by_value('date')

driver.implicitly_wait(4)
#annons = driver.find_element("class name", "LoadingAnimationStyles__PlaceholderWrapper-sc-c75se8-0 cfYzFC")
annons = driver.find_element("xpath","//div[contains(@class, 'SearchResultsstyles__SearchResultsWrapper-sc-kmhlm3-1 gZEfAS')]")
#for i in range(4):

driver.implicitly_wait(6)

#print(annons.get_attribute('aria-label'))
#children = annons.find_elements("xpath","./child::*")

time.sleep(10)

#for i in children:
#    try:
#        print(i)
#        title = annons.find_element("id", i)
#        print(2)
#        driver.implicitly_wait(16)
#        print(2)
#        print(title.find_attribute('aria-label'))
#    except:
#        print('error')
#        pass
#for a in driver.find_elements("xpath", "//div[contains(@class, 'Pagination__Strong-sc-uamu6s-6 ceAxhh')]"):
#    articles.append(a)
articles = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div[2]/div[1]/div[5]/div/div[1]/span[2]")

articleNumber = int(articles.text)
pages = round(articleNumber / 39)
print(pages)

counter = 0

for i in range(pages):
        
    print('page numer ' + str(i))
    
    
    
    for p in driver.find_elements("xpath", "//div[contains(@class, 'styled__Wrapper-sc-1kpvi4z-0 ddgqIB')]"):
        #print(p.get_attribute('aria-label'))    
        name.append(str(p.get_attribute('aria-label')))   
    counter  = counter + 1            

    for element in driver.find_elements("xpath","//div[contains(@class, 'styled__SalesInfo-sc-1kpvi4z-20 eRZMjm')]" ):
        #print(element.text)
        try:
            elementInt = str(element.text)
            elementInt = elementInt.replace('kr', '')
            elementInt = elementInt.replace(' ','')
            elementInt = int(elementInt)
            
            
            price.append(elementInt)
        except:
            price.append(' price not availible')
            print(element.text + 'was not added')
    counterTwo = 0
    
    
    
    for elementName in driver.find_elements("xpath", "/html/body/div[@id='__next']/div[@class='LayoutStyles__FullHeightWrapper-sc-du5f0h-0 MediumLayout__Container-sc-q6qal1-0 esWQar gjSZca']/main[@class='MediumLayout__CenterWithPadding-sc-q6qal1-1 jDCQpS']/div[@class='MediumLayout__BodyWrapper-sc-q6qal1-2 jaGElF']/div[@class='MediumLayout__BodyLeft-sc-q6qal1-3 fotkOp']/div[@class='MediumLayout__PaginationWrapper-sc-q6qal1-5 fGjzWP']/div/div[@class='Pagination__Wrapper-sc-uamu6s-2 fJxvFR']/a[@class='Pagination__Button-sc-uamu6s-1 Pagination__PrevNextButton-sc-uamu6s-7 jUbFsW iHgjRU']"):
        
        if counterTwo >= 1:
            
            driver.execute_script("arguments[0].click();", elementName)
        counterTwo += 1   
    if counter <= 1:
        nextButton = driver.find_element("xpath", "/html/body/div[@id='__next']/div[@class='LayoutStyles__FullHeightWrapper-sc-du5f0h-0 MediumLayout__Container-sc-q6qal1-0 esWQar gjSZca']/main[@class='MediumLayout__CenterWithPadding-sc-q6qal1-1 jDCQpS']/div[@class='MediumLayout__BodyWrapper-sc-q6qal1-2 jaGElF']/div[@class='MediumLayout__BodyLeft-sc-q6qal1-3 fotkOp']/div[@class='MediumLayout__PaginationWrapper-sc-q6qal1-5 fGjzWP']/div/div[@class='Pagination__Wrapper-sc-uamu6s-2 fJxvFR']/a[@class='Pagination__Button-sc-uamu6s-1 Pagination__PrevNextButton-sc-uamu6s-7 jUbFsW iHgjRU']")
        driver.execute_script("arguments[0].click();", nextButton)        
    time.sleep(3)

#print(price)
#print(name)

for a in range(len(price)):
    
    placeholder = ''
    placeholder = 'price:' + str(price[a]) + '  ' +  'name:' + str(name[a])
    pricename.append(placeholder)
#print(pricename)
#print(pricename)
print("""










""")
#sorting
sortList = []



#sort by price funcion
def priceSort():
    
    if underOver:
        
        for i in range(len(price)):
            #counter =+ 1
            #print(price[i])
            try:    
                if price[i] <= underOverValue:
                    placeholderTwo = ''
                    placeholderTwo = 'name: ' + str(name[i]) + ' price: ' + str(price[i])
                    #print(2)
                    sortList.append(placeholderTwo)
                    #print(1)
            except:
                #print('invalid price')
                pass
        #print(sortList)
    else:
        for i in range(len(price)):
            #counter =+ 1
            #print(price[i])
            try:    
                if price[i] <= underOverValue:
                    placeholderTwo = ''
                    placeholderTwo = 'name: ' + str(name[i]) + ' price: ' + str(price[i])
                    sortList.append(placeholderTwo)
            except:
                #print('invalid price')
                pass
        #print(sortList)
                
priceSort()
#print(sortList)
#keyword sort
keywordSortList = []
def keywordSort():
    keywords =['m1','m2','2020']
    for c in sortList:
        for o in keywords:
            if o in c:
                keywordSortList.append(c)
                #print('sss')
            else:
                pass
    print(keywordSortList)
                

keywordSort()

    

time.sleep(14)
        
#for i in children:
#    
#    driver.implicitly_wait(3)
#    print(i.get_attribute('aria-label'))
#time.sleep(15)
# driver.quit()
