from backend.src.parser_generic import MedicalDocParser
import re


class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)


    def parse(self):
        return {
            'patient_name': self.GetField('patient_name'),
            'patient_phone_number': self.GetField('patient_phone_number'),
            'chickenpox': self.GetField('chickenpox'),
            'measles': self.GetField('measles'),
            'has_medical_insurance': self.GetField('has_medical_insurance'),
            'allergies': self.GetField('allergies'),
            'regular_medications': self.GetField('regular_medications')
        }

    def GetField(self, field_name):
        pattern = ''
        flags = 0

        pattern_dict = {
            'patient_name': {'pattern': r"Birth Date(.*?)\w+ \d \d{4}", 'flags':re.DOTALL},
            'patient_phone_number': {'pattern': r"(\(\d{3}\) \d{3}-\d{4}) Weight", 'flags': 0},
            'chickenpox': {'pattern': r"(IMMUNE |NOT IMMUNE )\w+", 'flags': re.DOTALL},
            'measles': {'pattern': r"IMMUNE (NOT IMMUNE|IMMUNE)", 'flags': re.DOTALL},
            'has_medical_insurance': {'pattern': r"insurance\?\n.*?(\S+)", 'flags': re.DOTALL},
            'allergies': {'pattern': r"allergies:\n.*?(\S+)", 'flags': re.DOTALL},
            'regular_medications': {'pattern': r"regularly:\n(.*)", 'flags': re.DOTALL},

        }

        pattern_obj = pattern_dict.get(field_name)

        if pattern_obj:
            matches = re.findall(pattern_obj['pattern'], self.text, flags=pattern_obj['flags'])
            if len(matches) > 0:
                return matches[0].strip()


if __name__ == '__main__':
    doc1 = """17112/2020
    
    Patient Medical Record
    
    Patient Information Birth Date
    Kathy Crawford May 6 1972
    (737) 988-0851 Weight
    9264 Ash Dr 95
    New York City, 10005
    United States Height:
    190
    In Casc of Emergency
    ce a  E ee
    Simeone Crawford 9266 Ash Dr
    New York City, New York, 10005
    
    Home phone United States
    
    (990) 375-4621
    Work phone
    
    Genera! Medical History
    
    cree ete amegras mater
    
    ee
    
    Chicken Pox (Varicella): Meacies:
    
    IMMUNE IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    No
    List any Medical Problems (asthma, seizures, headaches):
    Migraine
    E: Name of Insurance Company: a )
    
    f Random Insuarance Company - 4789 Bollinger Rd
    
    aa Policy Number: Jersey City, New Jersey, 07030
    
    71 1520731 3 Expiry Date:
    30 December 2020
    
    Do you have medical insurance?
    
    Yes.
    
    Medical Insurance Details
    
    List any allergies:
    
    Peanuts
    
    List any medication taken regularly:
    Triptans
    """
    doc2 = """17/12/2020
    
    Patient Medical Record
    
    Patient Information Birth Date
    Jerry Lucas May 2 1998
    (279) 920-8204 Weight:
    4218 Wheeler Ridge Dr 57
    
    Buffalo, New York, 14201
    
    United States Height:
    
    170
    
    In Case of Emergency
    ee
    
    Joe Lucas 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone . United States
    Work phone
    
    General Medical History
    
    Chicken Pox (Varicelia): Measles:
    
    IMMUNE NOT IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    “Yes
    
    List any Medical Problems (asthma, seizures, headaches):
    N/A
    —_—_
    
    Name of Insurance Company:
    
    Random Insuarance Company 4218 Smeeler Ridge Dr
    i Buf
    Policy Number: i” ae New York. 14206
    5638746258
    Expiry Date:
    
    31 December 2020
    
    Do you have medical insurance?
    
    Yes
    
    Medical Insurance Details
    
    List any allergies:
    
    N/A
    
    List any medication taken regularly:
    
    N/A"""

    print(PatientDetailsParser(doc1).parse())
    print(PatientDetailsParser(doc2).parse())

