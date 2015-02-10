from django.test import TestCase
import plyplus
import os


class RawsParsingTestCase(TestCase):
    def setUp(self):
        self.grammar = plyplus.Grammar(plyplus.grammars.open(
            os.getcwd() +
            '/raws_parser/dictionaries/base.g'),
            auto_filter_tokens=False)

    def test_parsing_action(self):
        """Parsing actually ends successful"""
        result = self.grammar.parse(open(os.getcwd() +
                                         '/packs/tests/test_item.txt').read())

    def test_elements(self):
        result = self.grammar.parse(open(os.getcwd() +
                                         '/packs/tests/test_item.txt').read())

        self.assertEqual(result.select('objects > object_stm *')[0],
                         '[OBJECT:ITEM]')
        self.assertEqual(result.select('token_item_name *')[:]
                         , ['ITEM_PANTS_PANTS', 'ITEM_PANTS_GREAVES'])

