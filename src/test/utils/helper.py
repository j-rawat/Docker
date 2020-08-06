import os
import sys
from xml.etree import ElementTree as ET
from . import utility as util


class Helper:

    def testme(self):
        print("you just reached me")

    def get_wsdl(self):
        var_name = sys.argv[1]
        var_value = sys.argv[2]

        os.environ[var_name] = var_value

        return os.getenv(var_name)

    def getPayload(self, file_name, *args):
        full_file = os.path.abspath(os.path.join('test_data', file_name))

        print(full_file)

        tree = ET.parse(full_file)

        root = tree.getroot()
        for x in args:
            unique = util.get_unique()
            for e in root.iter(x):
                e.text = unique

        updated_xml = ET.tostring(root).decode()
        return updated_xml

    def get_tag_text(self, payload, tag_name):
        root = ET.fromstring(payload)
        tag_text = root.find(tag_name)
        return tag_text.text
