def cyk_algorithm(grammar, string):
    n = len(string)
    table = [[set() for _ in range(n)] for _ in range(n)]

    # Initialize the table with single letter productions
    for i in range(n):
        for lhs, rhs in grammar.items():
            if [string[i]] in rhs:
                table[i][i].add(lhs)

    # Fill the table for larger spans
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            for j in range(i + 1, i + length):
                for lhs, rhs in grammar.items():
                    for rule in rhs:
                        if len(rule) == 2 and rule[0] in table[i][j - 1] and rule[1] in table[j][i + length - 1]:
                            table[i][i + length - 1].add(lhs)

    return 'S' in table[0][n - 1]

# Grammar
grammar = {
    'S': [['A', 'B'], ['B', 'A']],
    'A': [['a']],
    'B': [['b']]
}

# Input string
input_string = "ab"

# Check if string belongs to the grammar
print(cyk_algorithm(grammar, input_string))
