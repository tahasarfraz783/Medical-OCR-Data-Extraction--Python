from backend.src.parser_generic import MedicalDocParser
import re


class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name' : self.GetField('patient_name'),
            'patient_address' : self.GetField('patient_address'),
            'medicines' : self.GetField('medicines'),
            'instructions' : self.GetField('instructions'),
            'refills' : self.GetField('refills')
        }
    def GetField(self, field_name):
        pattern = ''
        flags = 0

        pattern_dict = {
            'patient_name': {'pattern' : r"Name:(.*) Date", 'flags' : 0},
            'patient_address': {'pattern' : r"Address:(.*)\n", 'flags' : 0},
            'medicines': {'pattern' : r"Address:[^\n]*(.*)Directions", 'flags' : re.DOTALL},
            'instructions': {'pattern' :r"Directions:(.*)Refill", 'flags' : re.DOTALL},
            'refills': {'pattern' : r"Refill:(.*) times", 'flags' : 0}
        }

        pattern_obj= pattern_dict.get(field_name)

        if pattern_obj:
            matches = re.findall(pattern_obj['pattern'], self.text, flags = pattern_obj['flags'])
            if len(matches) > 0:
                return matches[0].strip()