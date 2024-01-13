from data import resource
from pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Hugo')
    registration_page.fill_last_name('Boss')
    registration_page.fill_email('test@email.com')
    registration_page.fill_gender()
    registration_page.fill_phone('1234567891')
    registration_page.fill_date_of_birth('1990', 'June', '22')
    registration_page.fill_subjects('Computer Science')
    registration_page.fill_hobbies()
    registration_page.fill_avatar(resource.path('foto.jpg'))
    registration_page.fill_address('New York')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Delhi')
    registration_page.fill_submit()
    # THEN
    registration_page.should_registered_user_with(
        'Hugo Boss',
        'test@email.com',
        'Female',
        '1234567891',
        '22 June,1990',
        'Computer Science',
        'Sports',
        'foto.jpg',
        'New York',
        'NCR Delhi',
    )
