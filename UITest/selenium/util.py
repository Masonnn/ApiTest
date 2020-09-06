from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def get_element(driver, *loc):
    e = driver.find_element(*loc)
    return e


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')

    loc = (By.ID, 'su')

    get_element(driver, By.ID, 'kw').send_keys('极客时间')
    get_element(driver, *loc).click()
    sleep(3)
    driver.quit()
