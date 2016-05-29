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

def before_all(context):
    print("Executing before all")


def before_feature(context, feature):
    print("Before feature\n")


# Scenario level objects are popped off context when scenario exits
def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    print("Before scenario\n")


def after_scenario(context, scenario):
    context.browser.quit()
    print("\nAfter scenario")


def after_feature(context, feature):
    print("\nAfter feature")


def after_all(context):
    print("Executing after all")
