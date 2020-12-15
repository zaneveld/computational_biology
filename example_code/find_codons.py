

def get_codons(seq):
  """Given a coding sequence, return each codon
     seq -- a string representing the sequence

     NOTE: this code does not detect start/stop codons
     it just splits up the sequence
  """
  codon_length = 3
  last_codon_start = len(seq) - codon_length

  codons = []
  for start in range(0,last_codon_start,codon_length):
      current_codon = seq[start:start + codon_length]
      codons.append(current_codon)

  return codons

print("Example result for AAATTTCCCGGG:", get_codons("AAATTTCCCGGG"))
