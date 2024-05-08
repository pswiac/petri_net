from petri import Place, Transition, PetriNet
import random

SIM_ITERATIONS = 20
KIOSK_INPUT = 1
INPUT_ATTEMPT = 1

def kiosk_init():
    places = [Place("P_1", tokens=KIOSK_INPUT), Place("P_2"), Place("P_3"), Place("P_4"), Place("P_5"), Place("P_6"), Place("P_7"), Place("P_8"), Place("P_9")]

    transitions = [ Transition("t_1",inputs=[places[0]],outputs=[places[1]]),
                    Transition("t_2",inputs=[places[1]],outputs=[places[2]]), 
                    Transition("t_3",inputs=[places[2]],outputs=[places[3]]),
                    Transition("t_4",inputs=[places[3]],outputs=[places[4]]), 
                    Transition("t_5",inputs=[places[4]],outputs=[places[5]]),
                    Transition("t_6",inputs=[places[5]],outputs=[places[6]]),
                    Transition("t_7",inputs=[places[6]],outputs=[places[6]]), 
                    Transition("t_8",inputs=[places[3]],outputs=[places[2], places[7]]),
                    Transition("t_9",inputs=[places[7], places[2]],outputs=[places[8]]),
                    Transition("t_10",inputs=[places[8]],outputs=[places[5]]),
                    Transition("t_11",inputs=[places[6]],ninputs=[places[7]],outputs=[places[0]])]
    return transitions, places

def main():

    kiosk = PetriNet()
    
    kiosk_transitions, kiosk_places = kiosk_init()

    for place in kiosk_places:
        kiosk.add_place(place)

    for transition in kiosk_transitions:
        kiosk.add_transition(transition)        

    kiosk.display_places()
    i = 1
    while i <= SIM_ITERATIONS:
        kiosk.add_tokens_to_place("P_1", INPUT_ATTEMPT)
        kiosk.fire_transitions_at_random()
        i += 1

    kiosk.display_places()

if __name__ == '__main__':
    main()