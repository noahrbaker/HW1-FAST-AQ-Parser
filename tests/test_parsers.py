# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # blank file
    with pytest.raises(ValueError):
        # Test with an empty file
        fa_blank = FastaParser("tests/blank.fa")
        next(iter(fa_blank))  # this should fail
    
    # bad file
    with pytest.raises(ValueError):
        fa_bad = FastaParser("tests/bad.fa")
        next(iter(fa_bad))  # this should fail
    
    # test file as list
    fa_test = list(FastaParser("tests/good.fa"))
    fa_good = [("seq0", "TGATT"), ("seq1", "TCCGC")]
    assert len(fa_test) > 0, "Test FASTA should read in 1 or more lines"
    assert all(len(fa_item) == 2 for fa_item in fa_test), "Each item should be a tuple of 2 items"
    assert fa_test == fa_good, "Test FASTA not reading in correctly"


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # test FASTQ file for None
    fq_test = FastaParser("data/test.fq")
    assert next(iter(fq_test))[0] is None, "Reading a FASTQ should produce a None"


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    # blank file
    with pytest.raises(ValueError):
        # Test with an empty file
        fq_blank = FastqParser("tests/blank.fq")
        next(iter(fq_blank))  # this should fail
    
    # bad file
    fq_bad = FastqParser("tests/bad.fq")
    assert next(iter(fq_bad))[0] is None, "FastqParser does not return a None for a bad fastq"
    
    # test file as list
    fq_test = list(FastqParser("tests/good.fq"))
    fq_good = [("seq0", "TGTGG", "*540("), ("seq1", "CCCCG", "3(<#/")]
    assert len(fq_test) > 0, "Test FASTA should read in 1 or more lines"
    assert all(len(fq_item) == 3 for fq_item in fq_test), "Each item should be a tuple of 3 items"
    assert fq_test == fq_good, "Test FASTA not reading in correctly"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # test FASTA file for None
    fa_test = FastqParser("data/test.fa")
    assert next(iter(fa_test))[0] is None, "Reading a FASTA should produce a None"