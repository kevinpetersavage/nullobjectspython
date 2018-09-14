from unittest import TestCase

from collection_null_objects_example import sum_list


class CollectionNullObjectsTest(TestCase):
    def testNullListsExample(self):
        assert sum_list(None) == None

    def testSummingListsActuallyWorksWithSomeNumbers(self):
        assert sum_list([1, 2, 3, 4]) == 10
