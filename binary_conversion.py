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

    if int(input_value) < 2 ** 16 and int(input_value) > -(2 ** 16):  # check if input string is in decimal
        decimal = True

    constant = (2 ** 16) / 2

    if binary == True:
        string = input_value
        result = 0

        if input_value[0] == '1':  # if negative, do two's complement
            string = list(input_value)
            for i in range(len(string)):  # switch the numbers
                if string[i] == '1':
                    string[i] = '0'
                elif string[i] == '0':
                    string[i] = '1'

            for i in range(len(string) - 1, -1, -1):  # add one by going backwards through numbers, changing 1s to 0s until a 0 is found, turning it to 1
                if string[i] == '0':
                    string[i] = '1'
                    break
                elif string[i] == '1':
                    string[i] = '0'

            string = ''.join(string)

        for letter in string:
            result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
            constant /= 2

        if input_value[0] == '1':
            result = ('-' + str(result))

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


def binary_converter_v3(input_value, fixed_position=None):
    '''
    This function has two different modes. If you input a decimal, it returns a string of 1’s and 0’s
    that encode it in 16-bit binary. If you input a 16-bit string of 1’s and 0’s, it will return the
    two’s complement number that the string represents. If you input a value outside the accepted range,
    it will return None. If you put a value that will not perfectly fit into a binary decimal, it will
    round the value down as little as possible. It also takes a second input that tells it where the
    fixed decimal point is located.
    :param input_value: a positive integer, or a string of 1’s and 0’s
    :param fixed_position: a positive integer from 0 to 15, this indicates which bit the fixed point is
    found in front of. So position 0 would have all bits behind the fixed point
    :return: a number
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

    if float(input_value) < 2 ** 16 and float(input_value) > -(2 ** 16):  # check if input string is in decimal
        decimal = True

    constant = (2 ** 16) / 2

    if binary == True:

        string = input_value
        result = 0

        if fixed_position != None:

            if input_value[0] == '1':  # if negative decimal

                string = list(input_value)
                bits_to_keep = ''

                for i in range(len(string) - 1, -1, -1):  # goes backwards through binary to find least significant one
                    if string[i] == '0':
                        bits_to_keep += string[i]
                    elif string[i] == '1':
                        bits_to_keep = '1' + bits_to_keep
                        break

                for i in range(len(string) - len(bits_to_keep)):  # switches all of the bits except the least significant one
                    if string[i] == '1':
                        string[i] = '0'
                    elif string[i] == '0':
                        string[i] = '1'

                string = ''.join(string)


            constant = 2 ** (len(string[:int(fixed_position)]) - 1)  # the max decimal is different depending on where the fixed point is

            for letter in string:
                result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
                constant /= 2

            if input_value[0] == '1':
                result = '-' + str(result)


        else:

            if input_value[0] == '1':  # if negative, do two's complement
                string = list(input_value)
                for i in range(len(string)):  # switch the numbers
                    if string[i] == '1':
                        string[i] = '0'
                    elif string[i] == '0':
                        string[i] = '1'

                for i in range(len(string) - 1, -1, -1):  # add one by going backwards through numbers, changing 1s to 0s until a 0 is found, turning it to 1
                    if string[i] == '0':
                        string[i] = '1'
                        break
                    elif string[i] == '1':
                        string[i] = '0'

                string = ''.join(string)

            for letter in string:
                result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
                constant /= 2

            if input_value[0] == '1':
                result = '-' + str(result)


    elif decimal == True:

        result = ''
        string = float(input_value.replace('-', ''))  # removes the hyphen if number is negative

        if float(input_value) - int(float(input_value)) != 0:  # check if decimal number

            constant = 128
            while len(result) < 16:
                if constant < 1 and '.' not in result:
                    result += '.'  # add fixed point to separate the whole numbers to the decimal numbers
                if string - constant >= 0:
                    result += '1'
                    string -= constant
                else:
                    result += '0'

                print(result, string, constant)

                constant /= 2

            if float(input_value) < 0:  # check if negative decimal number, and converts the previous result

                string = list(result)
                bits_to_keep = ''

                for i in range(len(string) - 1, -1, -1):  # goes backwards through binary to find least significant one
                    if string[i] == '0':
                        bits_to_keep += string[i]
                    elif string[i] == '1':
                        bits_to_keep = '1' + bits_to_keep
                        break

                for i in range(len(string) - len(bits_to_keep)):  # switches all of the bits except the least significant one
                    if string[i] == '1':
                        string[i] = '0'
                    elif string[i] == '0':
                        string[i] = '1'

                result = ''.join(string)

        else:

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


def binary_converter_v4(input_value, exponent_bits=None):
    '''
    If you input a 16-bit string of 1’s and 0’s, it will return the two’s complement number that the
    string represents. If you input a value outside the accepted range, it will return None. If you put
    a value that will not perfectly fit into a binary decimal, it will round the value down as little
    as possible. It also takes a second input that tells it how many bits are used in the exponent. It
    is assumed 1 for the sign bit and the rest for the mantissa.
    :param input_value a string of 1’s and 0’s
    :param exponent_bits: a positive integer from 1 to 13, this how many bits are used in the exponent.
    These are always found at the end of the string
    :return: a number
    '''

    if len(input_value) == 16:  # checks if input is in binary
        for letter in input_value:
            if letter != '0' and letter != '1':
                return None

    else:
        return None


    if exponent_bits == None:

        constant = (2 ** 16) / 2
        result = 0

        if input_value[0] == '1':  # if negative, do two's complement
            string = list(input_value)
            for i in range(len(string)):  # switch the numbers
                if string[i] == '1':
                    string[i] = '0'
                elif string[i] == '0':
                    string[i] = '1'

            for i in range(len(string) - 1, -1,
                           -1):  # add one by going backwards through numbers, changing 1s to 0s until a 0 is found, turning it to 1
                if string[i] == '0':
                    string[i] = '1'
                    break
                elif string[i] == '1':
                    string[i] = '0'

            string = ''.join(string)

        for letter in string:
            result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
            constant /= 2

        if input_value[0] == '1':
            result = '-' + str(result)


    else:

        exponent_bits = int(exponent_bits)

        mantissa = input_value[:len(input_value) - exponent_bits]
        exponent = input_value[len(mantissa):]
        constant = 2 ** (exponent_bits - 1)  # the max decimal is different depending on how long the exponent is
        result = 0

        if exponent[0] == '1':  # if negative exponent, do two's complement
            string = list(exponent)
            for i in range(len(string)):  # switch the numbers
                if string[i] == '1':
                    string[i] = '0'
                elif string[i] == '0':
                    string[i] = '1'

            for i in range(len(string) - 1, -1, -1):  # add one by going backwards through numbers, changing 1s to 0s until a 0 is found, turning it to 1
                if string[i] == '0':
                    string[i] = '1'
                    break
                elif string[i] == '1':
                    string[i] = '0'

            exponent = ''.join(string)

        for letter in exponent:  # find value of exponent
            result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
            constant /= 2

        if (input_value[len(mantissa):])[0] == '1':  # checks if negative exponent
            result *= -1

        power = result
        result = 0
        constant = 2 ** power  # the max decimal is different depending on where the fixed point is

        for letter in mantissa:
            result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
            constant /= 2

        if mantissa[0] == '1':
            result *= -1

    return result


def binary_normalisation(input_value, exponent_bits):
    '''
    This function takes a given 16-bit binary string and normalised it. It also takes a second input
    that tells it how many bits are used in the exponent. It is assumed 1 for the sign bit and the rest
    for the mantissa.
    :param input_value a string of 1’s and 0’s
    :param exponent_bits: a positive integer from 1 to 13, this how many bits are used in the exponent.
    These are always found at the end of the string
    :return: a normalized string of 1’s and 0’s
    '''

    exponent_bits = int(exponent_bits)

    sign_bit = input_value[0]
    mantissa = input_value[1:len(input_value) - exponent_bits]
    exponent = input_value[len(mantissa) + 1:]

    # exponent to binary:

    constant = 2 ** (exponent_bits - 1)  # the max decimal is different depending on how long the exponent is
    result = 0

    if exponent[0] == '1':  # if negative exponent, do two's complement
        string = list(exponent)
        for i in range(len(string)):  # switch the numbers
            if string[i] == '1':
                string[i] = '0'
            elif string[i] == '0':
                string[i] = '1'

        for i in range(len(string) - 1, -1, -1):  # add one by going backwards through numbers, changing 1s to 0s until a 0 is found, turning it to 1
            if string[i] == '0':
                string[i] = '1'
                break
            elif string[i] == '1':
                string[i] = '0'

        exponent = ''.join(string)

    for letter in exponent:  # find value of exponent
        result += (int(letter) * constant)  # adds the constant to the result if a 1 is there
        constant /= 2

    if (input_value[len(mantissa):])[0] == '1':  # checks if negative exponent
        result *= -1

    power = result
    mantissa = list(mantissa)

    for i in range(len(mantissa)):
        if mantissa[i] == sign_bit:
            mantissa[i] = ''
            power -= 1  # for every bit removed, we must decrease the power
        else:
            break

    mantissa = ''.join(mantissa)

    # turn power back into binary

    string = power
    if power < 0:
        string = power * -1

    exponent = ''
    constant = 2 ** (3)  # ???

    while len(exponent) < 4:  # continues until the number is in valid 4-bit binary
        if string - constant >= 0:
            exponent += '1'
            string -= constant
        else:
            exponent += '0'
        constant /= 2

    if power < 0:  # if the value is negative, do two's complement
        exponent = list(exponent)

        for i in range(len(exponent)):  # switch the numbers
            if exponent[i] == '1':
                exponent[i] = '0'
            elif exponent[i] == '0':
                exponent[i] = '1'

        for i in range(len(exponent) - 1, -1, -1):  # add one
            if exponent[i] == '0':
                exponent[i] = '1'
                break
            elif exponent[i] == '1':
                exponent[i] = '0'

        exponent = ''.join(exponent)

    if sign_bit == '1':
        result = (sign_bit + mantissa + ' ' + exponent)

    else:
        result = (mantissa + ' ' + exponent)

    return result

my_string = input('Enter number: ')
fixed_position = input('Enter fixed position: ')
exponent_bits = input('Enter number of bits in exponent: ')

print(binary_normalisation(my_string, exponent_bits))

