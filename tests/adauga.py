import time

from selenium import webdriver

from pages.handle_rezervare import HandleRezervare
from pages.login_page import LoginPage
from pages.cauta_hotel import CautaHotelPage



def test_adauga_in_cos():
    driver = webdriver.Chrome(executable_path='C:/Users/filip/PycharmProjects/lito/browsers/chromedriver.exe')

    login_page = LoginPage(driver)
    cauta_hotel = CautaHotelPage(driver)
    handle_rezervare = HandleRezervare(driver)

    login_page.login('https://www.stgtourop.litoralulromanesc.ro/','wesrom','lsajkacs2osj')
    time.sleep(5)
    cauta_hotel.selecteaza_statiune('Mamaia')
    cauta_hotel.apasa_cautare()
    time.sleep(15)

    handle_rezervare.apasa_adaugare_in_cos()
    time.sleep(15)