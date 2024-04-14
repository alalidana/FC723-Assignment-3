#define a class to encapsulate the functionality
class EuclideanAlgorithm:
    #parameter a is the first number and parameter b is the second number
    def calculate_gcd(self, a, b):
        #First, check if either number is 0 and return the other number as GCD
        if a == 0:
            return b
        if b == 0:
            return a
        #Iterate applying the euclidean algorithm until b becomes 0
        while b != 0:
            #calculate the remainder of a divided by b
            remainder = a % b
            #ipdate a to be b and b to be the remainder
            a, b = b, remainder
        #when b = 0 a contains the gcd
        return a
#example of using the class
gcd_calculator = EuclideanAlgorithm()
result = gcd_calculator.calculate_gcd(48, 18)
print(f"The GCD of 48 and 18 is {result}")