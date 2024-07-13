from backend.src.parser_patient_details import PatientDetailsParser
from backend.src.extractor import extract
import pytest



@pytest.fixture()
def doc1_kathy():
    document_text = """17112/2020
        
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
        Triptans"""
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc2_jerry():
    document_text = """17/12/2020
        
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
    return PatientDetailsParser(document_text)

@pytest.fixture()
def doc3_empty():
    document_text = ""
    return PatientDetailsParser(document_text)

def test_get_name(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('patient_name') == "Kathy Crawford"
    assert doc2_jerry.GetField('patient_name') == "Jerry Lucas"
    assert doc3_empty.GetField('patient_name') == None

def test_get_number(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('patient_phone_number') == "(737) 988-0851"
    assert doc2_jerry.GetField('patient_phone_number') == "(279) 920-8204"
    assert doc3_empty.GetField('patient_phone_number') == None

def test_get_chickenpox(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('chickenpox') == "IMMUNE"
    assert doc2_jerry.GetField('chickenpox') == "IMMUNE"
    assert doc3_empty.GetField('chickenpox') == None

def test_get_measles(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('measles') == "IMMUNE"
    assert doc2_jerry.GetField('measles') == "NOT IMMUNE"
    assert doc3_empty.GetField('measles') == None

def test_get_medical_insurance(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('has_medical_insurance') == "Yes."
    assert doc2_jerry.GetField('has_medical_insurance') == "Yes"
    assert doc3_empty.GetField('has_medical_insurance') == None

def test_get_allergies(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('allergies') == "Peanuts"
    assert doc2_jerry.GetField('allergies') == "N/A"
    assert doc3_empty.GetField('allergies') == None

def test_get_daily_medications(doc1_kathy, doc2_jerry, doc3_empty):
    assert doc1_kathy.GetField('regular_medications') == "Triptans"
    assert doc2_jerry.GetField('regular_medications') == "N/A"
    assert doc3_empty.GetField('regular_medications') == None

def test_parse(doc1_kathy, doc2_jerry, doc3_empty):
    record_kathy = doc1_kathy.parse()
    assert record_kathy == {
        'patient_name': 'Kathy Crawford',
        'patient_phone_number': '(737) 988-0851',
        'chickenpox' : 'IMMUNE',
        'measles' : 'IMMUNE',
        'has_medical_insurance' : 'Yes.',
        'allergies' :'Peanuts',
        'regular_medications' : 'Triptans'
    }

    record_jerry = doc2_jerry.parse()
    assert record_jerry == {
        'patient_name': 'Jerry Lucas',
        'patient_phone_number': '(279) 920-8204',
        'chickenpox' : 'IMMUNE',
        'measles' : 'NOT IMMUNE',
        'has_medical_insurance' : 'Yes',
        'allergies' :'N/A',
        'regular_medications' : 'N/A'
    }

    record_empty = doc3_empty.parse()
    assert record_empty == {
        'patient_name': None,
        'patient_phone_number': None,
        'chickenpox' : None,
        'measles' : None,
        'has_medical_insurance' : None,
        'allergies' :None,
        'regular_medications' : None
    }