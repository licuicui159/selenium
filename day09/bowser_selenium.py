from selenium import  webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# options = webdriver.FirefoxOptions()
# options.add_argument('--headless')

browser = webdriver.Firefox()
base_url = 'https://mail.qq.com/'
browser.get(base_url)
# element = browser.find_element(By.LINK_TEXT,'设置')
# ActionChains(browser).move_to_element(element).perform()
login_frame = browser.find_element(By.ID,'login_frame')
browser.switch_to.frame(login_frame)

browser.find_element(By.ID,'u').send_keys('765512581')
browser.find_element(By.ID,'p').send_keys('weidongdong1212')
browser.find_element(By.ID,'login_button').click()






# browser.save_screenshot('baidu.png')
#
# browser.find_element(By.ID,'kw').send_keys('赵丽颖')
# browser.find_element(By.ID,'kw').send_keys(Keys.ENTER)

# browser.find_element(By.ID,'su').click()
#
# sleep(2)
# browser.quit()

