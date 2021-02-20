"""
    raises any number to the degree
"""


def degree(value, value_of_degree=2, console="on"):
    import sys

    help_message = """
            ? - this message;
            exit - shutdown;
            degree: {integer} - change degree
            or some integer
        """

    if value == 'exit' and console == 'on':
        sys.exit()

    elif 'degree:' in value:
        try:
            return int(value.replace("degree:", ''))
        except ValueError:
            print("invalid input: you can't use string as value of integer, you need use integer.")

    elif value == '?' and console == 'on':
        print(help_message)

    elif console == 'on':
        try:
            return int(value) ** int(value_of_degree), value_of_degree
        except ValueError:
            print("invalid input: {} \n"
                  "what you can enter: \n "
                  "{}".format(value, help_message))

    elif console == 'off':
        try:
            return int(value) ** int(value_of_degree), value_of_degree
        except ValueError:
            return ("invalid input: {} \n"
                    "what you can enter only numbers".format(value))


if __name__ == '__main__':
    value_of_degree = 2
    while True:
        value = degree(input('enter:').lower().replace(' ', ''), value_of_degree)

        if type(value) is int:
            value_of_degree = value
            print('saved')
        elif type(value) is tuple:
            print(value[0])
            value_of_degree = value[1]
