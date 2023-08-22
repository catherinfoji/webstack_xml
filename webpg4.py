import xmlschema as xml
xml_file = "webpg4.xml"
xsd_file = "webpg4.xsd"

validator = xml.XMLSchema(xsd_file)
if validator.is_valid(xml_file):
    print("XML file is valid against the XSD schema.")
else:
    print("XML file is not valid against the XSD schema.")
    print(validator.validate(xml_file))
    
    
    
    