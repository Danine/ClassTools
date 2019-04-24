from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get("http://bkjws.sdu.edu.cn/")
driver.find_element_by_name("j_username").send_keys("201618130133")
driver.find_element_by_name("j_password").send_keys("110520")
driver.find_element_by_id("loginButtonId").click()

driver.implicitly_wait(10)

driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[9]/a/span[1]").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/ul/li[9]/ul/li[1]/a").click()

driver.implicitly_wait(2)
time.sleep(1)

temp = driver.find_elements_by_tag_name('tbody')[2].find_elements_by_tag_name('tr')
row = len(temp)
for j in range(row):
    if driver.find_element_by_xpath("//*[@id='dataTableId']/tbody/tr["+str(j+1)+"]/td[4]/font") != 0:
        driver.find_element_by_xpath("//*[@id='dataTableId']/tbody/tr["+str(j+1)+"]/td[5]/a").click()
        for i in range(19):
            driver.find_elements_by_id('zbda_'+str(i))[0].click()
        #special
        driver.find_elements_by_id('zbda_19')[2].click()
        driver.find_elements_by_id('zbda_20')[0].click()
        driver.find_element_by_id('zbda_21').send_keys("老师讲课思路清晰，认真负责")
        submit = driver.find_elements_by_class_name('red')[0]
        ActionChains(driver).
        submit.click()
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]").click()
    else:
        continue
time.sleep(5)


# table = driver.find_elements_by_id('dataTableId')
# for i in table:
#     table_tr = i.find_element_by_tag_name('tr')
#     if table_tr.find_element_by_tag_name('td')[4].txt == 0:
#         table_tr.find_element_by_tag_name('td')[5].click()
#     else:
#         print(table_tr.find_element_by_tag_name('td')[4].txt)
#     if driver.find_element_by_xpath("//*[@id='dataTableId']/tbody/tr[1]/td[4]/font") == 0:
#         driver.find_element_by_xpath("//*[@id='dataTableId']/tbody/tr[1]/td[5]/a").click()

#     if i.value == "5.0":
#         i.click()
#         time.sleep(5)
