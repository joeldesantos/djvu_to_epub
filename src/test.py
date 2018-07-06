import xml.etree.ElementTree

def is_new_row(previous_y_min, previous_y_max, y_min, y_max, tolerance=5):
  out = False

  top = previous_y_min + tolerance
  bottom = previous_y_min - tolerance

  if bottom < y_min or y_min > top:
    out = False

  top = previous_y_max + tolerance
  bottom = previous_y_max - tolerance

  if bottom < y_max or y_max > top:
    out = False
  
  return out

tree = xml.etree.ElementTree.parse('C:\\workspace\\djvu_to_epub\\input\\xml_10p.xml')
root = tree.getroot()

p = 0
text_list = []

body = root.find('BODY')
pages = body.findall('OBJECT')

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

# p = 0
# for child in root[1][1][3][0][0][0]:
#   for word in child:
#     # print (word.attrib)
#     # print (word.attrib['coords'])
#     x_min, y_min, x_max, y_max = [int(val) for val in word.attrib['coords'].split(',')]
#     # print (x_min, y_min, x_max, y_max, y_min - y_max)
#     # print (y_min, y_max, y_min - p, '\t\t'+word.text)
#     if abs(y_min - p) >= 150:
#       text_list.append('\n')
#     p = y_min
#     text_list.append(word.text)

text = ''
for word in text_list:
  if word == '\n':
    text += word + '\n'
  else:
    text += word + ' '

print(text)


