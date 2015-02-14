from django.test import TestCase
import plyplus
import os

MODULE_DIR = os.getcwd() + '/raws_parser'
TEST_ASSETS = MODULE_DIR + '/tests/assets'


class RawsParsingTestCase(TestCase):
    def setUp(self):
        self.grammar = plyplus.Grammar(plyplus.grammars.open(
            MODULE_DIR + '/dictionaries/base.g'),
            auto_filter_tokens=False)

    def test_parsing_action(self):
        """Parsing actually ends successful"""
        self.grammar.parse(open(TEST_ASSETS + '/test_item.txt').read())

    def test_elements(self):
        result = self.grammar.parse(open(TEST_ASSETS + '/test_item.txt').read())

        self.assertEqual(result.select('main > object_stm *')[0],
                         '[OBJECT:ITEM]')
        self.assertEqual(result.select('token_item_name *')[:]
                         , ['ITEM_PANTS_PANTS', 'ITEM_PANTS_GREAVES'])


class TransformsTestCase(TestCase):
    def setUp(self):
        self.grammar = plyplus.Grammar(plyplus.grammars.open(
            MODULE_DIR + '/dictionaries/base.g'),
            auto_filter_tokens=False
        )
        self.result = self.grammar.parse(open(TEST_ASSETS + '/test_item.txt')
                                         .read())

    def test_json_formating(self):
        import json
        from raws_parser.tojson import MakeJson
        with open(TEST_ASSETS + '/test_json.json') as f:
            test_json = json.load(f)

        make_json = MakeJson()
        self.assertEqual(json.loads(make_json.transform(self.result.tail[0])),
                         test_json)

    def test_d3_json_formating(self):
        import json
        from raws_parser.tojson import MakeD3Json
        with open(TEST_ASSETS + '/test_d3_json.json') as f:
            test_d3_json = json.load(f)

        make_json = MakeD3Json()

        self.assertEqual(json.loads(make_json.transform(self.result.tail[0])),
                         test_d3_json)

