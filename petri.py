import random

class Place:
    def __init__(self, name, tokens=0):
        self.name = name
        self.tokens = tokens

    def add_tokens(self, n_tokens):
        self.tokens += n_tokens

    def __str__(self):
        return f"Place '{self.name}' with {self.tokens} token(s)"

class Transition:
    def __init__(self, names, inputs, outputs, ninputs=[], full_inputs={}):
        self.name = names
        self.inputs = inputs
        self.outputs = outputs
        self.ninput = ninputs
        self.full_input = full_inputs

    def is_enabled(self):
        # Check if input places have tokens
        inputs_enabled = all(place.tokens > 0 for place in self.inputs)
        # Check if negative input places do not have tokens
        ninput_enabled = all(place.tokens == 0 for place in self.ninput)
        # Check if full inputs have enough tokens
        full_input_enabled = all(place.tokens == required_tokens for place, required_tokens in self.full_input.items())

        return inputs_enabled and ninput_enabled and full_input_enabled

    def fire(self):
        if self.is_enabled():
            for place in self.inputs:
                place.tokens -= 1
            for place in self.outputs:
                place.tokens += 1
            print(f"Transition '{self.name}' fired")
        else:
            print(f"Transition '{self.name}' is not enabled")

class PetriNet:
    def __init__(self):
        self.places = {}
        self.transitions = []

    def add_place(self, place):
        self.places[place.name] = place

    def add_transition(self, transition):
        self.transitions.append(transition)

    def fire_transitions_at_random(self):
        random.shuffle(self.transitions)
        for transition in self.transitions:
            transition.fire()

    def display_places(self):
        for place in self.places.values():
            print(place)

    def add_tokens_to_place(self, place_name, num_tokens):
            self.places[place_name].add_tokens(num_tokens)



