# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-01-09 19:07
from hanlp.utils.io_util import get_resource

HANLP_CHAR_TABLE = 'https://file.hankcs.com/corpus/char_table.zip#CharTable.txt'


class CharTable:
    convert = {}

    @staticmethod
    def normalize(text: str) -> str:
        return ''.join(CharTable.convert.get(c, c) for c in text)

    @staticmethod
    def _init():
        with open(get_resource(HANLP_CHAR_TABLE)) as src:
            for line in src:
                cells = line.rstrip('\n')
                if len(cells) != 3:
                    continue
                a, _, b = cells
                CharTable.convert[a] = b


# noinspection PyProtectedMember
CharTable._init()
