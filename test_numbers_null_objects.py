from unittest import TestCase

from number_null_objects_example import product, sum
from optional import optional_of_nullable, optional_of, empty


class NumbersNullObjectsTest(TestCase):
    def test_null_product_example(self):
        assert product(5, None) == 0

    def test_product_actually_works_with_some_numbers(self):
        assert product(5, 5) == 25

    def test_null_sum_example(self):
        assert sum(None, 5) == 5

    def test_sum_actually_works_with_some_numbers(self):
        assert sum(5, 5) == 10
