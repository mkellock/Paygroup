import sys

sys.path.append("../Application")
import fizz_buzz


def test_fizz_buzz_should_calculate():
    expected_result = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16, 17, "Fizz", 19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 26, "Fizz", 28, 29, "FizzBuzz"]
    assert fizz_buzz.fizz_buzz(1, 30) == expected_result
