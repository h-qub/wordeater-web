# coding=utf-8

import unittest
from dal_test_base import BaseTest
from services.service_locator import ServiceLocator
from services.real.translate import TranslateService
from services.mocks.yandex_translate import YandexTranslateFake

__author__ = 'Glebov Boris'


class TranslationTest(BaseTest):
    def setUp(self):
        BaseTest.setUp(self)

        self.ts = TranslateService()
        self.ts.engine = YandexTranslateFake()

        self.create_demo_session()

        ServiceLocator.register(ServiceLocator.TRANSLATIONS, self.ts)


class TranslationTranslateTest(TranslationTest):
    """
    Test all case for translate method
    """

    def test_translate_new_word(self):
        """
        Translate new word. Save in DB.

        1. Check that translate is true
        2. Checks that word preserved in DB
        :return:
        """
        self.clear_db()

        translation = self.ts.translate(u'dog', u'en-ru')
        self.assertIsNotNone(translation)
        self.assertEqual(translation.variations[0], u'собака')
        self.assertEqual(translation.author, u'user1')

    def test_translate_word_exists_in_cache(self):
        """
        Detect what word exists in cache, extract it from DB and send to user
        :return: Translation entity
        """
        self.clear_db()

        translation1 = self.ts.translate(u'dog', u'en-ru')
        translation2 = self.ts.translate(u'dog', u'en-ru')

        self.assertEqual(translation1.id, translation2.id)
