from unittest import TestCase
import os, sys; sys.path.append(os.path.abspath('.'))
from src.restart.utils import SingletonFieldClass

class TestSingletonFieldClass(TestCase):
    a_call_count = 0
    b_call_count = 0

    class A(SingletonFieldClass):
        def __init__(self, c=3):
            super().__init__()
            self.c = c
        def get_singleton_fields(self):
            TestSingletonFieldClass.a_call_count += 1
            return {'a': 1, 'b': 2}

    class B(SingletonFieldClass):
        def __init__(self, c=6):
            super().__init__()
            self.c = c
        def get_singleton_fields(self):
            TestSingletonFieldClass.b_call_count += 1
            return {'a': 4, 'b': 5}


    def setUp(self) -> None:
        return super().setUp()

    def test_init_values(self):
        a = self.A()
        b = self.B()
        self.assertEqual(a.a, 1)
        self.assertEqual(a.b, 2)
        self.assertEqual(a.c, 3)
        self.assertEqual(b.a, 4)
        self.assertEqual(b.b, 5)
        self.assertEqual(b.c, 6)

    def test_set_singleton_field(self):
        a = self.A()
        a.c = 10
        with self.assertRaises(Exception):
            a.a = 0
        with self.assertRaises(Exception):
            a.b = 0
        b = self.B()
        with self.assertRaises(Exception):
            b.a = 0
        with self.assertRaises(Exception):
            b.b = 0

    def test_init_calls(self):
        for _ in range(100):
            self.A()
            self.B()
        self.assertEqual(self.a_call_count, 1)
        self.assertEqual(self.b_call_count, 1)