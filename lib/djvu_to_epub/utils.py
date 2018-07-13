"""This file is part of djvu_to_epub.

Copyright (c) 2018 Joel de Santos <joeldesantos@gmail.com>

djvu_to_epub is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

djvu_to_epub is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with djvu_to_epub.  If not, see <http://www.gnu.org/licenses/>.

"""

def get_info_from_djvu_file(file):
    """Parses a DJVU file and returns relevant information.
    
    Parses a DJVU file and returns relevant information, like wheter or not OCR layer is present, min and max text coordinates, etc.
    
    Arguments:
        file {filename or file object} -- DJVU filename or file object
    """
    pass

def get_ocr_layer_xml_from_djvu_file(djvu_file, xml_file=djvu_file+'.xml'):
    pass

def get_text_from_ocr_layer_xml(xml_file, template=None, templates=[], split=[], formatter=TextFormatter):
    pass

def create_book(id, title, language, author, css):
    pass

def add_chapters_to_book(book, chapters):
    pass

def create_epub(book, epub_file):
    pass