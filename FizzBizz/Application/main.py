import fizz_buzz as fb
import os

if __name__ == "__main__":
    min = int(os.getenv("FIZZ_BUZZ_MIN"))
    max = int(os.getenv("FIZZ_BUZZ_MAX"))

    for item in fb.FizzBuzz().execute_fizz_buzz(min=min, max=max):
        print(item)
