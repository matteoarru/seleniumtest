#!../venv python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 16:05:37 2020

@author: matteoarru
"""
from selenium import webdriver
import smtplib

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.worldometers.info/coronavirus/')
        table = self.driver.find_element_by_xpath('//*[@id="main_table_countries"]/tbody[1]')
        country_element = table.find_element_by_xpath("//tr[contains(text(), 'China')]")
        row = country_element.find_element_by_xpath("./..")
        data = row.text.split(" ")
        self.total_cases = data[1]
        self.new_cases = data[2]
        self.total_deaths = data[3]
        self.new_deaths = data[4]
        self.active_cases = data[5]
        self.total_recovered = data[6]
        self.serious_critical = data[7]
    def print_cases(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
        print(total_cases)
        print(new_cases)
        print(total_deaths)
        print(new_deaths)
        print(active_cases)
        print(total_recovered)
        print(serious_critical)
    
    def send_mail(country_element, total_cases, new_cases, total_deaths, new_deaths, active_cases, total_recovered, serious_critical):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('email', 'password')
        subject = 'Coronavirus stats in your country today!'
        body = 'Today in ' + country_element + '\
        \nThere is new data on coronavirus:\
        \nTotal cases: ' + total_cases +'\
        \nNew cases: ' + new_cases + '\
        \nTotal deaths: ' + total_deaths + '\
        \nNew deaths: ' + new_deaths + '\
        \nActive cases: ' + active_cases + '\
        \nTotal recovered: ' + total_recovered + '\
        \nSerious, critical cases: ' + serious_critical  + '\
        \nCheck the link: https://www.worldometers.info/coronavirus/'
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail(
        'Coronavirus',
        'email',
        msg
        )
        print('Hey Email has been sent!')
        server.quit()