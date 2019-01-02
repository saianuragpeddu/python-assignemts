def baseComposition(dna_seq):
    result = {'A': 0, 'T':0, 'C':0, 'G':0 }
    for var in dna_seq:
        if var in result:
            result[var] += 1
    return result

print(baseComposition("ATTTCGGAGCAATCGC"))
