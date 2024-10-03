from selene import browser, be, have


def test_have_result():
    browser.open('')
    browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
    browser.element('[class="b-header__menu"]').should(have.text('Решения'))
    browser.element('[class="b-header__menu"]').should(have.text('Продукты'))
    browser.element('[class="b-header__menu"]').should(have.text('Центры компетенций'))
    browser.element('[class="b-header__menu"]').should(have.text('Закупки'))
    browser.element('[class="b-header__menu"]').should(have.text('Мероприятия'))
    browser.element('[class="b-header__menu"]').should(have.text('Карьера'))
    browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))


def test_have_do_not_have_result():
    browser.open('')
    browser.element('[class="b-header__search"]').click()
    browser.element('[name="q"]').click()
    browser.element('[name="q"]').type('2024').press_enter()
    browser.element('[class="b-layout__main-content"]').should(have.text('2024'))


def test_have_do_not_have_result1():
    browser.open('')
    browser.element('[class="b-header__button"]').should(have.text('Написать нам'))
    browser.element('[class="b-header__button"]').click()
    browser.element('[id="cboxLoadedContent"]').should(have.text('Написать нам'))
    browser.element('[id="cboxClose"]').click()


def test_have_do_not_have_result1():
    browser.open('')
    browser.element('a[class="cbox-inline"]').click()
    browser.element('[class="b-header__button"]').click()
    browser.element('[id="cboxLoadedContent"]').should(
        have.text('Осуществляя взаимодействие с Т1 по электронной почте, я выражаю согласие на '))
    browser.element('[id="cboxClose"]').click()


def test_have_do_not_have_result2():
    browser.open('')
    browser.element('[class="c-center-all"]').should(have.text('Презентация о холдинге'))
    browser.element('[class="c-center-all"]').click()
    browser.element('[id="cboxLoadedContent"]').should(have.text('Скачать презентацию'))
    browser.element('[id="cboxClose"]').click()


def test_have_do_not_have_result3():
    browser.open('')
    browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
    browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[1]/a").click()
    browser.element('[class="b-layout__main-content"]').should(have.text('О Холдинге Т1'))


def test_have_do_not_have_result4():
    browser.open('')
    browser.element(css_or_xpath_or_by="/html/body/div[3]/footer/div/div[1]/div[4]/div[2]/a[3]").click()
    browser.element('[class="b-header__button"]').click()
    browser.element('[id="cboxLoadedContent"]').should(
        have.text('Осуществляя взаимодействие с Т1 по электронной почте, я выражаю согласие на '))
    browser.element('[id="cboxClose"]').click()


def test_have_do_not_have_result4():
    browser.open('')
    browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").should(
        have.text('Презентация о холдинге'))
    browser.element(css_or_xpath_or_by="/html/body/div[3]/main/div[2]/div[12]/span").click()
    browser.element('[id="cboxLoadedContent"]').should(have.text('Скачать презентацию'))
    browser.element('[id="cboxClose"]').click()
