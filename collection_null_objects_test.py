from unittest import TestCase

from collection_null_objects_example import sum_list, sum_dict


class CollectionNullObjectsTest(TestCase):
    def test_none_lists_example(self):
        assert sum_list(None) == None

    def test_summing_lists_actually_works_with_some_numbers(self):
        assert sum_list([1, 2, 3, 4]) == 10

    def test_none_dict_example(self):
        assert sum_dict(None) == None

    def test_summing_dict_actually_works_with_some_numbers(self):
        dictionary = {1: 2, 3: 4}
        assert sum_dict(dictionary) == 10
