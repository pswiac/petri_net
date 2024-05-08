# Petri Net Simulation

Class implementation for Petri Net modelling. 

*petri.py* - defining classes *Place*, *Transition* and *PetriNet*:

+ *Place* - this class has an attribute tokens, to keep track of events happening in the system, and it returns text to terminal with the Place’s information.

+ *Transition* - class which allows for initializing transitions with three different kinds of inputs, checking if the transition is enabled as well as a method to simulate firing. The three kinds of inputs are checked by the is_enabled for different conditions:
    - standard input - the method checks if all input Places have at least one token,
    - negative input ninput - the method checks if all ninput Places have zero tokens,
    - full_input - the method checks if all full_input have certain amount of tokens defined for the Place connected to the transition

+ *PetriNet* - class created to manage all the created transitions and places. It has methods for adding places and transitions, randomly firing transition - to simulate the system, displaying places - to verify results of simulation and a method for adding tokens to places.

***
