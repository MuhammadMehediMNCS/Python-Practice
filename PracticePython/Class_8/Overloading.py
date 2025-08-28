
# Method Overloading
class Calculator:
    def add(self, *args):  # একাধিক সংখ্যা handle করবে
        return sum(args)

calc = Calculator()
print(calc.add(5, 7))        # Output: 12
print(calc.add(2, 3, 4))     # Output: 9
print(calc.add(2.5, 3.5))    # Output: 6.0