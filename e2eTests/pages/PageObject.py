from selenium import webdriver


class PageObject:

    def __init__(self, driver=None, browser='chrome'):
        if driver:
            self.driver = driver
        else:
            if browser == 'chrome':
                self.driver = webdriver.Chrome()
            else:
                raise Exception('Browser não encontrado!')
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def is_page(self, url):
        is_url = self.driver.current_url == url
        return is_url
    