#!/usr/bin/env python3
# Yoinked shamelessly from https://stackoverflow.com/a/47283224

from glob import glob
from os import getcwd, path
from PyPDF2 import PdfReader, PdfWriter

wdir = getcwd()
merger = PdfWriter()
#merger.add_outline()

for ix, filename in enumerate(glob('tags/*.pdf')):
    tag_name = path.basename(filename).rstrip('.pdf').replace('_', ' ').strip()
    print(tag_name)
    merger.append(path.join(wdir, filename), outline_item=tag_name)

merger.write("merged-pdf.pdf")
merger.close()
