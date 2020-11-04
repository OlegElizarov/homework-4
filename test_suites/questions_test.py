from selenium import webdriver
import unittest

from pages.auth_page import AuthPage
from pages.ask_page import AskPage


class QuestionsTests(unittest.TestCase):
    TOPIC = 'Какую породу собаки выбрать?'
    LONG_TOPIC = 'a' * 121
    TEXT = 'Помогите выбрать породу'

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_page.login()

    def tearDown(self):
        self.driver.quit()

    def test_question_topic(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.TOPIC)
        ask_page.publish_question()
        self.assertEqual(ask_page.question_topic, self.TOPIC)

    def test_empty_topic(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_text(self.TEXT)
        ask_page.set_category()
        ask_page.set_subcategory()
        self.assertEqual(ask_page.is_button_disabled, True)

    def test_long_topic_error(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.LONG_TOPIC)
        self.assertEqual(ask_page.topic_has_error, True)

    def test_long_topic_button_disabled(self):
        ask_page = AskPage(self.driver)
        ask_page.open()
        ask_page.set_topic(self.LONG_TOPIC)
        self.assertEqual(ask_page.is_button_disabled, True)
