import sys
import os
import allure
import uuid
from allure_commons.types import AttachmentType
from playwright.sync_api import sync_playwright

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/../../')

from config import admin_password, HOST
from helpers.api import Api
from helpers.action import ClassAction


# def before_all(context):
#     pass


def before_scenario(context, scenario):
    if "skip" in scenario.effective_tags:
        scenario.skip("Marked with @skip")
        return

    with allure.step('------------------Старт Сценария------------------'):
        # Используем HOST из config.py, если не передан через userdata
        if 'HOST' in context.config.userdata.keys():
            context.host = context.config.userdata['HOST']
        else:
            context.host = HOST

        # behave -D BROWSER=chrome
        if 'BROWSER' in context.config.userdata.keys():
            BROWSER = context.config.userdata['BROWSER']
        else:
            BROWSER = 'chrome'

        p = sync_playwright().start()
        context.playwright = p

        # behave -D HEADLESS
        HEADLESS = True if 'HEADLESS' in context.config.userdata.keys() else False

        if BROWSER == 'chrome':
            context.browser = p.chromium.launch(headless=HEADLESS)
        elif BROWSER == 'firefox':
            context.browser = p.firefox.launch(headless=HEADLESS)

        context.playwright_context = context.browser.new_context()
        context.playwright_context.tracing.start(screenshots=True, snapshots=True, sources=True)

        # Создаем страницу и открываем сайт автоматически
        context.page = context.playwright_context.new_page()
        page = ClassAction(context)
        page.visit(context.host)


def after_scenario(context, scenario):
    with allure.step('------------------Финиш Сценария------------------'):
        try:
            name = str(uuid.uuid4())
            allure.attach(context.page.screenshot(path=f"{name}.png"), name=f"{name}.png",
                          attachment_type=AttachmentType.PNG)
            allure.attach(context.playwright_context.tracing.stop(path=f'{name}.zip'), name=f'{name}.zip')
            context.browser.close()
            context.playwright.stop()
        except:
            context.browser.close()
            context.playwright.stop()

def after_all(context):
    """Очистка тестовых данных после выполнения всех тестов."""
    with allure.step('------------------Очистка тестовых данных------------------'):
        api = Api(HOST)
        api.post("api/admin/reset-bookings", json={"password": admin_password})
