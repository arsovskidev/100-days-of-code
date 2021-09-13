# Write your code below this line 👇


def prime_checker(number):
    flag = 0
    for check in range(1, number + 1):
        if number % check == 0:
            flag += 1

    if flag > 2:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


# Write your code above this line 👆

# Tests
import unittest
from unittest.mock import patch
from io import StringIO


class MyTest(unittest.TestCase):
    # Testing Print output
    def test_1(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            prime_checker(87)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_2(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            prime_checker(97)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_3(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            prime_checker(66)
            expected_print = "It's not a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)

    def test_4(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            prime_checker(47)
            expected_print = "It's a prime number.\n"
            self.assertEqual(fake_out.getvalue(), expected_print)


print("\n")
print("Running some tests on your code:")
print(".\n.\n.\n.")
unittest.main(verbosity=1, exit=False)
