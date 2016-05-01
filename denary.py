##Prepei na kanw thn module .isdigit na douleuei kai me Python2.x

print("\nThe number you will enter will be converted into an 8-bit binary number.")
print("The maximum number you can enter is: 255")
binary_status = True
binary_numbers = [128,64,32,16,8,4,2,1]
##For debugging purposes I have included: print(binary_numbers, ",", len(binary_numbers)-1)
binary_output = [0]*8
##For debugging purposes I have included: print(binary_output)


while binary_status:
    denary_number = input("Enter the number you wish to convert in binary: ")
    if str(denary_number).isdigit():  ##Checking if the value is number or letter
        denary_number = int(denary_number)
        if denary_number != 0:
            if denary_number <= 255:
                for i in range(0, len(binary_numbers)):
                    ##For debugging purposes I have included: print("Before", i)
                    if binary_numbers[i] <= denary_number:  ##Trying to find the place in which will replace the 0 with 1
                        ##For debugging purposes I have included: print("After", i)
                        denary_number = denary_number - binary_numbers[i]
                        ##For debugging purposes I have included: print("Minus denary: ", denary_number)
                        if denary_number >0:
                            binary_output[i]=1
                            ##For debugging purposes I have included: print(binary_output)
                            binary_status = False
                        elif denary_number <= 0:
                            binary_output[i]=1
                            binary_output_str= ''.join(str(e) for e in binary_output)  ##Converting the list to a string but before doing that I have to convert the elements since they are digits
                            print("The value of the number you entered is: ", binary_output_str)
                            binary_status = False


                    else:
                        continue
            else:
                print("The number you entered is too big.\nTry again")
        else:
            binary_output_str = ''.join(str(e) for e in binary_output)  ##Converting the list to a string but before doing that I have to convert the elements since they are digits
            print("The value of the number you entered is: ", binary_output_str)
            binary_status = False
    else:
        print("The value you entered is not a number \033[1m"+"OR \033[0m"+"the number is float .\nPlease enter an integer number from 0-255\n")