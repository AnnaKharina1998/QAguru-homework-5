import os
from selene import browser, have, command


def test_correct_filling():
    # заполнение данных

    browser.open("/automation-practice-form")
    first_name = 'Vasya'
    last_name = 'Pupkin'
    email = 'some_email@mail.ru'
    gender = 'Female'
    mobile = '9099777874'
    birthday = '13 January,1998'
    subject = 'Chemistry'
    hobby = 'Music'
    picture_name = 'my_cat_better_than_my_face.jpg'
    adress = 'somwhere in India...'
    state = 'NCR'
    city = 'Delhi'

    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element(f"//label[contains(text(),'{gender}')]").click()
    browser.element('#userNumber').type(mobile)
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").type("1998").click()
    browser.element(".react-datepicker__month-select").element('[value="0"]').click()
    browser.element(".react-datepicker__day--013").click()
    browser.element('#subjectsInput').type(subject[:2]).press_enter()
    browser.element(f"//label[contains(text(),'{hobby}')]").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(picture_name))
    browser.element('#currentAddress').perform(command.js.scroll_into_view).type(adress)
    browser.element("//div[@id='stateCity-wrapper']/descendant::input[1]").type(state).press_enter()
    browser.element("//div[@id='stateCity-wrapper']/descendant::input[2]").type(city).press_enter()
    # подтвердить заполнение
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # проверка
    browser.element('.table').all('td').even.should(
        have.exact_texts(f'{first_name} {last_name}', email, gender, mobile, birthday, subject,
                         hobby, picture_name, adress, f'{state} {city}'))
