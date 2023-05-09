class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        login_link = self.browser.get(self.url)
