from POMproject.Locators.locators import locators

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = locators.welcome_link_id
        self.logout_link_linktext = locators.logout_link_linktext

    def click_welcome(self):
        self.driver.find_element_by_id(locators.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(locators.logout_link_linktext).click()
