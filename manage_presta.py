from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
import mysql.connector

class Prestashop:
    def __init__(self):
        my_options = Options()
        my_options.add_argument('--profile-directory=Default')
        self.driver = webdriver.Chrome(options=my_options)
        self.driver.implicitly_wait(10)
    def install(self):
        self.driver.get('http://localhost:8080')
        self.driver.find_element_by_id('btNext').click()
        self.driver.find_element_by_id('set_license').click()
        self.driver.find_element_by_id('btNext').click()
        self.driver.find_element_by_id('btNext').click()
        self.driver.find_element_by_id('infosShop').send_keys('Sweet')
        self.driver.find_element_by_id('infosActivity_chosen').click()
        self.driver.find_element_by_css_selector('#infosActivity_chosen>div>ul>li:nth-child(6)').click()
        self.driver.find_element_by_id('infosFirstname').send_keys('Maya')
        self.driver.find_element_by_id('infosName').send_keys('Kaya')
        self.driver.find_element_by_id('infosEmail').send_keys('jayafour@gmail.com')
        self.driver.find_element_by_id('infosPassword').send_keys('P!3issweet')
        self.driver.find_element_by_id('infosPasswordRepeat').send_keys('P!3issweet')
        self.driver.find_element_by_id('btNext').click()
        db_server_field = self.driver.find_element_by_id('dbServer')
        db_server_field.clear()
        db_server_field.send_keys('jaya-mysql')
        self.driver.find_element_by_id('dbPassword').send_keys('Yahoo123')
        self.driver.find_element_by_id('btNext').click()
        try:
            element = WebDriverWait(self.driver, 300).until(
                EC.visibility_of_element_located((By.ID, "install_process_success"))
            )
        finally:
            subprocess.call('./cleanup_prestashop_installation.sh', shell=True)
            print("Install success!")
    @staticmethod
    def reset_mysql():
        presta_mysql = mysql.connector.connect(host="localhost", user="root", password="Yahoo123")
        presta_mysql_cursor = presta_mysql.cursor()
        presta_mysql_cursor.execute("CREATE DATABASE prestashop")
        presta_mysql.commit()
        presta_mysql_cursor.close()
        presta_mysql.close()
        print("Prestashop database created")
    @staticmethod
    def presta_mysql_docker_reset():
        subprocess.call('./reset_prestashop_mysql_docker.sh', shell=True)
        time.sleep(15)
        print("Docker containers reset")
    def manage_backend(self):
        self.driver.get('http://localhost:8080/secret_admin')
        self.driver.find_element_by_id('email').send_keys('jayafour@gmail.com')
        self.driver.find_element_by_id('passwd').send_keys('P!3issweet')
        self.driver.find_element_by_id('submit_login').click()
        self.driver.find_element_by_id('stay_logged_in').click()
        print("Log in success")
        self.driver.find_element_by_css_selector("body > div.onboarding-popup.bootstrap > div > div > i").click()



p = Prestashop()
p.presta_mysql_docker_reset()
p.reset_mysql()
p.install()
p.manage_backend()
