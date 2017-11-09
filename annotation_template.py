'''Custom design of template for exported annotations.

# Copyright 2016 Guang-zhi XU
#
# This file is distributed under the terms of the
# GPLv3 licence. See the LICENSE file for details.
# You may use, distribute and modify this code under the
# terms of the GPLv3 license.

Update time: 2017-11-07 20:16:35.
'''



# spaces to indent for subsequent lines of a long text (e.g. highlighted
# texts). Spaces or \t for tabs.
INDENT_EACH_ENTRY='          '


# Line width to wrap long texts 
WRAP_EACH_ENTRY=80

# Maximum geometrical distance (in pixels) to associate a piece of note in
# Mendeley to a block of highlighted texts.
# If the note sits on top of the highlighted texts (e.g. you right click on
# the highlights and add note from the pop up menu, the note will always be
# associated with that highlight.
# If the note is inserted OUTSIDE of the highlighted texts (e.g. added at the
# page margin), this parameter controls how far the distance could be between
# the note and its NEAREST highlight text block for them to be associated.
# For reference, a normal PDF has a width of 612 and a height of 792 pixels,
# but this changes from file to file.

MAX_ASSOCIATE_DIST=5


# Template for notes asscoiated with highlights.

# You can change the template layout inside the triple quotes '''...'''.
# {} indicates a variable placeholder.
# Available variables one can use:

# text : note content for a note, or highlighted texts for a highlight.
# page : page number of the note/highlight in the PDF file, not necessarily
#        the same as printed out at the page margin.
# title: title of the document.
# tags : tag list.
# ctime: creation time.
# author : author(s) of the document.
# note_author: your name.
# citationkey: citation key.
# num : an integer id of the note/highlight, counting restarts in each document.

# NOTE: variable names are case sensitive, use exact words.
# DONT put spaces inside curly brackets {}.
# Indentation control can be done by adding/removing leading spaces, and adjusting
# the INDENT_EACH_ENTRY parameter, which controls only subsequent lines.

HIGHLIGHT_NOTE_ENTRY_TEMPLATE=u'''\

    Highlight #: {num}
    Page #: {page}
    Created : {ctime}
    Text : {ori_text}
    Comment : {text}

---

'''

# Template for notes not associated with highlights
NOTE_ONLY_ENTRY_TEMPLATE=u'''\

    Comment #: {num}
    Page #: {page}
    Created : {ctime}
    Comment : {text}

---

'''

# Template for highlights not associated with notes
HIGHLIGHT_ONLY_ENTRY_TEMPLATE=u'''\

    Highlight #: {num}
    Page #: {page}
    Created : {ctime}
    Text : {text}

---

'''



