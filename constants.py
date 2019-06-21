import sys

dashes = ["–", "--+"]
for i in range(8208, 8214):
    dashes.append(chr(i))


UNDECIDED = 0
SHOULD_SPLIT = 1
SHOULD_NOT_SPLIT = 2

