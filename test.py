from petri import Place, Transition

def main():
    # Create Places
    place_A = Place("A",tokens=1)
    place_B = Place("B",tokens=1)
    place_C = Place("C",tokens=5)
    # Create Transitions
    transition_A_to_B = Transition("A&B_to_C", inputs=[place_A], full_inputs={place_C: 5}, outputs=[place_B])

    # Print initial state
    print(place_A)
    print(place_B)
    print(place_C)

    # Simulate
    transition_A_to_B.fire()

    # Print state after simulation
    print(place_A)
    print(place_B)
    print(place_C)

if __name__ == '__main__':
    main()