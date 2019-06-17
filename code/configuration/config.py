import os

def sanitize_tokens(tokens):
    res = []
    for token in tokens:
        token = token.strip()
        if token != '' and token != '=':
            res.append(token)
    return res

class Config:
    type_mapping = dict()

    def __init__(self, attributes=None, *args):
        if attributes:
            for attr, key in attributes.items():
                self.__setattr__(attr, key)
        self.post_init()

    def post_init(self, *args):
        pass


    @staticmethod
    def load_config(class_type, path):
        assert os.path.exists(path), f'wrong config path: {path}'
        with open(path, 'r') as f:
            lines = f.readlines()
            pairs = dict()
            for line in lines:
                tokens = sanitize_tokens(line.split("'"))
                assert len(tokens) == 2, 'Wrong config tokens count'
                attr, value = tokens
                assert attr in class_type.type_mapping, f'{attr} attribute is not allowed'
                pairs[attr] = class_type.type_mapping[attr](value)
            return __class__(pairs)













