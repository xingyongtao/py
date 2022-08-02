import unittest

from extract import extract, split_cell


class TestExtract(unittest.TestCase):
    def test_extract(self):
        tests = ['张三5']
        for raw in tests:
            res = extract(raw)
            print(res)

    def test_split_cell(self):
        tests = ['张三5', '张三5,', '张三5,李四40']
        for raw in tests:
            res = split_cell(raw)
            print(res)
