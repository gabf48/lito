import time

from selenium import webdriver
from pages.login_page import LoginPage
from pages.cauta_hotel import CautaHotelPage



def test_adauga_in_cos():
    driver = webdriver.Chrome()

    login_page = LoginPage(driver)
    cauta_hotel = CautaHotelPage(driver)

    login_page.login('https://www.stgtourop.litoralulromanesc.ro/','wesrom','lsajkacs2osj')
    time.sleep(5)
    cauta_hotel.selecteaza_statiune('Mamaia')

    time.sleep(15)