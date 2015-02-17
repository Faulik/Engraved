import plyplus
import os


GRAMMAR_DIR = os.getcwd() + '/raws_parser/dictionaries'


def parse_file(pack_name, file_name):
    grammar = plyplus.Grammar(plyplus.grammars.open(
                              GRAMMAR_DIR + '/base.g'),
                              auto_filter_tokens=False)

    file = os.getcwd() + '/packs/' + pack_name + '/raw/objects/' + file_name\
           + ".txt"
    try:
        result = grammar.parse(open(file).read())
    except plyplus.ParseError as e:
        result = {'error': e}

    return result