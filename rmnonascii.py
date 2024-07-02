#!/usr/bin/env python
import sys

def remove_control_characters(text):
    return ''.join(ch for ch in text if ord(ch) >= 32)

with open(sys.argv[1], "r", encoding="utf-8") as file:
    content = file.read()

clean_content = remove_control_characters(content)

with open("cleaned_" + sys.argv[1], "w", encoding="utf-8") as file:
    file.write(clean_content)

