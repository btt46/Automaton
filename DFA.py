import pandas as pd
from tabulate import tabulate

class DFA:
    def __init__(self, states, input_set, transitions, initial_state, final_states):
        self.__states =  set(states)
        self.__input_set = set(input_set)
        self.__initial_state = initial_state
        self.__current_state = self.__initial_state
        self.__final_states = set(final_states)
        self.__transitions = transitions

        # check variables
        self.__check_variables()
        
    def __check_variables(self):
        # check type of state in the set of states
        for state in self.__states:
            if isinstance(state, int) == False:
                raise ValueError("The state must be an integer")

        # check type of input in the set of input values
        for input_value in self.__input_set:
            if isinstance(input_value, str) == False:
                raise ValueError("The input value must be a char")

        # check initial_state
        if self.__initial_state not in self.__states:
            raise ValueError("The initial state must be in the set of states")      

        # check current_state 
        if self.__current_state not in self.__states:
            raise ValueError("The current state must be in the set of states")    

        # check whether the set of final states is a subset of the set of states
        if self.__final_states.issubset(self.__states) == False:
            raise ValueError("The set of final states is not a subset of the set of states")        

    @property
    def transition_table(self):
        _state = []
        _input = []
        _next_state = []

        for i in range(len(self.__transitions)):
            _state.append(self.__transitions[i]['current_state'])
            _input.append(self.__transitions[i]['input_value'])
            _next_state.append(self.__transitions[i]['next_state'])
        
        return pd.DataFrame({'current_state': _state, 'input_value': _input, 'next_state': _next_state})

    def print_transition_table(self):
        print(tabulate(self.transition_table.set_index('current_state'), headers = 'keys', tablefmt = 'pretty')) 
        return self

    def print_DFA(self):
        print("states: ",self.__states)
        print("inputs: ",self.__input_set)
        print("Initial state: ", self.__initial_state)
        print("Final state: ", self.__final_states)
        print("\n\t\tTransition table")
        self.print_transition_table()

    def get_input(self, input_string):
        for input_char in input_string:
            if input_char not in self.__input_set:
                print(input_char)
                print("There is no input in input_set")
                return self
            self.__current_state = int(self.transition_table.loc[
                                                (self.transition_table['current_state']== self.__current_state) \
                                                & (self.transition_table['input_value']==input_char)        \
                                            ]['next_state']
                                      )

        print("current state: ", self.__current_state)
        print("Accepted ? ---> ", self.__accepted())
        self.__reset()

        return self

    def __reset(self):
        self.__current_state = self.__initial_state

    def __accepted(self):
        if self.__current_state in self.__final_states:
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


