# This is a fork from https://github.com/saladeen/vitalsource_screenshot_to_pdf.git

I added the possibility to simulate a key instead a mouse clic (see `app.py`) and I commented the file `coordinfo.txt` for the users that use MacOS with a Retina display (they must multiply by 2 the coordonate - except for the mouse clic).

I use `Pynput` to simulate the keyboard.

Everything else is pretty the same :-)

# Convert anything from your screen into a PDF

Largely yoinked from here: https://github.com/manhtai/vitalsource-printer

This script simulates clicking through and screenshotting every page of the text, then putting together those images into a single PDF

# Usage:

Create an env:

`python3 -m venv env`
`source env/bin/activate`

Install:
`pip install -r requirements.txt`

Get the coordinates of the top left corner of the page, bottom right corner, and the next button using coord_getter.py:

`python coord_getter.py`

Type the coordinate pairs in the file `coordinfo.txt`, along with the total number of pages, as instructed in the file.

Then open up Bookshelf and the book you want to download, and run:

`python app.py`

Make sure you aren't covering up the screenshot area or next button. Works with multiple monitors. Book will be saved as book.pdf
