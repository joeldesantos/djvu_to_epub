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

import DJVU_Template


class IndexTemplate(abc.ABC):

    def __init__(self, lrx, lry, tlx, tly, margin=0):
        self.lrx = lrx
        self.lry = lry
        self.tlx = tlx
        self.tly = tly
        self.margin = margin

    def fits(self, lrx, lry, tlx, tly):
        out = True
        if self.lrx < (lrx - self.margin)
        and self.lry < (lry - self.margin)
        and self.tlx > (tlx + self.margin)
        and self.tly > (tly + self.margin):
            out = False

        return out
