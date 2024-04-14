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
    #define get_numbers_gcd function that asks for the inputs of a
    # and b and calls the function that calculates its gcd
    def get_numbers_gcd(self):
        while True:
            try:
                a = int(input("Enter the first positive integer: "))
                b = int(input("Enter the second positive integer: "))
                #check are both numbers positive
                if a > 0 and b > 0:
                    #call calculate_gcd dunction the calculate the gcd of a and b
                    return self.calculate_gcd(a, b)
                else:
                    #tell user their input is incorrect
                    print("Both numbers have to be positive. Please try again. ")
            except ValueError:
                # tell user their input is incorrect
                print("Invalid input; please enter positive integers only.")
#create an instance of the class to get gcd
gcd_calculator = EuclideanAlgorithm()
#call get_number_gcd
result = gcd_calculator.get_numbers_gcd()
#print the result of the gcd calculation
print(f"The GCD is {result}.")