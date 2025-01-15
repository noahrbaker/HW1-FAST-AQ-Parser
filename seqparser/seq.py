# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    assert all(nuc in ALLOWED_NUC for nuc in seq), "ILLEGAL nucleotides present"
    if reverse == True:
        return reverse_transcribe(seq)
    else:
        t_seq = ''.join(TRANSCRIPTION_MAPPING.get(nuc, '') for nuc in seq)
        return t_seq



def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    assert all(nuc in ALLOWED_NUC for nuc in seq), "ILLEGAL nucleotides present"
    t_seq = ''.join(TRANSCRIPTION_MAPPING.get(nuc, '') for nuc in seq)
    rt_seq = t_seq[::-1]
    return rt_seq