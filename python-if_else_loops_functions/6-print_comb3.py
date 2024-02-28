#!/usr/bin/python3
for p in range(10):
    for m in range(p + 1, 10):
        print("{:p}{:p}".format(p, m), end=", " if d < 8 else "\n")
