#!/usr/bin/env python

"""
Pre-process Crowbar markdown documentation into
restructured text, and generate a Sphinx index page
"""

import os
import os.path
import pprint
import subprocess

source_docs_root = "/home/mikeyp/opencrowbar/core/doc"
processed_docs_root = "./doc"

def copy_to_staging(src, dest):
    """copies file tree from source to a staging area for processing"""
    command = [ '/bin/cp', '-r', src, dest, ]
    subprocess.call(command)

def generate_file_list(directory):
    """walk the file tree starting at dir , 
    and generate a list of markdown files to
    be converted"""

    contents = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            if os.path.splitext(f)[1] == '.md':
                contents.append(os.path.join(root, f))
    return sorted(contents)

def sort_crowbar():
    """custom sort to match crowbar's doc processing order"""
    # TODO mikeyp determine sort logic 
    return 
    

# make a copy of the source, so we don't accidentally mess up a checkout

copy_to_staging(source_docs_root, processed_docs_root)

# this script has some knowledge of of the 'top level' documentation sections 
# to help generate a cleaner documentation index depsite the markdown to
# restructured text conversion
# the format ff sections is:
# (directory, corresponding directive for the index template)

sections = [
    ('deployment-guide', 'deploy-guide-files::'),
    ('development-guides','development-guide-files::'),
    ('faq','faq-files::'),
    ('licenses', 'license-files::'),
    ('principles', 'principles-files::'),
    ('user-guide', 'user-guide-files::'),
]

index_template =  open('index_template', 'r')
index_data = index_template.read()
index_template.close()

for s in sections:
    print 'processing section: ', s[0]
    files = generate_file_list(os.path.join(processed_docs_root,s[0]))
    pprint.pprint(files)
    for file in files:
        command = [
            '/usr/bin/pandoc',
            '-f',
            'markdown_github',
            '-t',
            'rst',
            '-o',
            os.path.abspath(os.path.splitext(file)[0] + '.rst'),
            os.path.abspath(file)
        ]
        subprocess.call(command)

    # create toc list and merge it into the sphinx
    # index file
    toc_list = [ 3 * ' ' + os.path.splitext(f)[0] for f in files ]

    index_data = index_data.replace(s[1], '\n'.join(toc_list))
    

index_file = open('index.rst', 'w')
index_file.write(index_data)
index_file.close()

