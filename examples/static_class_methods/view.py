from examples.static_class_methods.test import TestOfStaticAndClassMethods

test = TestOfStaticAndClassMethods()

test.instance_method()

TestOfStaticAndClassMethods.class_method()
TestOfStaticAndClassMethods.static_method_wrong_using()
TestOfStaticAndClassMethods.static_method_correct_using(25, 30)
