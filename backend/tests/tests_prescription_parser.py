from backend.src.parser_presciption import PrescriptionParser
from backend.src.extractor import extract
import pytest



@pytest.fixture()
def doc1_maria():
    document_text = """Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 mg

Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,

Finish in 2.5 weeks
Lialda - take 2 pill everyday for 1 month

Refill: 2 times"""
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc2_virat():
    document_text = """Dr John Smit} h, M.D

2 Non-Important Street,

New York, Phone (000)-213- ~2222

Name: Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

Ry

, Omeprazole 40 me

Directions: Use two tablets daily for three months

Refill: 3 times"""
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc3_empty():
    document_text = ""
    return PrescriptionParser(document_text)

def test_get_name(doc1_maria, doc2_virat, doc3_empty):
    assert doc1_maria.GetField('patient_name') == "Marta Sharapova"
    assert doc2_virat.GetField('patient_name') == "Virat Kohli"
    assert doc3_empty.GetField('patient_name') == None

def test_get_address(doc1_maria, doc2_virat, doc3_empty):
    assert doc1_maria.GetField('patient_address') == "9 tennis court, new Russia, DC"
    assert doc2_virat.GetField('patient_address') == "2 cricket blvd, New Delhi"
    assert doc3_empty.GetField('patient_address') == None

def test_get_medicines(doc1_maria, doc2_virat, doc3_empty):
    assert doc1_maria.GetField('medicines') == ("Prednisone 20 mg\n\n"
                                                "Lialda 2.4 gram")
    assert doc2_virat.GetField('medicines') == "Omeprazole 40 mg"
    assert doc3_empty.GetField('medicines') == None

def test_get_instructions(doc1_maria, doc2_virat, doc3_empty):
    assert doc1_maria.GetField('instructions') == ("Prednisone, Taper 5 mg every 3 days,\n"
                                                   "Finish in 2.5 weeks\n"
                                                   "Lialda - take 2 pill everyday for 1 month")
    assert doc2_virat.GetField('instructions') == "Use two tablets daily for three months"
    assert doc3_empty.GetField('instructions') == None

def test_get_refills(doc1_maria, doc2_virat, doc3_empty):
    assert doc1_maria.GetField('refills') == "2"
    assert doc2_virat.GetField('refills') == "3"
    assert doc3_empty.GetField('refills') == None

def test_parse(doc1_maria, doc2_virat, doc3_empty):
    record_maria = doc1_maria.parse()
    assert record_maria == {
        'patient_name' : 'Maria Sharapova',
        'patient_address' : '9 tennis court, new Russia, DC',
        'medicines' : 'Prednisone 20 mg\n'
                        'Lialda 2.4 gram',
        'instructions':'Prednisone, Taper 5 mg every 3 days,\n'
                        'Finish in 2.5 weeks\n'
                        'Lialda - take 2 pill everyday for 1 month',
        'refills' : '2'
    }

    record_virat = doc2_virat.parse()
    assert record_virat == {
        'patient_name': 'Virat Kohli',
        'patient_address': '9 tennis court, new Russia, DC',
        'medicines': 'Omeprazole 40 mg',
        'instructions': 'Use two tablets daily for three months',
        'refills': '3'
    }

    record_empty = doc3_empty.parse()
    assert record_maria == {
        'patient_name': None,
        'patient_address': None,
        'medicines': None,
        'instructions': None,
        'refills': None
    }