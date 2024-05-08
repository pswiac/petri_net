from petri import Place, Transition, PetriNet
import random

CARS_AT_L1_DET_INIT = 1
CARS_AT_L2_DET_INIT = 1
CARS_AT_L3_DET_INIT = 1

CARS_RAND_ADD_RANGE = 1
SIM_ITERATIONS = 100
CARS_IN_PARKING = 20

def intersection_init():

    detection_state_L1 = Place("L1_det", tokens=CARS_AT_L1_DET_INIT)
    detection_state_L2 = Place("L2_det", tokens=CARS_AT_L2_DET_INIT)
    detection_state_L3 = Place("L3_det", tokens=CARS_AT_L3_DET_INIT)

    cars_waiting_L1 = Place("L1_wait")
    cars_waiting_L2 = Place("L2_wait")
    cars_waiting_L3 = Place("L3_wait")

    L1_red_forward = Place("L1_for_R", tokens=1)
    L1_green_forward = Place("L1_for_G")
    L1_red_left = Place("L1_left_R", tokens=1)
    L1_green_left = Place("L1_left_G")

    L2_green_right = Place("L2_right_G")
    L2_red_right = Place("L2_right_R", tokens=1)

    L3_green_right = Place("L3_right_G")
    L3_red_right = Place("L3_right_R", tokens=1)

    R1 = Place("R1", tokens=1)
    R2 = Place("R2", tokens=1)

    cars_in_P1 = Place("P1_cars", tokens = CARS_IN_PARKING)

    cars_gone_by_exit_1 = Place("Exit_1")

    # Car movement transitions

    L1_cars_arrive = Transition("L1_cars_arrive", inputs = [detection_state_L1], outputs = [cars_waiting_L1])
    L2_cars_arrive = Transition("L2_cars_arrive", inputs = [detection_state_L2], outputs = [cars_waiting_L2])
    L3_cars_arrive = Transition("L3_cars_arrive", inputs = [detection_state_L3], outputs = [cars_waiting_L3])

    cars_enter_P1_from_L1 = Transition("cars_enter_P1_from_L1", inputs=[cars_waiting_L1, L1_green_left], outputs=[cars_in_P1])
    cars_enter_P1_from_L2 = Transition("cars_enter_P1_from_L2", inputs=[cars_waiting_L2, L3_green_right], outputs=[cars_in_P1])
    parking_full = Transition("parking_full", inputs=[], full_inputs={cars_in_P1: 20}, outputs=[L1_red_forward, L3_red_right])
    cars_leave_exit_1 = Transition("cars_leave_exit_1", inputs=[cars_in_P1, cars_waiting_L2, L2_green_right], outputs=[cars_gone_by_exit_1])

    # Lights operation transitions

    T1 = Transition("T1", inputs=[L1_green_forward, R1], outputs=[L1_red_forward])
    T2 = Transition("T2", inputs=[L1_red_forward], outputs=[L1_green_forward, R1])

    T3 = Transition("T3", inputs=[R1, L1_red_left, R2], ninputs=[cars_in_P1, cars_waiting_L2], outputs=[L1_green_left])
    T4 = Transition("T4", inputs=[L1_green_left], outputs=[R1, L1_red_left, R2])

    T5 = Transition("T5", inputs=[cars_waiting_L3, R2, L3_red_right], ninputs=[cars_waiting_L2, cars_in_P1], outputs=[L3_green_right])
    T6 = Transition("T6", inputs=[L3_green_right], outputs=[R2, L3_red_right])

    T7 = Transition("T7", inputs=[cars_waiting_L2, L2_red_right], outputs=[L2_green_right])
    T8 = Transition("T8", inputs=[L2_green_right], outputs=[L2_red_right])

    transitions = [L1_cars_arrive, L2_cars_arrive, L3_cars_arrive, 
                   cars_enter_P1_from_L1, cars_enter_P1_from_L2, 
                   parking_full, cars_leave_exit_1, 
                   T1, T2, T3, T4, T5, T6, T7, T8]
    
    places = [detection_state_L1, detection_state_L2, detection_state_L3, 
          cars_waiting_L1, cars_waiting_L2, cars_waiting_L3, 
          L1_red_forward, L1_green_forward, L1_red_left, L1_green_left, 
          L2_green_right, L2_red_right, L3_green_right, L3_red_right, 
          R1, R2, cars_in_P1, cars_gone_by_exit_1]
    
    return transitions, places

def main():

    intersection = PetriNet()
    
    intersection_transitions, intersection_places = intersection_init()


    for place in intersection_places:
        intersection.add_place(place)

    
    for transition in intersection_transitions:
        intersection.add_transition(transition)        

    intersection.display_places()
    i = 1
    while i <= SIM_ITERATIONS:
        intersection.add_tokens_to_place("L1_det",random.randint(0,CARS_RAND_ADD_RANGE))
        intersection.add_tokens_to_place("L2_det",random.randint(0,CARS_RAND_ADD_RANGE))
        intersection.add_tokens_to_place("L3_det",random.randint(0,CARS_RAND_ADD_RANGE))
        intersection.fire_transitions_at_random()
        i += 1
    intersection.display_places()

if __name__ == '__main__':
    main()