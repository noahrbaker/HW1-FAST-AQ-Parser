from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # function for easy printing
    def iterate_n_print(parser_obj, reverse=False):
        for parser_rec in parser_obj:
            name, seq, *optional = parser_rec
            t_seq = transcribe(seq, reverse=reverse)
            print(name)
            print(t_seq)
    
    # Create instance of FastaParser
    fa_seq = FastaParser("data/test.fa")
    # Create instance of FastqParser
    fq_seq = FastqParser("data/test.fq")

    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print("Transcribe the FASTA")
    iterate_n_print(fa_obj)

    
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print("Transcribe the FASTQ")
    iterate_n_print(fq_obj)


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print("Reverse transcribe the FASTA")
    iterate_n_print(fa_obj, reverse=True)
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print("Reverse transcribe the FASTQ")
    iterate_n_print(fq_obj, reverse=True)

    # comment to test if actions work


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
