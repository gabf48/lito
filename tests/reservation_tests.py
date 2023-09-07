import time

from selenium import webdriver

from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.nav_bar import NavBar
def test_reservation():
    driver = webdriver.Chrome(
        executable_path='D:/alvanda/browsers/chromedriver.exe')

    login_page = LoginPage(driver)
    basepage = BasePage(driver)
    nav_bar = NavBar(driver)

    login_page.login('https://www.stgtourop.litoralulromanesc.ro/', 'wesrom', 'lsajkacs2osj')
    time.sleep(5)
    nav_bar.select_specific_page_from_nav_bar("Cauta Rezervare")
    presence = False

    if basepage.assert_if_element_is_display_on_the_page(
            '[class="fa fa-pencil-square-o"]') or basepage.is_text_displayed('Nu exista nicio rezervare'):
                presence = True

    assert presence == True


