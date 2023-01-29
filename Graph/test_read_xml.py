from read_xml import read_XML
from prettify import minify,beautify
path = "sample.xml"
users = read_XML(path)
print(len(users))