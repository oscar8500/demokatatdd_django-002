__author__ = 'asistente'
from unittest import TestCase

from selenium import webdriver


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    # def test_t1(self):#titulo
    #     self.browser.get('http://localhost:8000')
    #     self.assertIn('Busco Ayuda', self.browser.title)

    # def test_t2(self):#registro
    #     self.browser.get('http://localhost:8000')
    #     link = self.browser.find_element_by_id('id_register')
    #     link.click()
    #
    #     nombre = self.browser.find_element_by_id('id_nombre')
    #     nombre.send_keys('Juan Daniel')
    #
    #     apellidos = self.browser.find_element_by_id('id_apellidos')
    #     apellidos.send_keys('Arevalo')
    #
    #     experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
    #     experiencia.send_keys('5')
    #
    #     self.browser.find_element_by_xpath(
    #         "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
    #     telefono = self.browser.find_element_by_id('id_telefono')
    #     telefono.send_keys('3173024578')
    #
    #     correo = self.browser.find_element_by_id('id_correo')
    #     correo.send_keys('jd.patino1@uniandes.edu.co')
    #
    #     imagen = self.browser.find_element_by_id('id_imagen')
    #     imagen.send_keys('C:\imagen.png')
    #
    #     nombreUsuario = self.browser.find_element_by_id('id_username')
    #     nombreUsuario.send_keys('juan645')
    #
    #     clave = self.browser.find_element_by_id('id_password')
    #     clave.send_keys('clave123')
    #
    #     botonGrabar = self.browser.find_element_by_id('id_grabar')
    #     botonGrabar.click()
    #     self.browser.implicitly_wait(3)
    #     span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
    #
    #     self.assertIn('Juan Daniel Arevalo', span.text)

    # def test_t3(self):#ver detalle
    #     self.browser.get('http://localhost:8000')
    #     span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
    #     span.click()
    #     self.browser.implicitly_wait(3)
    #
    #     h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')
    #
    #     self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_t4(self):  # Login
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')
        # clave = self.browser.find_element_by_id('id_password')
        #clave.send_keys('clave123')

        # enviar = self.browser.find_element_by_id('id_grabar')
        #enviar.click()

        # link = self.browser.find_element_by_id('id_logout')
        # self.assertIsNotNone(link)
        #msg = self.browser.find_element_by_class_name('alert alert-danger error float-message')
