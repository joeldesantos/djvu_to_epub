import xml.etree.ElementTree
from ebooklib import epub

print('Open source')
tree = xml.etree.ElementTree.parse('C:\\workspace\\djvu_to_epub\\input\\xml.xml')
root = tree.getroot()

p = 0
text_list = []

body = root.find('BODY')
pages = body.findall('OBJECT')

print('Parse xml')
for page in pages:
  hidden_text = page.find('HIDDENTEXT')
  page_column = hidden_text.find('PAGECOLUMN')
  region = page_column.find('REGION')
  paragraph = region.find('PARAGRAPH')
  for line in paragraph.findall('LINE'):
    for word in line:
      # print(word.text)
      x_min, y_min, x_max, y_max = [int(val) for val in word.attrib['coords'].split(',')]
      if abs(y_min - p) >= 150:
        text_list.append('\n')
      p = y_min
      text_list.append(word.text)

print('Create paragraphs')
text = ''
for word in text_list:
  if word == '\n':
    text += word + '\n'
  else:
    text += word + ' '

# print(text)
text_paragraphs = text.split('\n\n')

print('Create epub')
book = epub.EpubBook()

# set metadata
book.set_identifier('ISBN 978-0-9847828-5-7')
book.set_title('CRACKING the CODING INTERVIEW')
book.set_language('en')

book.add_author('Gayle Laakmann McDowell')

print('Add content to the epub book')
# create chapter
c1 = epub.EpubHtml(title='CRACKING the CODING INTERVIEW', file_name='book.xhtml', lang='en')
tmp='<h1>CRACKING the CODING INTERVIEW</h1>'
for p in text_paragraphs:
  tmp += '<p>' + p + '</p>'
c1.content=u''+tmp

# add chapter
book.add_item(c1)

# define Table Of Contents
book.toc = (epub.Link('book.xhtml', 'CRACKING the CODING INTERVIEWa', 'CRACKING the CODING INTERVIEWb'),
       (epub.Section('CRACKING the CODING INTERVIEWc'),
       (c1, ))
      )

# add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define CSS style
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# add CSS file
book.add_item(nav_css)

# basic spine
book.spine = ['nav', c1]

print('Write book to disk')
# write to the file
epub.write_epub('c:/workspace/djvu_to_epub/output/test.epub', book, {})


