__author__ = 'asistente'
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_t1(self):  # test_title
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_t2(self):  # test_registro
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\imagen.png')

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_t3(self):  # test_verDetalle
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        self.browser.implicitly_wait(3)

        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_t4(self):  # test_login
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_username1')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password1')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_entrar')
        botonGrabar.click()

        self.browser.implicitly_wait(3)
        span = self.browser.find_elements_by_class_name("glyphicon-log-out")
        self.assertTrue(len(span) > 0)

    def test_t5(self):  # Editar
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_login')
        link.click()

        nombreUsuario = self.browser.find_element_by_id('id_username1')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password1')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_entrar')
        botonGrabar.click()

        self.browser.implicitly_wait(5)
        link = WebDriverWait( self.browser, 60).until(EC.presence_of_element_located((By.ID, 'id_editar')))
        #visibility_of_element_located
        link.click()

        self.browser.implicitly_wait(5)

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.clear()
        experiencia.send_keys('1')

        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.clear()
        telefono.send_keys('3164177888')

        imagen = self.browser.find_element_by_id('id_imagen')
        imagen.send_keys('C:\imagen.png')

        self.browser.implicitly_wait(5)

        botonGrabar = self.browser.find_element_by_id('id_modificar')
        botonGrabar.click()
        self.browser.implicitly_wait(5)

        link = self.browser.find_element_by_id('id_logout')

        self.assertIsNotNone(link)

    def test_t6(self):  #test_comentar
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        self.browser.implicitly_wait(3)

        correo = self.browser.find_element_by_id('correo')
        correo.send_keys('1@1.com')
        comentario= self.browser.find_element_by_id('comentario')
        comentario.send_keys('Este es un comentario. Le vendi mi alma a satan para terminar este taller')
        botonGrabar = self.browser.find_element_by_id('id_submitComentario')
        botonGrabar.click()

        p = self.browser.find_element(By.XPATH,
                                      '//p[text()="Este es un comentario. Le vendi mi alma a satan para terminar este taller"]')
        self.assertIn('Este es un comentario. Le vendi mi alma a satan para terminar este taller', p.text)
