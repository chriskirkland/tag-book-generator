#!/usr/bin/env python3
# Yoinked shamelessly from https://stackoverflow.com/a/47283224

# install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
from PIL import Image
from glob import glob
from os import getcwd, path
from pdf2image import convert_from_path

wdir = getcwd()
images = [
    convert_from_path(path.join(wdir, f))[0]
    for f in glob('tags/*.pdf')
]

pdf_path = "book.pdf"

images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
