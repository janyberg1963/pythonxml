from lxml import etree
from bs4 import BeautifulSoup as bs, Tag
from xml.dom import minidom
import xml.etree.ElementTree as gfg
import os

content =[]
with open('Cucas2.xml', 'r') as f:

        content = f.readlines()
        content = "".join(content)
        bs_content = bs(content, "lxml")


result = bs_content.find_all("trigger")
#print(result)




t = result[1]
#print (t)
A = t.attrs['exp']
#print(A)
i = 0
root = minidom.Document()
xml = root.createElement("Tags")
root.appendChild(xml)


root = etree.Element('tags')
#root.set("MinVersion", "7.9.12")


child1 = etree.SubElement(root,"Tag")
child1.set("name","NewAlarms")
child1.set("type","Folder")
child1.set("path", "")



#child2 = etree.SubElement(root, "Tags")
#child2.set("MinVersion", "7.9.12")

#child3 = etree.SubElement(child2, "Tag")

#child4 = etree.SubElement(child3,"Property")
#child4.set("name","OPCServer")
#child4.text = "Ignition OPC-UA Server"

#child5 = etree.SubElement(child3,"Property")
#child5.set("name","datatype")
#child5.text = "6"

#child6 = etree.SubElement(child3,"Property")
#child6.set("name", "OPCItemPath")
#child6.text = "ns=1;s=[tags]Alarms_on"




#i=0
#while i < 10:

for x in result:

        bx = x.attrs['exp']

        #bx = result[i].attrs['exp']
    
       
        
        print (bx)
        #print(i)#

        bo = bx.replace('{', '')
        nb = bo.replace('}','')
        np = nb.replace('::','')

        lowcaps = bs()
        np1 =nb.replace('CUCAS1','Cucas1')
        np2 = np1.replace('CUCAS2','Cucas2')
        np3= np2.replace('CUCAS3','Cucas3')
        np4 = np3.replace('CUCAS4','Cucas4')
        np5 = np4.replace('CUCAS5','Cucas5')
        np6= np5.replace('CUCAS6', 'Cucas6')
        np7 = np6.replace('::',"")
       


        newnp = np7.split(']')
        newstr = newnp[0] + "]Global." + newnp[1]


        print (np) #tag path

        tname = np.split(".")
        tag_name = tname[0].split("]")
        
        #print (tname[0])
        print (tag_name[1])
        Wt_name = tag_name[1]
        Cor_Name = Wt_name.replace('[','')


        newtag1 = etree.SubElement(root,"Tag")
        newtag2 = newtag1.append

        newtag1.set('name', Cor_Name)
        newtag1.set("type", "OPC")
        newtag1.set("path","NewAlarms")

        newproperty1 = etree.SubElement(newtag1,"Property")
        newproperty1.append
        newproperty1.set('name','opcServer')
        newproperty1.text="Ignition OPC-UA Server"

        newproperty2 = etree.SubElement(newtag1,"property")
        newproperty2.append
        newproperty2.set('name','opcItempath')
        newproperty2.text = "ns=1;s=" + newstr
        

        newproperty3 = etree.SubElement(newtag1,"property")
        newproperty3.append
        newproperty3.set('name','datatype')
        newproperty3.text = "6"

        newproperty4 = etree.SubElement(newtag1,"property")
        newproperty4.append
        newproperty4.set('name','ValueSource')
        newproperty4.text = "OPC"
        
        i += 1






tree = etree.ElementTree(root)

with open('tags4.xml', "wb") as f:
    tree.write(f, pretty_print=True)

#print(etree.tostring(root, pretty_print=True))