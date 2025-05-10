class Caluclator:
    #Function to input the numbers and choice of operation
    def input(self):
        print("")
        while True:
            try:
                inputNumber = int(input("How many number you want for input: "))
                if inputNumber <2:
                    print ("Input atleast 2 digits for the operation.")
                    print("")
                    continue
                break
            except:
                print("Invalid input for the number of inputs.")

        numberList = []
        counter=1

        for num in range(inputNumber):
            while True:
                try:
                    print("")
                    print("------------------------------")
                    value = int(input(f"Enter your value-{counter}: "))
                    numberList.append(value)
                    counter += 1
                    break
                except:
                    print("Error:- Write only interger numbers")

        print("")
        print("Choice of Operations:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Divison")
        print("")
        
        while True:
            option = int(input("Choose the option from above: "))
            match option:
                
                case 1:
                    total = obj1.addition (numberList)
                    print("Addition is : ", total)
                    self.continueApplication() 
                
                case 2:
                    total = obj1.substraction(numberList)
                    print("Substraction is : ", total)
                    self.continueApplication() 

                case 3:
                    total = obj1.multiplication(numberList)
                    print("Multiplication is : ", total)
                    self.continueApplication() 

                case 4:
                    total = obj1.divison(numberList)
                    print("Divison is : ", total)
                    self.continueApplication() 
                
                case _:
                    print("Error:- Invalid choice")
        
    # To check if user wants to continue the program or not
    def continueApplication(self):
        while True:
            try:
                valueContinueApplication = str(input("Do you want to continue? Y or N:  "))
                
                valueContinueApplication = valueContinueApplication.upper()

                if valueContinueApplication == 'Y' or valueContinueApplication == 'YES':
                    self.input()
                
                elif valueContinueApplication == 'N' or valueContinueApplication == 'NO': 
                    break
                
                else:
                    print("Please put corect choice.")

            except:
                print("Invalid Input. Write only Y or N.")
 
    
    #Function for the addition
    def addition(self,numberList):
        total = 0
        for num in numberList:
            total += num
        return total
    
    #Function for the substraction
    def substraction(self,numberList):
        total = numberList[0]
        for num in numberList[1:]:
            total -= num 
        return total
    
    #Function for the multiplucation
    def multiplication(self,numberList):
        total = 0
        for num in numberList:
            total *= num
        return total
    
    #Function for the divison
    def divison(self,numberList):
        numberList.sort(reverse=True)
        total = numberList[0]
        for num in numberList[1:]:
            if num==0:
                print("Can't divide by zero")
            else:
                total /= num 
        return total


# Main Program
print("")    
print("-------------------------")
print("|---Python Calculator---|")
print("-------------------------")
obj1 = Caluclator()

obj1.input()
