def mRNAtranscription(dna_template):
    dna2rna = {'A':'U', 'T':'A', 'C':'G', 'G':'C'  }
    mRNA = ''
    for base in dna_template:
        mRNA+=(dna2rna.get(base))
    return mRNA

print(mRNAtranscription("ATCGATTG"))
print(mRNAtranscription("TAGCTTGC"))
