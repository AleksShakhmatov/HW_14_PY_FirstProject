import allure
from allure_commons.types import Severity
from selene import have, browser


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "AleksSH")
@allure.feature("Check content of site T1")
@allure.story("Work of elements")
def test_content_t_one():
    with allure.step("Open site"):
        browser.open('')

    with allure.step("Check header content"):
        browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
        browser.element('[class="b-header__menu"]').should(have.text('Решения'))
        browser.element('[class="b-header__menu"]').should(have.text('Продукты'))
        browser.element('[class="b-header__menu"]').should(have.text('Центры компетенций'))
        browser.element('[class="b-header__menu"]').should(have.text('Закупки'))
        browser.element('[class="b-header__menu"]').should(have.text('Мероприятия'))
        browser.element('[class="b-header__menu"]').should(have.text('Карьера'))
        browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))

    with allure.step("Check search"):
        browser.element('[class="b-header__search"]').click()
        browser.element('[name="q"]').click()
        browser.element('[name="q"]').type('2024').press_enter()
        browser.element('[class="b-layout__main-content"]').should(have.text('2024'))

    with allure.step("Check feedback"):
        browser.element('[class="b-header__button"]').should(have.text('Написать нам'))
        browser.element('[class="b-header__button"]').click()
        browser.element('[id="cboxLoadedContent"]').should(have.text('Написать нам'))
        browser.element('[id="cboxClose"]').click()

    with allure.step("Check feedback2"):
        browser.element('[class="b-header__menu"]').should(have.text('Холдинг'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[1]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('О Холдинге Т1'))

    with allure.step("Check feedback2"):
        browser.element('[class="b-header__menu"]').should(have.text('Пресс-центр'))
        browser.element(css_or_xpath_or_by="/html/body/div[3]/header/div/div/div[2]/div[2]/div[9]/a").click()
        browser.element('[class="b-layout__main-content"]').should(have.text('Пресс-центр'))
