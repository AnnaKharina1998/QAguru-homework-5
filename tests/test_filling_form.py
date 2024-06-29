import os
from selene import browser, have, command


def test_correct_filling():
    # заполнение данных

    browser.open("/automation-practice-form")
    # в качестве тестовых данных использую свои персональные данные, т.к.
    # библиотека fake для генерации случайных не разрешена к использованию
    first_name = 'Anna'
    last_name = 'Krasnokutskaia'
    email = 'anna.kharina.1998@mail.ru'
    mobile = '9099777874'
    birthday = '13 January,1998'
    subject = 'Chemistry'
    picture_name = 'my_cat_better_than_my_face.jpg'
    adress = 'Russia, Yaroslavskaya oblast, Yaroslavl,st. Pobedy, 13-12'
    state = 'NCR'
    city = 'Delhi'

    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(email)
    browser.element('[for="gender-radio-2"]').click()
    # не хорошо хардкодить, но создавать переменную и искать пол по тексту сильно сложнее,
    # в других чекбоксах аналогично
    browser.element('#userNumber').type(mobile)
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").type("1998").click()
    browser.element(".react-datepicker__month-select").element('[value="0"]').click()
    browser.element(".react-datepicker__day--013").click()
    browser.element('#subjectsInput').type(subject[:2]).press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(picture_name))
    browser.element('#currentAddress').perform(command.js.scroll_into_view).type(adress)
    # мы в Индии что ли? хорошо, что эта форма не проверяет адрес на соответствие по городу и штату
    browser.element("//div[@id='stateCity-wrapper']/descendant::input[1]").type(state).press_enter()
    browser.element("//div[@id='stateCity-wrapper']/descendant::input[2]").type(city).press_enter()
    # подтвердить заполнение
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    # проверка
    browser.element('.table').all('td').even.should(
        have.exact_texts(f'{first_name} {last_name}', email, 'Female', mobile, birthday, subject,
                         'Reading, Music', picture_name, adress, f'{state} {city}'))
