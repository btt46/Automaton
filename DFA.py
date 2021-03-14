import pandas as pd
from tabulate import tabulate

class DFA:
    def __init__(self, states, input_set, transitions, initial_state, final_states):
        self.states =  set(states)
        self.input_set = set(input_set)
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = set(final_states)
        self.current_state = self.initial_state

    def print_transition_table(self):
        _state = []
        _input = []
        _next_state = []

        for i in range(len(self.transitions)):
            _state.append(self.transitions[i]['current_state'])
            _input.append(self.transitions[i]['input_value'])
            _next_state.append(self.transitions[i]['next_state'])
        
        self._transition_table = pd.DataFrame({'current_state': _state, 'input_value': _input, 'next_state': _next_state})

        print(tabulate(self._transition_table.set_index('current_state'), headers = 'keys', tablefmt = 'pretty')) 
        return self

    def print_DFA(self):
        print("states: ",self.states)
        print("inputs: ",self.input_set)
        print("Initial state: ", self.initial_state)
        print("Final state: ", self.final_states)
        print("\n\t\tTransition table")
        self.print_transition_table()

    def get_input(self, input_string):
        for i in range(len(input_string)):
            input_char = input_string[i]
            if input_char not in self.input_set:
                print(input_char)
                print("There is no input in input_set")
                return self
            self.current_state = int(self._transition_table.loc[(self._transition_table['current_state']== self.current_state) \
                                     & (self._transition_table['input_value']==input_char)]['next_state'])
        print("current state: ", self.current_state)
        print("Accepted ? ---> ", self.accepted())
        self.reset()
        return self

    def reset(self):
        self.current_state = self.initial_state

    def accepted(self):
        if self.current_state in self.final_states:
            return True
            
    
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
    dfa.get_input('110101')

