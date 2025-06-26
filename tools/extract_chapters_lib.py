from ebooklib import epub
from ebooklib import ITEM_DOCUMENT
from lxml import etree
import os, re

def extract_chapter_titles(epub_path):
    if not os.path.exists(epub_path):
        raise FileNotFoundError(f"EPUB file not found: {epub_path}")

    book = epub.read_epub(epub_path)
    chapters = []


    for item in book.get_items_of_type(ITEM_DOCUMENT):
        filename = item.get_name().lower()
        if filename.endswith('.xhtml') and 'image' not in filename:
            chapters.append(filename)


    return chapters