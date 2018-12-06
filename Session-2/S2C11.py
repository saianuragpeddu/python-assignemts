def pairwiseScore(seqA, seqB):
  '''1+1+3-1-1+1+3+1-1-1+1-1-1-1'''
  print
  signed = ''
  score = 0
  for i in range(len(seqA)):
    if(seqA[i] == seqB[i]):         
        signed += '|'
        if i > 0 and signed[len(signed)-2]=='|':
            score += 3
        else:
            score += 1

    else:
        signed += ' '
        score -=1
  return seqA+"\n"+signed+"\n"+seqB+"\n"+'score:'+ str(score)


print(pairwiseScore("ATTCGT", "ATCTAT"))  
