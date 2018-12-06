def tictactoe(moves):
    for r in range(len(moves)):
        for c in range(len(moves[r])):      
            if moves[0][c]==moves[1][c]==moves[2][c]:
                return "\'%s\' wins (%s)." % ((moves[0][c]),'vertical')
            elif moves[r][0]==moves[r][1]==moves[r][2]:
                return "\'%s\' wins (%s)."%((moves[r][0]),'horizontal')
            elif moves[0][0]==moves[1][1]==moves[2][2]:
                return "\'%s\' wins (%s)."%((moves[0][0]),'diagonal')
            elif moves[0][2]==moves[1][1]==moves[2][0]:
                return "\'%s\' wins (%s)."%((moves[0][2]),'diagonal')
    return 'Draw.'

print(tictactoe[('X', ' ', 'O'),
                (' ', 'O', 'O'),
                ('X', 'X', 'X')])



