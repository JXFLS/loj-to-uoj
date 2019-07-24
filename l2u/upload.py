# -*- coding:utf-8 -*-

# By Terrasse
# 自动上传

from selenium import webdriver as wd
from time import sleep as slp
from selenium.webdriver.common.keys import Keys
from .info import get_name
from .file import get_dir
from os import path

url = "https://www.jxoj.net"


def init():
    ff_options = wd.firefox.options.Options()
    ff_options.add_argument('--headless')
    work = wd.Firefox(options=ff_options)
    return work


def login(work):
    file = open("administrator.inf", 'r')
    username = file.readline()[:-1]
    password = file.readline()[:-1]
    file.close()
    work.get(url + "/login")
    slp(2)
    work.find_element_by_id("input-username").send_keys(username)
    work.find_element_by_id("input-password").send_keys(password)
    slp(1)
    work.find_element_by_id("button-submit").click()
    slp(1)
    work.get(url + "/problems")
    slp(1)
    return


def adp(work):
    work.find_element_by_id("button-submit-new_problem").click()
    slp(1)
    work.switch_to.alert.accept()
    slp(1)
    return


def put_face(work, name, md):
    work.find_element_by_xpath("//tbody/tr[last()]/td[2]/a").click()
    slp(1)
    work.find_element_by_xpath("//ul[@role='tablist']/li[last()]/a").click()
    slp(1)
    work.find_element_by_id(
        "input-problem_title").send_keys(Keys.BACKSPACE * 12, name)
    slp(1)
    work.find_elements_by_tag_name("textarea")[1].send_keys(md)
    slp(1)
    work.find_elements_by_tag_name("textarea")[1].send_keys(Keys.CONTROL, 's')
    work.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
    slp(2)
    work.find_element_by_xpath("//ul[@role='tablist']/li[3]/a").click()
    slp(2)
    return


def put_zip(work, zip):
    work.find_element_by_xpath(
        "//button[@data-target='#UploadDataModal']").click()
    slp(1)
    work.find_element_by_id("problem_data_file").send_keys(zip)
    slp(2)
    work.find_element_by_xpath(
        "//div[@class='modal-footer']/button[@type='submit']").click()
    slp(1)
    work.switch_to.alert.accept()
    slp(1)
    work.find_element_by_id("button-submit-hackable").click()
    slp(1)
    work.switch_to.alert.accept()
    slp(1)
    return


def push(pid):
    try:
        work = init()
        name = get_name(pid)
        file = open(get_dir(pid) + "problem.md")
        md = file.read()
        file.close()
        zip = path.abspath(get_dir(pid) + "uoj.zip")
        login(work)
        adp(work)
        put_face(work, name, md)
        put_zip(work, zip)
    except Exception as e:
        print(str(e))
        input("PAUSE")
    work.quit()
    return
