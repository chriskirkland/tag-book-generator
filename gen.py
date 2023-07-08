#!/usr/bin/env python3
# Yoinked shamelessly from https://stackoverflow.com/a/47283224

from glob import glob
from os import getcwd, path
from PyPDF2 import PdfReader, PdfWriter

OUTPUT = 'tagbook.pdf'

wdir = getcwd()
merger = PdfWriter()
#merger.add_outline()

for ix, filename in enumerate(glob('tags/*.pdf')):
    tag_name = path.basename(filename).rstrip('.pdf').replace('_', ' ').strip()
    merger.append(path.join(wdir, filename), outline_item=tag_name)
    print('[%d] added "%s"' % (ix+1, tag_name))

merger.write(OUTPUT)
merger.close()
print(OUTPUT)
