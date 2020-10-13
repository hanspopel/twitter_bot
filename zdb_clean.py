#!/usr/bin/env python3

import markovify
import tweepy
from mtranslate import translate
import json

import fileinput
import re

def atest(test_str):
    ret = ''
    skip1c = 0
    skip2c = 0
    for i in test_str:
        if i == '[':
            skip1c += 1
        elif i == '(':
            skip2c += 1
        elif i == ']' and skip1c > 0:
            skip1c -= 1
        elif i == ')'and skip2c > 0:
            skip2c -= 1
        elif skip1c == 0 and skip2c == 0:
            ret += i
    return ret

# def line_numbers(file_path, word_list):

#     with open("GLView.txt", 'r') as f:
#         file_contents = f.read()
#         # print(file_contents)

#         results = {word:[] for word in word_list}
#         for num, line in enumerate(file_contents, start=1):
#             for word in word_list:
#                 if word in line:
#                     # print(word)
#                     results[word].append(num)
#     return results

# for line in fileinput.FileInput("GLView.txt",inplace=1):
#     if line.rstrip():
#         print line

# word_list = ['b', 'int', 'float', 'float']
# result = line_numbers("GLView.txt",word_list)

# for word, lines in result.items():
#     print(word, ": ", ', '.join(lines))
# print(result)


# words = ['void', 'proton', 'electron', 'neutron']

# file_path = "GLVieh.h"

# result = line_numbers(file_path, words)

# Get raw text as string.
# with open("GLView.h") as f:
#     text = f.read()

# if 'void' in text
#     print('void!')

# for line in text:
#     print line
#     line.strip().split('/n')
#     for term in line:
#         print term
# file.close()