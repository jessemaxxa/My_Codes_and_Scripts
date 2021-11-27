import xml.etree.ElementTree as ET
tree = ET.parse('/home/hondaunispree/Masscan/Port80/port80.xml')
root = tree.getroot()
print(root.tag)
for child in root:
	print(child.tag, child.attrib)

for x in child[0]:
	print(x.text)