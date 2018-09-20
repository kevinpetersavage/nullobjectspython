# Null Objects Python

This is a repo that was used during a workshop on the concept of null objects. 

To run all the tests use the following command (or an ide of your choice):
```python -m unittest discover```

All the tests should initally pass. 

The task is to replace all the usages of None, assume that you will never receive a None and see how (if?) this simplifies the code.

Recommended order of attack:

* look at test_collection_null_objects.py to consider how null objects for collections are empty collections, e.g. the null object for list is []
* look at test_numbers_null_objects.py and use the classes/functions in optional.py to handle numbers (because numbers do not have a natural null object, it depends on the context)
* look at test_pet_null_objects.py to consider how we might implement a null object for a type in our own codebase
