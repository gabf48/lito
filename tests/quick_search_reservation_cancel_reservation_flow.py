import time

from selenium import webdriver

from pages.adauga_client import AdaugaClient
from pages.adaugare_turisti import AdaugareTuristi
from pages.cauta_hotel import CautaHotelPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
def test_quick_search_reservation_cancel_reservation():
    driver = webdriver.Chrome(
        executable_path='C:/projects python/lito/browsers/chromedriver.exe')

    login_page = LoginPage(driver)
    basepage = BasePage(driver)
    cauta_hotel = CautaHotelPage(driver)
    adauga_client = AdaugaClient(driver)
    adaugare_turisti = AdaugareTuristi(driver)

    login_page.login('https://www.stgtourop.litoralulromanesc.ro/', 'wesrom', 'lsajkacs2osj')
    time.sleep(10)
    cauta_hotel.selecteaza_statiune("Mamaia")
    time.sleep(2)
    cauta_hotel.calendar_numar_luni_in_fata(2)
    time.sleep(5)

    basepage.zoom_out(6)
    time.sleep(6)
    cauta_hotel.rezerva_camera_allotment_random()
    basepage.zoom_in(6)
    time.sleep(5)
    adauga_client.adauga_client("gabriel.filip@wesrom.com")
    time.sleep(5)
    basepage.zoom_out(3)
    adaugare_turisti.rezerva_rezervarea()
    time.sleep(200)

