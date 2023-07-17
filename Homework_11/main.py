def new_format(string):
    if len(string) <= 3:
        return string
    else:
        result = ""
        for i in range(len(string)-1, -1, -1):
            result = string[i] + result
            if (len(string) - i) % 3 == 0 and i != 0:
                result = "." + result
        return result


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
print("Good!")
