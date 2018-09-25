from dna import DNA
from rna import RNA
import pytest

def test_bad_sequence_raises_error():
    with pytest.raises(ValueError):
        DNA('ATB')
        RNA('AUB')

def test_complimentary_sequences_works():
    assert DNA('GTC').complimentary_sequence == DNA('CAG')
    assert DNA('ATC').complimentary_sequence == DNA('TAG')
    assert RNA('GUC').complimentary_sequence == RNA('CAG')
    assert RNA('AUC').complimentary_sequence == RNA('UAG')