from util.utils import element_exists_by_css_selector


class Register:
    def __init__(self, driver):
        self.address = 'https://www.fitatu.com/app/create-account'
        self.driver = driver

    def registration_form(self):
        return {
        'email' : self.driver.find_element_by_css_selector('[name="email"]'),
        'password' : self.driver.find_element_by_css_selector('[name="password"]'),
        'agreement_checkbox' : self.driver.find_element_by_css_selector('[data-key="acceptTerms"]'),
        'age_checkbox': self.driver.find_element_by_css_selector('[data-key="acceptAgeRequirements"]'),
        'sensitive_checkbox': self.driver.find_element_by_css_selector('[data-key="sensitiveAccepted"]')
        }

    def submit_registration(self):
        return self.driver.find_element_by_css_selector("button.test-id--register")

    def fill_form(self, data):
        self.driver.get(self.address)
        self.registration_form()['email'].send_keys(data['email'])
        self.registration_form()['password'].send_keys(data['password'])
        self.registration_form()['agreement_checkbox'].click()
        self.registration_form()['age_checkbox'].click()
        self.registration_form()['sensitive_checkbox'].click()
        self.submit_registration().click()

    def test_empty_form_validation_errors_present(self, data):
        self.fill_form(data)
        return (element_exists_by_css_selector('label[data-labeled-input-text="Adres e-mail"]>span.validation__message', self.driver)
                and element_exists_by_css_selector('label[data-labeled-input-text="Hasło (od 6 do 32 znaków)"]>span.validation__message', self.driver)
                )

    def test_successful_registration(self, data):
        self.fill_form(data)
        return element_exists_by_css_selector('div.menu__user', self.driver)



