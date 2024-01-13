from data.users import admin
from pages.registration_page import HighLevelRegistrationPage

def test_registration_form():
    reg = HighLevelRegistrationPage()
    reg.registration(admin)
    reg.should_registered_user_with(admin)
