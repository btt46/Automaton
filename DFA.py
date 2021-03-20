import pandas as pd
from tabulate import tabulate

class DFA:
    def __init__(self, states, input_set, transitions, initial_state, accepted_states):
        self.__states =  set(states)
        self.__input_set = set(input_set)
        self.__initial_state = initial_state
        self.__current_state = self.__initial_state
        self.__accepted_states = set(accepted_states)
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
                raise ValueError("The input value must be a string")

        # check initial_state
        if self.__initial_state not in self.__states:
            raise ValueError("The initial state must be in the set of states")      

        # check current_state 
        if self.__current_state not in self.__states:
            raise ValueError("The current state must be in the set of states")    

        # check whether the set of final states is a subset of the set of states
        if self.__accepted_states.issubset(self.__states) == False:
            raise ValueError("The set of final states is not a subset of the set of states")        

    # Create a data frame for transition functions
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

    # Return the input states
    @property
    def states(self):
        return self.__states
    
    # Return the set of input values
    @property
    def input_set(self):
        return self.__input_set

    # Return the initial state
    @property 
    def initial_state(self):
        return self.__initial_state

    # return the accepted states
    @property
    def accepted_states(self):
        return self.__accepted_states

    # print the trasition table
    def print_transition_table(self):
        print(tabulate(self.transition_table.set_index('current_state'), headers = 'keys', tablefmt = 'pretty')) 
        return self

    # print the DFA
    def print_DFA(self):
        print("states: ",self.states)
        print("inputs: ",self.input_set)
        print("Initial state: ", self.initial_state)
        print("Final state: ", self.accepted_states)
        print("\n\t\tTransition table")
        self.print_transition_table()

    # get an input string and return the final state and check
    # whether the given string is accepted or not
    def get_input(self, input_string):
        for input_char in input_string:
            if input_char not in self.__input_set:
                print("There is no input in input_set")
                return self
            else:
                self.__current_state = int(self.transition_table.loc[
                                              (self.transition_table['current_state']== self.__current_state) \
                                             &(self.transition_table['input_value']==input_char)        \
                                           ]['next_state'])
        output = (self.__current_state, self.__accepted())
        self.__print_result()        
        self.__reset()
        return output

    # set the current state to the initial state
    def __reset(self):
        self.__current_state = self.initial_state

    # check whether the current state is a accepted state
    def __accepted(self):
        if self.__current_state in self.accepted_states:
            return True
        return False

    def __print_result(self):
        # print current state and check whether 
        # the input string is accepted or not
        print("current state: ", self.__current_state)
        print("Accepted ? ---> ", self.__accepted())
    