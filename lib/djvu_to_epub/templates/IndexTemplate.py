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

    def __init__(self, x_min, y_min, x_max, y_max, margin=0):
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max
        self.margin = margin

    def fits(self, x1, y1, x2, y2):
        out = True
        if self.x_max < (x1 - self.margin)
        and self.y_max < (y1 - self.margin)
        and self.x_min > (x1 + self.margin)
        and self.y_min > (y2 + self.margin):
            out = False

        return out
