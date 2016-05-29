from behave import *
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.common.exceptions import WebDriverException
import unittest
import time
import traceback

use_step_matcher("re")


@given("I open Let's Talk Tea page")
def step_impl(context):
    context.browser.get("http://www.practiceselenium.com/let-s-talk-tea.html")
    pass


@then("I complete the form")
def step_impl(context):

    name = context.browser.find_element_by_name("name").send_keys("Dwindy Stanza")
    email = context.browser.find_element_by_name("email").send_keys("dwindy.stanza@live.com")
    subject = context.browser.find_element_by_name("subject").send_keys("Dummy subject")
    message = context.browser.find_element_by_name("message").send_keys("Dummy message")


@then("I leave name blank")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I enter 256 character on name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I add number or symbol on name")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I leave email blank")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then("I fill incorrect email format")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step("I submit")
def step_impl(context):
    button = context.browser.find_element_by_xpath('//*[@id="form_78ea690540a24bd8b9dcfbf99e999fea"]/div[1]/div[5]/input')
    button.click()
    try:
        WebDriverWait(context.browser, 10).until(EC.text_to_be_present_in_element_value((By.ID, 'msg_78ea690540a24bd8b9dcfbf99e999fea'), 'Thank you sending us your information. We will get back to you with your Chai :)'))
    except(Exception):
        traceback.print_exc()

#    context.browser.find_element_by_xpath('//*[@id="form_78ea690540a24bd8b9dcfbf99e999fea"]/div[1]/div[1]/input and @class="form-value form-value-invalid"')