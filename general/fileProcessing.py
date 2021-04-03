#!/usr/bin/python3
import os

os.chdir("/home/patrick/Github/ict1110/mips-programming")
directory = os.listdir("/home/patrick/Github/ict1110/mips-programming")


for file in directory:
    with open(file, "r") as original: data = original.read()
    with open(file, "w") as modified: modified.write("## Author: 2019037459\n## Instructor: Dr Lighton Phiri\n\n " + data)

