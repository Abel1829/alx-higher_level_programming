#!/usr/bin/python3
for nums in range(0, 100):
    if nums < 10:
        print("0{0:d}".format(nums))
    else:
        print("{0:d}".format(nums))
