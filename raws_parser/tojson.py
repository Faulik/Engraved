from plyplus import STransformer


class MakeJson(STransformer):
    def main(self, tree):
        obj_stm = tree.select('object_stm > * ')[:][0]
        # nah, i done it again
        return '{{"object stm":"{}",' \
               '"objects":[{}]}}'.format(obj_stm,
                                              ''.join(tree.tail[1:])[:-1])

    def object(self, tree):
        token_type = tree.select1('token_type *')
        token_item_name = tree.select1('token_item_name *')
        return '{{"token type":"{}",' \
               '"token item name":"{}",' \
               '"options":[{}]}},'.format(token_type, token_item_name,
                                            ''.join(tree.tail[1:]))

    def options(self, tree):
        # The most stupid thing i done yet
        return ''.join(tree.tail)[:-1]

    def option(self, tree):
        tokens = tree.select('token > *')[:]
        return '{{"token name":"{}"' \
               '{}}},'.format(tokens[0],
                              ''.join(',"token elem":"{}"'.format(x)
                                      for x in tokens[1:]))


class MakeD3Json(STransformer):
    def main(self, tree):
        object_stm = tree.select('object_stm > *')[:][0]
        return '{{"name":"{}",' \
               '"children": [{}]}}'.format(object_stm,
                                           ''.join(tree.tail[1:])[:-1])

    def object(self, tree):
        token_item_name = tree.select1('token_item_name *')
        return '{{"name":"{}",' \
               '"children":[{}]}},'.format(token_item_name,
                                            ''.join(tree.tail[1:]))

    def options(self, tree):
        return ''.join(tree.tail)[:-1]

    def option(self, tree):
        tokens = tree.select('token > *')[:]
        if len(tokens) == 1:
            return '{{"name":"{}"}},'.format(tokens[0])
        else:
            return '{{"name":"{}",' \
                   '"children":[{}]}},'\
                   .format(tokens[0],
                           ''.join('{{"name":"{}"}},'.format(x)
                                   for x in tokens[1:])[:-1])