from lxml import etree

root = etree.Element("Tags", MinVersion="8.0.0")

child1 = etree.SubElement(root,"Tag")
child1.set("name"," ")
child1.set("type","Provider")


child2 = etree.SubElement(child1, "Tags")
child2.set("MiniVersion", "8.0.0")

child3 = etree.SubElement(child2, "Tag")
child3.set("name","Atemp")
child3.set("type","AtomicTag")

child4 = etree.SubElement(child3,"Property")
child4.set("name","valueSource")
child4.text = "expr"

child5 = etree.SubElement(child3,"Property")
child5.set("name","expression")
child5.set("name","datatype")
child5.text = "6"

child6 = etree.SubElement(child3,"Property")
child6.set("name", "sourceTagPath")
child6.text = "[tags]Alarms_on"


i = 1

while i < 6:



    newtag1 = etree.SubElement(child2,"Tag")
    newtag2 = newtag1.append

    newtag1.set('name','newtagalarm')

    newproperty1 = etree.SubElement(newtag1,"Property")
    newproperty1.append
    newproperty1.set('name','valuesource')
    newproperty1.text="newexp"

    newproperty2 = etree.SubElement(newtag1,"property")
    newproperty2.append
    newproperty2.set('name','expression')
    newproperty2.set('name','datatype')
    newproperty2.text = '6'

    newproperty3 = etree.SubElement(newtag1,"property")
    newproperty3.append
    newproperty3.set('name','sourcetagpath')
    newproperty3.text = '[tag]newalarm2'
    
    i += 1

#newname = etree.SubE.lement(child4,"Property")
#newname.text = "newProp"
#newtag.append(newname)







tree = etree.ElementTree(root)

with open('tags2.xml', "wb") as f:
    tree.write(f, pretty_print=True)

#print(etree.tostring(root, pretty_print=True))
