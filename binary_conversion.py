def binary_converter(input_value):
    '''
    This function has two different modes. If you input a positive integer, it returns a string of
    1’s and 0’s that encode it in 16-bit binary. If you input a 16-bit string of 1’s and 0’s, it will
    return the positive integer that the string represents. If you input a value outside the accepted
    range, it will return None.
    :param input_value: a positive integer, or a string of 1’s and 0’s
    :return: a string of 1’s and 0’s or a positive integer
    '''

    binary = False
    decimal = False

    if len(input_value) == 16:
        for letter in input_value:
            if letter == '0' or letter == '1':  # checks if input string is in binary
                binary = True
            else:
                binary = False
                break
    if int(input_value) >= 0 and int(input_value) < 2 ** 16:  # checks if input string is in decimal
        decimal = True
    else:
        return None

    result = 0
    constant = (2 ** 16) / 2  # this is the first number that will be checked, which is halved each time

    if binary == True:
        for letter in input_value:
            result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
            constant /= 2

    elif decimal == True:

        string = int(input_value)
        result = ''

        while len(result) < 16:  # continues until the number is in valid 16-bit binary
            if string - constant >= 0:
                result += '1'
                string -= constant
            else:
                result += '0'
            constant /= 2

    return result



def binary_converter_v2(input_value):
    '''
    This function has two different modes. If you input an integer, it returns a string of 1’s and 0’s
    that encode it in 16-bit binary. If you input a 16-bit string of 1’s and 0’s, it will return the
    two’s complement number that the string represents. If you input a value outside the accepted range,
    it will return None.
    :param input_value: a positive integer, or a string of 1’s and 0’s
    :return: a string of 1’s and 0’s or an integer
    '''

    binary = False
    decimal = False

    if len(input_value) == 16:
        for letter in input_value:
            if letter == '0' or letter == '1':  # checks if input string is in binary
                binary = True
            else:
                binary = False
                break

    if int(input_value) < 2 ** 16 and int(input_value) > -(2 ** 16):
        decimal = True

    else:
        return None

    constant = (2 ** 16) / 2

    if binary == True:  # do two's complement

        string = list(input_value)
        for i in range(len(string)):  # switch the numbers
            if string[i] == '1':
                string[i] = '0'
            elif string[i] == '0':
                string[i] = '1'

        for i in range(len(string) - 1, -1, -1):  # add one
            if string[i] == '0':
                string[i] = '1'
                break
            elif string[i] == '1':
                string[i] = '0'

        result = ''.join(string)


    elif decimal == True:
        string = int(input_value.replace('-', ''))  # removes the hyphen if number is negative
        result = ''
        while len(result) < 16:  # continues until the number is in valid 16-bit binary
            if string - constant >= 0:
                result += '1'
                string -= constant
            else:
                result += '0'
            constant /= 2

        if int(input_value) < 0:  # if the value is negative, do two's complement
            result = list(result)

            for i in range(len(result)):  # switch the numbers
                if result[i] == '1':
                    result[i] = '0'
                elif result[i] == '0':
                    result[i] = '1'

            for i in range(len(result) - 1, -1, -1):  # add one
                if result[i] == '0':
                    result[i] = '1'
                    break
                elif result[i] == '1':
                    result[i] = '0'

            result = ''.join(result)


    else:
        result = None

    return result


string = input("Enter number: ")
#print(binary_converter(string))
print(binary_converter_v2(string))
