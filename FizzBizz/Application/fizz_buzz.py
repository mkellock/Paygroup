import abc

class FizzBuzzInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'execute_fizz_buzz') and 
                callable(subclass.execute_fizz_buzz) or 
                NotImplemented)

    @abc.abstractmethod
    def execute_fizz_buzz(self, min: int, max: int):
        raise NotImplementedError

class FizzBuzz(FizzBuzzInterface):
    def execute_fizz_buzz(self, min: int, max: int):
        # Define the array of inclusive integers
        items = [i for i in range(min, max + 1)]

        # Adjust the values based on FizzBuzz logic
        for index, item in enumerate(items):
            if item%3 == 0 and item%5 == 0:
                items[index] = "FizzBuzz"
            elif item%3==0:
                items[index] = "Fizz"
            elif item%5==0:
                items[index] = "Buzz"
        
        # Return the list
        return items