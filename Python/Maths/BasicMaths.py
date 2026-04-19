import math


class BasicMaths:
    def __init__(self):
        pass

    def count_digits(self, num):
        answer = 0
        num = abs(num)

        while num > 0:
            digit = num % 10
            answer += 1
            num = math.floor(num / 10)

        return answer

    def reverse_integer(self, num):
        answer = 0
        copiedNum = num

        # when integer is -ve
        signBit = -1 if num < 0 else 1
        num = abs(num)

        # for long integers
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        if copiedNum < INT_MIN:
            print("The given number is too small")
            return 0

        while num > 0:
            digit = num % 10
            if num * 10 > INT_MAX:
                print("The given number is too big")
                return 0

            answer = answer * 10 + digit
            num = math.floor(num / 10)

        return answer * signBit

    def check_palindrome(self, num):
        reversedNum = self.reverse_integer(num)

        if reversedNum == num:
            return True
        else:
            return False

    def check_armstrong(self, num):
        num = abs(num)
        originalNum = num

        digitCount = self.count_digits(num)
        powerSum = 0

        while num > 0:
            digit = num % 10
            powerSum += pow(digit, digitCount)
            num = num // 10  # floor division operator

        if originalNum == powerSum:
            return True
        else:
            return False

    def get_divisors(self, num):
        tempDivisors = []

        for i in range(1, num + 1):
            if num % i == 0:
                tempDivisors.append(i)

        print(f"Divisors of {num} is {",".join(map(str, tempDivisors))}")

    def get_divisors_best_way(self, num):
        tempDivisors = []

        x = math.floor(math.sqrt(num))  #
        for i in range(1, x + 1):
            if num % i == 0:
                tempDivisors.append(i)

                second_factor = num // i  #
                if second_factor != i:
                    tempDivisors.append(second_factor)

        allDivisors = sorted(tempDivisors)
        print(f"Divisors of {num} is {",".join(map(str, allDivisors))} \n")

    def gcd(self, num1, num2):
        hcf = 1

        x = min(num1, num2)
        # one way
        for i in range(1, x + 1):
            if num1 % i == 0 and num2 % i == 0:
                hcf = i

        # second way
        # just a tweak in range func.
        for j in range(x + 1, 1, -1):
            if num1 % j == 0 and num2 % j == 0:
                hcf = j
                break

        return hcf

    def gcd_euclidean_way(self, num1, num2):
        """
        Euclid said, gcd(x,y) = gcd(x-y, y) if x > y
        Deduced, gcd(x,y) = gcd(x % y, y) if x > y
                    once x or y = 0
                    then if x = 0, y = gcd
                         else y = 0, x = gcd
        Time = O(log ϕ min(n1,n2)) ==> log of fie of min(n1, n2)
        """
        x = num1
        y = num2

        while (x > 0) and (y > 0):
            if x > y:
                x = x % y
            else:
                y = y % x

        if x == 0:
            return y
        else:
            return x

    def check_prime(self, num):
        if num < 2:
            return False

        isPrime = True

        x = math.floor(math.sqrt(num))
        for i in range(2, x + 1):
            if num % i == 0:
                isPrime = False

        return isPrime

    def prime_till_integer(self, num):
        tempPrimes = []

        for i in range(num):
            if self.check_prime(i):
                tempPrimes.append(i)

        print(f"Prime integers till {num} are {",".join(map(str, tempPrimes))} \n")

    def prime_till_integer_by_soe(self, num):
        """
        1. fill an array with True till given num (this is main logic of SOE)
        2. Outer loop: for i = 2 to sqrt(n)
                checks, if(primes) is true
        3. Inner loop:  for j = i*i to n with j += i (Main Logic)
        4.              set multiples of j to false
        5. whatever primes[i] is true, are the actual primes till num

        Time = O(n log log n)
        """
        answer = []
        primes = [True for _ in range(num + 1)]  # 1

        x = int(math.sqrt(num))  # 2
        for i in range(2, x + 1):

            if primes[i] == True:
                j = i * i
                while j <= num:  # 3
                    primes[j] = False  # 4
                    j += i

        for i in range(2, num + 1):  # 5
            if primes[i]:
                answer.append(i)

        print("---Sieve of Eratosthenes---")
        print(f"Prime integers till {num} are {",".join(map(str, answer))} \n")


obj = BasicMaths()
numberToEvaluate = 203

digitCount = obj.count_digits(numberToEvaluate)
print(f"No. of digits in {numberToEvaluate} is {digitCount} \n")

reversedInteger = obj.reverse_integer(numberToEvaluate)
print(f"Reverse of {numberToEvaluate} is {reversedInteger} \n")

isPalindrome = obj.check_palindrome(numberToEvaluate)
print(
    f"{numberToEvaluate} is a {'palindrome' if isPalindrome else 'NOT a palindrome!'} \n"
)

isArmstrong = obj.check_armstrong(numberToEvaluate)
print(
    f"{numberToEvaluate} is {'an Armstrong' if isArmstrong else 'NOT an Armstrong'} number! \n"
)

obj.get_divisors(numberToEvaluate)
obj.get_divisors_best_way(numberToEvaluate)

isPrime = obj.check_prime(numberToEvaluate)
print(f"{numberToEvaluate} is {'a Prime' if isPrime else 'a Composite'} number! \n")

obj.prime_till_integer(30)
obj.prime_till_integer_by_soe(30)

n1 = 20
n2 = 40
hcf = obj.gcd(n1, n2)
print(f"GCD of {n1} and {n2} is {hcf}")

gcd = obj.gcd_euclidean_way(n1, n2)
print(f"GCD of {n1} and {n2} by Euclidean way is {gcd}")
