from DFA import DFA
if __name__ == "__main__":
    transitions_func = [
        {
            'current_state' : 0,
            'input_value' : '0',
            'next_state': 2
        },
        {
            'current_state' : 0,
            'input_value' : '1',
            'next_state': 1
        },
        {
            'current_state' : 1,
            'input_value' : '0',
            'next_state': 3
        },
        {
            'current_state' : 1,
            'input_value' : '1',
            'next_state': 0
        },
        {
            'current_state' : 2,
            'input_value' : '0',
            'next_state': 0
        },
        {
            'current_state' : 2,
            'input_value' : '1',
            'next_state': 3
        },
        {
            'current_state' : 3,
            'input_value' : '0',
            'next_state': 1
        },
        {
            'current_state' : 3,
            'input_value' : '1',
            'next_state': 2
        },
    ]

    dfa = DFA({0,1,2,3},{'0','1'},transitions_func,0,[0])
    dfa.print_DFA()

    print('\nInput: "110"')
    dfa.get_input('110')

    print('\nInput: "1"')
    dfa.get_input('1')

    print('\nInput: "110101"')
    print(dfa.get_input('110101'))

    test1 = dfa.get_input("110")
    print(test1)
    print(test1)
    # dfa.initial_state = 1