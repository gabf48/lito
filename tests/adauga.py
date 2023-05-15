import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.asserts import Asserts
from pages.cos_page import Cos
from pages.handle_rezervare import HandleRezervare
from pages.login_page import LoginPage
from pages.cauta_hotel import CautaHotelPage

NUMAR_CAMERE = ''


def test_adauga_in_cos():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    cauta_hotel = CautaHotelPage(driver)
    handle_rezervare = HandleRezervare(driver)
    cos_page = Cos(driver)
    asserts = Asserts(driver)


    #login
    login_page.login('https://www.stgtourop.litoralulromanesc.ro/','wesrom','lsajkacs2osj')
    time.sleep(5)

    #cauta hotel
    cauta_hotel.selecteaza_statiune('Mamaia')
    cauta_hotel.apasa_cautare()
    time.sleep(15)

    #memoreza numar camere disponibile
    NR_1 = handle_rezervare.stocheaza_numere_camere_disponibile()
    print(NR_1)

    #adauga camera in cos
    handle_rezervare.apasa_adaugare_in_cos()
    time.sleep(2)

    #adauga cleint existent
    handle_rezervare.completeaza_adauga_client_existent_formular('gabriel.filip@wesrom.com')
    time.sleep(10)

    #verifica sa fie adaugata o camera in cos
    cos_page.verifica_numar_camere_cos('1')

    #verifica existenta butoanelor Rezerva si Oferteaza
    cos_page.deschide_cos()
    asserts.verifica_exitenta_selector_pe_pagina('[id="js-rezerva-inscrieri"]')
    asserts.verifica_exitenta_selector_pe_pagina('[id="js-rezerva-oferte"]')
    time.sleep(10)

    #verifica numarul de camere disponibile sa fie scazut cu unu
    handle_rezervare.stocheaza_numere_camere_disponibile()
    NR_2 = handle_rezervare.stocheaza_numere_camere_disponibile()
    print('NR 1 = ',NR_1)
    print('NR 2 = ',NR_2)
    a = NR_1.replace(' ','')
    b = NR_2.replace(' ','')
    c = int(a)-int(b)
    print(c)
    int_num1 = int(a)
    int_num2 = int(b)
    NR_3 = int_num1 - int_num2
    print(NR_3)
    assert NR_3 == 1
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)

    #mai adauga o camera in cos
    handle_rezervare.apasa_adaugare_in_cos()
    time.sleep(10)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.UP)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.UP)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.UP)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.UP)
    driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.UP)

    #verifica sa fie afisate doua camere in cos
    cos_page.verifica_numar_camere_cos('2')
    NR_4 = handle_rezervare.stocheaza_numere_camere_disponibile()
    assert NR_4 - NR_2 == 1
