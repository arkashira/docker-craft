import pytest
from axentx_product import QualityGate

def test_validate_valid_product():
    gate = QualityGate()
    product = {"name": "Axentx Tool", "pain_score": 10, "willingness_to_pay": 100}
    assert gate.validate(product) is True

def test_validate_no_pain():
    gate = QualityGate()
    product = {"name": "Bad Tool", "pain_score": 0, "willingness_to_pay": 100}
    assert gate.validate(product) is False

def test_validate_no_wtp():
    gate = QualityGate()
    product = {"name": "Free Tool", "pain_score": 10, "willingness_to_pay": 0}
    assert gate.validate(product) is False

def test_validate_missing_fields():
    gate = QualityGate()
    product = {"name": "Empty Tool"}
    assert gate.validate(product) is False

def test_validate_negative_scores():
    gate = QualityGate()
    product = {"name": "Negative Tool", "pain_score": -5, "willingness_to_pay": 100}
    assert gate.validate(product) is False

def test_validate_invalid_input_type():
    gate = QualityGate()
    assert gate.validate(None) is False
    assert gate.validate("not_a_dict") is False
