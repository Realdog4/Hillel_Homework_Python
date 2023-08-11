"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in.
Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(input_string, markers):
    lines = input_string.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        for marker in markers:
            if marker in line:
                line = line.split(marker)[0].rstrip()
        lines[i] = line
    return '\n'.join(lines)


input_string = "apples, pears # and bananas\ngrapes\nbananas !apples"
markers = ["#", "!"]
result = solution(input_string, markers)
print(result)
