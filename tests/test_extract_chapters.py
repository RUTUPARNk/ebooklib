import os
import sys

# Add the project root to the path so we can import tools
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tools.extract_chapters_lib import extract_chapter_titles

def test_extract_chapter_titles():
    test_file = os.path.join(os.path.dirname(__file__), "data/1.epub")

    assert os.path.exists(test_file), "Test EPUB file not found"

    chapters = extract_chapter_titles(test_file)


    #Expect at least 1-2 chapters in a valid EPUB
    assert len(chapters) >= 2

    # Pretty Optional: check a known file is in there
    assert any("ch1" in ch for ch in chapters), "Expected chapter not found"
