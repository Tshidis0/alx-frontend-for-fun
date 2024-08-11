#!/usr/bin/python3
''' Write a script markdown2html.py that takes an argument 2 strings:
    First argument is the name of the Markdown file
    Second argument is the output file name
'''


import sys
import os
import markdown


if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <input_file> <output_file>", file=sys.stderr)
    sys.exit(1)

# Get the input and output file names from command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Convert Markdown to HTML
with open(input_file, "r") as f:
    markdown_content = f.read()
    html_content = markdown.markdown(markdown_content)

# Write the HTML content to the output file
with open(output_file, "w") as f:
    f.write(html_content)

sys.exit(0)
