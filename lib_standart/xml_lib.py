import xml.etree.ElementTree as ET
from xml.dom import minidom

# Leer archivo

#tree = ET.parse('../resources/example.xml')
#root = tree.getroot()

#print(root.tag)

#for x in root:
#    print(x.tag, x.attrib)

#print(root[0][1].text)

# Modificar achivo

#root[0][1].text = "Loquesea"
#tree.write('../resources/example.xml')
#for x in root.iter('title'):
#    new_rank = str(x.text) + "agregado"
#    x.text = str(new_rank)
#    x.set('updated', 'yes')
#tree.write('../resources/example.xml')

# Crear xml nuevo


root = ET.Element("root")
doc = ET.SubElement(root, "doc")
ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("../resources/nuevo.xml", "w") as f:
    f.write(xmlstr)

