import os

import json
import pprint

from xml.dom import minidom
import xml.etree.ElementTree as ET
import xmltodict

# with open('file.txt', 'r') as file:
#     print(file.readlines())
#
#
# with open('file2.txt', 'r') as file:
#     for l in file:
#         print(l)
#
#
# f = open('file2.txt', 'wa')
# f.write('ndjsner')
# f.close()
#
# with open('file2.txt', 'wa') as f:
#     f.write('cnhsjehw')

# if os.path.exists('file2.txt'):
#     os.remove('file2.txt')


data = {
    'human1': {
        'gender': 'm',
        'name': 'Vasya',
        'age': '19',
        'birth': {
            'country': 'Ukraine',
            'city': 'Kyiv',
            'postal': '02222'
        }
    },
    'human2': {
        'gender': 'f',
        'name': 'Valya',
        'age': '20',
        'birth': {
            'country': 'USA',
            'city': 'New York',
            'postal': '01111'
        }
    }
}


def write_json(filename: str, data: dict) -> None:
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file)


write_json('peoples', data)


def print_json(filename: str) -> None:
    with open(f'{filename}.json', 'r') as file:
        print(json.load(file))


def print_json_pretty(filename: str) -> None:
    from pprint import pp
    with open(filename, 'r') as file:
        pp(json.load(file))


# print_json_pretty('peoples.json')

def write_xml(filename: str, data: dict) -> None:
    root = ET.Element('users')
    for user_id, user_data in data.items():
        user = ET.SubElement(root, user_id)
        #user.attrib['id'] = user_id
        for key, value in user_data.items():
            if isinstance(value, dict):
                sub_element = ET.SubElement(user, key)
                for sub_key, sub_value in value.items():
                    sub_sub_elements = ET.SubElement(sub_element, sub_key)
                    sub_sub_elements.text = str(sub_value)
            else:
                element = ET.SubElement(user, key)
                element.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(f'{filename}.xml')


write_xml('my_users', data)

def print_xml(filename: str) -> None:
    document = minidom.parse(filename)
    print(document.toxml())

def print_xml_data(filename: str):
    tree = ET.parse(filename)
    root = tree.getroot()
    print(root)
    for child in root:
        print(child.tag, child.attrib)
        for sub_child in child:
            print(sub_child.tag, sub_child.text)
            for sub_sub_child in sub_child:
                print(sub_sub_child.tag, sub_sub_child.text)




# print_xml('my_users.xml')
# print_xml_data('my_users.xml')


def get_dict_from_xml(filename: str) -> dict:
    with open(filename) as file:
        data =  xmltodict.parse(file.read())
        return data


#pprint.pp(get_dict_from_xml('my_users.xml'))