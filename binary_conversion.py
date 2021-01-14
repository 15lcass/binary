def binary_converter(string):

    binary = False
    decimal = False

    if len(string) == 16:
        for letter in string:
            if letter == '0' or letter == '1':  # checks if input string is in binary
                binary = True
            else:
                binary = False
                break
    elif int(string) >= 0 and int(string) < 2 ** 16:  # checks if input string is in decimal
        decimal = True
    else:
        return None

    result = 0
    constant = (2 ** 16) / 2  # this is the first number that will be checked, which is halved each time

    if binary == True:
        for letter in string:
            result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
            constant /= 2

    elif decimal == True:

        string = int(string)
        result = ''

        while len(result) < 16:  # continues until the number is in valid 16-bit binary
            if string - constant >= 0:
                result += '1'
                string -= constant

            else:
                result += '0'

            constant /= 2

    return result

string = input("Enter number: ")
print(binary_converter(string))


#def binary_converter_v2(string):