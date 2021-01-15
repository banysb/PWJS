from xml.dom import minidom

xmlData = minidom.parse("files/simple.xml")
doc_root = xmlData.documentElement

node = xmlData.createElement("food")

name = xmlData.createElement("name")
name.appendChild(xmlData.createTextNode("pizza"))
node.appendChild(name)

price = xmlData.createElement("price")
price.appendChild(xmlData.createTextNode("12 PLN"))
node.appendChild(price)

descr = xmlData.createElement("description")
descr.appendChild(xmlData.createTextNode("pyszna pizza"))
node.appendChild(descr)

calories = xmlData.createElement("calories")
calories.appendChild(xmlData.createTextNode("1000"))
node.appendChild(calories)

doc_root.appendChild(node)


with open("files/new.xml", "w") as fs:
    fs.write(xmlData.toxml())
    fs.close()