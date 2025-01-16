# write tests for transcribe functions
import pytest

# from seqparser import (
#         transcribe,
#         reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    seq_tup_in = ("test_in", "ACTGAACCC")
    seq_tup_bad = ("test_in", "NNNNNNNN")
    seq_out = "UGACUUGGG"
    assert transcribe(seq_tup_in[1]) == seq_out, "Transcription function not working as expected"
    with pytest.raises(AssertionError):
        transcribe(seq_tup_bad[1])


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    seq_tup_in = ("test_in", "ACTGAACCC")
    seq_tup_bad = ("test_in", "NNNNNNNN")
    seq_out = "GGGUUCAGU"
    # check the argument version works
    assert transcribe(seq_tup_in[1], reverse=True) == seq_out, "Transcription function (reverse=True) not working as expected"
    # check the base function works
    assert reverse_transcribe(seq_tup_in[1]) == seq_out, "Reverse transcription function not working as expected"
    with pytest.raises(AssertionError):
        transcribe(seq_tup_bad[1])