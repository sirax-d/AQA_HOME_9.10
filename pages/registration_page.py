from selene import have, command
from selene import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#state')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]').element_by(have.value('Female')).element('..')
        self.phone = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element("[for='hobbies-checkbox-1']")
        self.avatar = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.submit = browser.element('#submit')
    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self
    def fill_gender(self):
        self.gender().click()
        return self

    def fill_phone(self, value):
        self.phone.type(value)
        return self

    def fill_subjects(self, value):
        self.subjects.type(value).press_enter()
        return self

    def fill_hobbies(self):
        self.hobbies.click()
        return self
    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_avatar(self, path):
        self.avatar.set_value(path)
        return self

    def fill_address(self, value):
        self.address.type(value)
        return self
    def fill_state(self, name):
        browser.element('#react-select-3-input').type(name).press_enter()
        return self

    def fill_city(self, name):
        browser.element('#react-select-4-input').type(name).press_enter()
        return self

    def fill_submit(self):
        self.submit.press_enter()
        return self

    def should_registered_user_with(self, full_name, email, gender, phone, date_of_birth, subjects, hobbies, avatar, address, state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                phone,
                date_of_birth,
                subjects,
                hobbies,
                avatar,
                address,
                state,
            )
        )
        return self
