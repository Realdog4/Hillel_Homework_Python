from colorama import init, Fore, Style


class Colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print(Fore.RED, end='')
        elif self.color == 'blue':
            print(Fore.BLUE, end='')
        elif self.color == 'green':
            print(Fore.GREEN, end='')
        elif self.color == 'yellow':
            print(Fore.YELLOW, end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Style.RESET_ALL, end='')


init()


with Colorizer('red'):
    print('printed in red')

with Colorizer('green'):
    print('printed in green')

with Colorizer('blue'):
    print('printed in blue')

with Colorizer('yellow'):
    print('printed in yellow')

print('printed in default color')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')


