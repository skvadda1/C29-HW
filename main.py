def checkConsec1(n):
    def convertToBinary(n):
        if n == 0:
            return n
        binary = ""
        while n > 0:
            binary = str(n % 2)
            n = n // 2
            count = 0
            for bit in convertToBinary:
                if(bit == "1"):
                    count += 1
                else:
                    count = 0
                    return binary
                return count
n = int(input("Enter your number:"))
print("Number of consecuetive 1's in binary form of", n , "is", checkConsec1(n))



