from selene import have, command, be, by, browser

from data import resource
from data.users import User, admin


class HighLevelRegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.state = browser.element('#react-select-3-input')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]').element_by(have.value('Female')).element('..')
        self.phone = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.element("[for='hobbies-checkbox-1']")
        self.avatar = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.submit = browser.element('#submit')
        self.city = browser.element('#react-select-4-input')
        self.user_birthday = browser.element('#dateOfBirthInput')
        self.month = browser.element('.react-datepicker__month-select')
        self.year = browser.element('.react-datepicker__year-select')
        self.day = browser.element(f'.react-datepicker__day--0{admin.dob}')

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)
        return self

    def registration(self, user: User):
        self.open()
        self.first_name.should(be.blank).type(user.firstname)
        self.last_name.should(be.blank).type(user.lastname)
        self.email.should(be.blank).type(user.email)
        self.gender.click()
        self.phone.should(be.blank).type(user.phone)
        self.user_birthday.click()
        self.month.click().element(by.text(user.mob)).click()
        self.year.click().element(by.text(user.yob)).click()
        self.day.click()
        self.subjects.type(user.subjects).press_enter()
        self.hobbies.click()
        self.avatar.send_keys(resource.path(user.avatar))
        self.address.type(user.address)
        self.state.type(user.state).press_enter()
        self.city.type(user.city).press_enter()
        self.submit.press_enter()

    def should_registered_user_with(self, user):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                user.firstname + ' ' + user.lastname,
                user.email,
                user.gender,
                str(user.phone),
                f'{user.dob} {user.mob},{user.yob}',
                user.subjects,
                user.hobbies,
                user.avatar,
                user.address,
                user.state + ' ' + user.city,
            )
        )
        return self
