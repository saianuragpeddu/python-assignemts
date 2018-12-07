def stripComment(sentence):
    codeonly  = ""
    for ch in sentence:
        if ch == '#':
            break
            codeonly += '#'
        codeonly+=ch  
    return codeonly

print(stripComment('Hello # World'))
