import xml.etree.ElementTree as ET
tree = ET.parse('hw7.xml')
root = tree.getroot()
for student in root.findall('student'):
        name = student.find('name').text
        major = student.find('major').text
        try:
                minor = student.find('minor').text
        except AttributeError:
                minor = "N/A"
        gradyear = student.find('gradyear').text
        print("Student:", name, "Major:", major, "Minor:", minor, "Graduation year:", gradyear)


