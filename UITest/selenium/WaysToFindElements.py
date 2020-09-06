from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.maximize_window()
        sleep(2)

    # def test_id(self):
    #     element = self.driver.find_element_by_id('kw')
    #     element.send_keys('极客时间')
    #     print(element)
    #     print(type(element))
    #     self.driver.find_element_by_id('su').click()
    #     sleep(3)
    #     # self.driver.quit()
    #
    # def test_name(self):
    #     self.driver.find_element_by_name('wd').send_keys('极客时间')
    #     self.driver.find_element_by_id('su').click()
    #     sleep(3)
    #     self.driver.quit()
    #
    # def test_xpath(self):
    #     element = self.driver.find_element_by_xpath('//*[@id="kw"]')
    #     element.send_keys('极客时间')
    #     self.driver.find_element_by_xpath('//*[@id="su"]').click()
    #     sleep(2)
    #     self.driver.quit()
    #
    # def test_link(self):
    #     self.driver.find_elements_by_link_text('hao123')[0].click()
    #     sleep(2)
    #     self.driver.quit()
    # #
    # def test_partial_link(self):
    #     self.driver.find_element_by_partial_link_text('123').click()
    #     sleep(5)
    #     self.driver.find_element_by_link_text('地图').click()
    #     sleep(3)
    # self.driver.quit()

    #
    # def test_tag_name(self):
    #     input = self.driver.find_element_by_tag_name('input')[0]
    #     print(input)
    #     self.driver.quit()
    #
    # def test_class_name(self):
    #     self.driver.find_element_by_class_name('s_ipt').send_keys('极客时间')
    #     self.driver.find_element_by_id('su').click()
    #     sleep(3)
    #     self.driver.quit()
    #
    # def test_css_selector(self):
    #     self.driver.find_element_by_css_selector('#kw').send_keys('极客时间')
    #     self.driver.find_element_by_id('su').click()
    #     sleep(3)
    #     self.driver.quit()
    #
    # def test_all(self):
    #     self.driver.find_element(By.ID, value='kw').send_keys('极客时间')
    #     self.driver.find_element_by_id('su').click()
    #     sleep(3)
    #     self.driver.quit()

    def test_prop(self):
        print(self.driver.name)
        print(self.driver.current_url)
        print(self.driver.title)
        print(self.driver.window_handles)
        print(self.driver.page_source)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_id('kw').send_keys('极客时间')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.back()
        sleep(2)
        self.driver.refresh()
        sleep(2)
        self.driver.forward()
        sleep(2)

        self.driver.close()
        sleep(2)

        self.driver.quit()

        wb = WebElement()


if __name__ == "__main__":
    case = TestCase()
    # case.test_partial_link()
    # case.test_prop()
    case.test_method()
    # case.test_id()
    # case.test_xpath()
    # case.test_name()
    # case.test_link()
    # case.test_partial_link()
    # case.test_tag_name()
    # case.test_class_name()
    # case.test_css_selector()
    # case.test_all()
