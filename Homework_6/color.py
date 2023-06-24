from colorama import init, Fore, Style


class Colorizer:
    def __init__(self, color):
        self.color = color

    def __enter__(self):
        if self.color == 'red':
            print(Fore.RED, end='')
        elif self.color == 'blue':
            print(Fore.BLUE, end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(Style.RESET_ALL, end='')


init()


with Colorizer('red'):
    print('printed in red')

print('printed in default color')


print('\033[93m', end='')
print('aaa')
print('bbb')
print('\033[0m', end='')
print('ccc')


